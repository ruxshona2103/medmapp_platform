# blog/serializers.py
from rest_framework import serializers
from .models import BlogCategory, Post

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ("id", "name", "slug")

class PostListSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ("id", "title", "slug", "image", "summary", "category", "published_date")

class PostDetailSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            "id","title","slug","image","summary","content","category","author",
            "published_date","status","meta_title","meta_description","meta_keywords",
        )
