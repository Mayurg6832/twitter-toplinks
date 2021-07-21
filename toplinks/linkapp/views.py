from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
import tweepy
from django.db.models import Count
from rest_framework.response import Response
from linkapp.helper import past_7_days
from linkapp.models import Tweet, Domain
from linkapp.serializers import (
    TweetSerializer,
    DomainSerializer,
    TopUserSerializer
)


consumer_key = 'cB4CBHuRA6p2i58JW2ISrhjXf'
consumer_secret = 'aDwMm2Z3LdDnUDF576tCtJREQXa7a0Fo7EDnlOn8Vz6KX3vfLz'
callback_url = 'http://127.0.0.1:8000/callback/'


def home_page(request):
    '''Home Page to authorize and all tweets button'''

    return render(request, 'base.html')


def signout(request):
    '''To Signout the user'''

    request.session.clear()
    return HttpResponseRedirect('/')


def to_react(request):
    '''To redirect to React'''

    return HttpResponseRedirect('http://127.0.0.1:3000')


class Authorize(APIView):
    '''Authorize the consumer key and consumer secret key'''

    def get(self, request):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)
        auth_url = auth.get_authorization_url()
        response = HttpResponseRedirect(auth_url)
        request.session['request_token'] = auth.request_token
        return response


class LoadAllTweets(APIView):
    '''Varify and load all Tweets to Database'''

    def get(self, request):
        verifier = request.GET.get('oauth_verifier')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        token = request.session.get('request_token')
        request.session.delete('request_token')
        auth.request_token = token
        auth.get_access_token(verifier)
        api = tweepy.API(auth)
        screen_name = api.me().screen_name
        tweets = api.user_timeline(tweet_mode='extended')
        user_id = tweets[0].user.id_str
        tweets_7_days = past_7_days(tweets)

        # For self Tweets
        for tweet, domain in tweets_7_days:
            Tweet.objects.get_or_create(**tweet)
            Domain.objects.get_or_create(**domain)

        # For friends Tweets
        for follower in api.friends(screen_name):
            tweets = api.user_timeline(
                follower.screen_name,
                tweet_mode='extended',
            )
            tweets_7_days = past_7_days(tweets)
            for tweet, domain in tweets_7_days:
                Tweet.objects.get_or_create(**tweet)
                Domain.objects.get_or_create(**domain)

        request.session['user_id'] = user_id
        return HttpResponseRedirect('/')


class AllTweetsList(APIView):
    '''Returns List of all Tweets with URLs'''

    def get(self, request):
        tweets = Tweet.objects.all()
        tweet = TweetSerializer(tweets, many=True)
        return Response(tweet.data)


class TopUser(APIView):
    '''Return List of Users that has shared the most links '''

    def get(self, request):
        top_user = Tweet.objects.all().\
            values('user_name').\
            annotate(total=Count('url')).\
            order_by('-total')
        topUser = TopUserSerializer(top_user, many=True)
        return Response(topUser.data)


class TopDomain(APIView):
    '''Returns List of Top Domains that have been shared so far'''

    def get(self, request):
        top_domain = Domain.objects.all().\
            values('domain_name').\
            annotate(total=Count('domain_name')).\
            order_by('-total')
        domain = DomainSerializer(top_domain, many=True)
        return Response(domain.data)
