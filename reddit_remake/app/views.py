from django.shortcuts import render
from app.models import Post, Comment, Subreddit
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

class SubredditView(ListView):
    template_name = "subreddits.html"
    model = Subreddit

class PostListView(ListView):
    model = Post

    def get_context_data(self):
        context = super().get_context_data()
        context["sub"] = Subreddit.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Post.objects.filter(subreddit = self.kwargs['pk'])

class PostCreateView(CreateView):
    model = Post
    success_url = "/subreddits"
    fields = ('title', 'description', 'body', 'url')

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id= self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    success_url = "/subreddits"
    fields = ('title', 'description', 'body', 'url')

class CommentCreateView(CreateView):
    model = Comment
    fields = ('text',)

    def get_success_url(self, **kwargs):
        return reverse('comment_list_view', args=self.kwargs['pk'])

    def form_valid(self,form):
        instance = form.save(commit = False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id= self.kwargs['pk'])
        return super().form_valid(form)

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

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/subreddits" #show reverse_lazy
