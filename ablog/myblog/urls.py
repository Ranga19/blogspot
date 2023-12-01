from django.urls import path
from .views import HomeView, CreatePost, PostDetail, UpdatePost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('update-post/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('delete-post/<int:pk>', DeletePost.as_view(), name='delete-post'),
 
]