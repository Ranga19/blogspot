from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from api.serializers import PostSerializer
from django.http import JsonResponse
from rest_framework import serializers
from django.shortcuts import redirect

class HomeView(ListView):
    model = Post
    ordering = ['post_date']

class PostDetail(DetailView):
    model = Post


# class CreatePost(CreateAPIView):
#     serializer_class = PostSerializer
#     def perform_create(self, serializer):
#         serializer.save()
#         return redirect('home')

class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    def post(self, request):
        serializer = PostSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('home')
        
    

class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    
class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')