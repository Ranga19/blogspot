from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    ordering = ['post_date']

class PostDetail(DetailView):
    model = Post

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')