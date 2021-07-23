from rest_framework import serializers
from linkapp.models import Tweet, Domain


class TweetSerializer(serializers.ModelSerializer):
    '''Serialize all Tweets'''

    class Meta:
        model = Tweet
        fields = '__all__'


class DomainSerializer(serializers.ModelSerializer):
    '''Serialize top Domains'''

    class Meta:
        model = Domain
        fields = ['domain_name']


class TopUserSerializer(serializers.ModelSerializer):
    '''Serialize Uses with Most URLs'''

    class Meta:
        model = Tweet
        fields = ['user_name']
