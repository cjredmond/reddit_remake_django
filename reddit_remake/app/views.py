from django.shortcuts import render
from app.models import Post, Comment, Subreddit

def example_view(request):

    connor = Subreddit.objects.get(id =1)
    answer = connor.current_count()
    time = connor.creation_time
    today = connor.today_count()
    avg = connor.daily_avg()
    x = Post.objects.get(id = 1)
    y = x.is_recent()
    z = x.is_hot()

    context = {
    "sub" : Subreddit.objects.all(),
    "post" : Post.objects.all(),
    "com" : Comment.objects.all(),
    "connor" : answer,
    "avg" : avg,
    "y" : y,
    "z" : z
    }
    return render(request, "example.html", context)
