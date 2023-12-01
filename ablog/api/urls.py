from django.urls import path
from myblog.views import CreatePost

urlpatterns = [
    path('create-post/', CreatePost.as_view(), name='create-post'),
    
]