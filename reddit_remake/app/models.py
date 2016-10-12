from django.db import models
from django.contrib.auth.models import User

class Subreddit(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 40)
    creation_time = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        posts = Post.objects.filter(subreddit = self)
        count = 0
        for post in posts:
            count += 1
        return count

    def today_count(self):
        pass
    def daily_avg(self):
        pass
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
    user = models.ForeignKey(User, null=True, blank = True)

    def is_recent(self):
        pass
    def is_hot(self):
        pass
    def __str__(self):
        return self.title
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, blank = True)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
