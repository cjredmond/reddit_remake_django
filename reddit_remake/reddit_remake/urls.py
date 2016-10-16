
from django.conf.urls import url, include
from django.contrib import admin
from app.views import SubredditView, PostListView, SubredditCreateView, SubredditUpdateView, \
CommentListView, PostCreateView, CommentCreateView, UserCreateView, PostUpdateView, CommentUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subreddits/$', SubredditView.as_view(), name="subreddits_view"),
    url(r'^subreddits/(?P<pk>\d+)/$', PostListView.as_view(), name="post_list_view"),
    url(r'^subreddits/create/$', SubredditCreateView.as_view(), name="subreddit_create_view"),
    url(r'^subreddits/(?P<pk>\d+)/update/$', SubredditUpdateView.as_view(), name="subreddit_update_view"),
    url(r'^posts/(?P<pk>\d+)/$', CommentListView.as_view(), name="comment_list_view"),
    url(r'^subreddits/(?P<pk>\d+)/post_create$', PostCreateView.as_view(), name="post_create_view" ),
    url(r'^posts/(?P<pk>\d+)/comment_create$', CommentCreateView.as_view(), name="comment_create_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^posts/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name="post_update_view"),
    url(r'^', include('django.contrib.auth.urls')),
    #url(r'^posts/(?P<pk>\d+)/comment_update/(?P<ck>\d+)$', CommentUpdateView.as_view(), name="comment_update_view"),
    url(r'^comment_update/(?P<pk>\d+)$', CommentUpdateView.as_view(), name="comment_update_view"),

]
