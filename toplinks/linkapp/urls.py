from django.urls import path, re_path
from linkapp import views

urlpatterns = [
    path('', views.home_page),
    path('signout/', views.signout, name='signout'),
    path('react/', views.to_react, name='all_tweets'),

    # Twitter
    path('api/authorize', views.Authorize.as_view(), name='auth'),
    re_path(r'^callback/$', views.LoadAllTweets.as_view()),
    path('api/all_tweets', views.AllTweetsList.as_view()),
    path('api/top_domain', views.TopDomain.as_view()),
    path('api/top_user', views.TopUser.as_view()),
]
