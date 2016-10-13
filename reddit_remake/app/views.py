from django.shortcuts import render
from app.models import Post, Comment, Subreddit
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

class SubredditView(ListView):
    template_name = "subreddits.html"
    model = Subreddit

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(subreddit = self.kwargs['pk'])

class SubredditCreateView(CreateView):
    model = Subreddit
    success_url = "/subreddits"
    fields = ('name', 'description')

class SubredditUpdateView(UpdateView):
    model = Subreddit
    success_url = "/subreddits"
    fields = ('name', 'description')

class CommentListView(ListView):
    model = Comment

    def get_context_data(self):
        context = super().get_context_data()
        context["post"] = Post.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Comment.objects.filter(post = self.kwargs['pk'])
