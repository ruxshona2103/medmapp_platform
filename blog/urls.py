# blog/urls.py
from django.urls import path
from .views import CategoryListView, PostListView, PostDetailView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="blog-categories"),
    path("posts/", PostListView.as_view(), name="blog-posts"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="blog-post-detail"),
]
