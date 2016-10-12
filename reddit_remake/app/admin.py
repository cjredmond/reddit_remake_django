from django.contrib import admin
from app.models import Post,Subreddit,Comment

admin.site.register([Post, Subreddit, Comment])
# Register your models here.
