from django.db import models


class Tweet(models.Model):
    tweet_id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=500)
    url = models.URLField()
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=200)


class Domain(models.Model):
    tweet_id = models.BigIntegerField()
    domain_name = models.URLField()
