
from django.conf.urls import url
from django.contrib import admin
from app.views import SubredditView, PostListView, SubredditCreateView, SubredditUpdateView, CommentListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subreddits/$', SubredditView.as_view(), name="subreddits_view"),
    url(r'^subreddits/(?P<pk>\d+)/$', PostListView.as_view(), name="post_list_view"),
    url(r'^subreddits/create/$', SubredditCreateView.as_view(), name="subreddit_create_view"),
    url(r'^subreddits/(?P<pk>\d+)/update/$', SubredditUpdateView.as_view(), name="subreddit_update_view"),
    url(r'^posts/(?P<pk>\d+)/$', CommentListView.as_view(), name="comment_list_view")
]
