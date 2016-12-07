from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone
from django.utils import timezone


class Subreddit(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 40)
    creation_time = models.DateTimeField(auto_now_add=True)
    @property
    def current_count(self):
        posts = Post.objects.filter(subreddit = self)
        return posts.count()

    def today_count(self):
        posts = Post.objects.filter(creation_time__gt = (datetime.now() - timedelta(days=1))).filter(subreddit = self)
        return posts.count()

    def daily_avg(self):
        posts = Post.objects.filter(creation_time__gt = (datetime.now() - timedelta(days=7))).filter(subreddit = self)
        return (posts.count() / 7)
    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length = 40)
    description =  models.CharField(max_length = 255)
    body = models.TextField()
    url = models.URLField(max_length = 250, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)
    @property
    def is_recent(self):
        first = self.creation_time
        second = (timezone.now() - timedelta(days=1))
        if first > second:
            return True
        else:
            return False
    @property
    def is_hot(self):
        first = self.creation_time
        second = (timezone.now() - timedelta(hours=3))
        com = Comment.objects.filter(post=self).filter(created_time__gt = (datetime.now() - timedelta(hours=3)))
        if com.count() > 3:
            return True
        else:
            return False

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
