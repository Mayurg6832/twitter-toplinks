from django.urls import path, re_path
from django.views.generic import TemplateView
from linkapp import views

urlpatterns = [
    path('homepage/', views.home_page),
    path('signout/', views.signout, name='signout'),
    path('react/', views.to_react, name='all_tweets'),

    # Twitter
    path('api/authorize', views.Authorize.as_view(), name='auth'),
    re_path(r'^callback/$', views.LoadAllTweets.as_view()),
    path('api/all_tweets', views.AllTweetsList.as_view(), name='all_tweet'),
    path('api/top_domain', views.TopDomain.as_view(), name='top_domain'),
    path('api/top_user', views.TopUser.as_view(), name='top_user'),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
