# commentaries/urls.py
from django.urls import path
from .views import PostCreateView, PostListView, list_posts, update_post

urlpatterns = [
    # path('list/', PostListView.as_view(), name='list_post'),
    path('list/', list_posts, name='list_posts'),
    path('update/<slug:slug>', update_post, name='update_post'),
    path('add/', PostCreateView.as_view(), name='create_post'),
]