from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from .models import BlogCategory, Post
from .serializers import BlogCategorySerializer, PostListSerializer, PostDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset = BlogCategory.objects.all().order_by("name")
    serializer_class = BlogCategorySerializer

    @swagger_auto_schema(
        operation_id="v1_blog_categories_list",
        operation_summary="Blog kategoriyalar ro‘yxati"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer

    @swagger_auto_schema(
        operation_id="v1_blog_posts_list",
        operation_summary="Blog postlar ro‘yxati",
        manual_parameters=[
            openapi.Parameter("category", openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Kategoriya slug"),
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Sarlavha/izoh qidiruv"),
            openapi.Parameter("status", openapi.IN_QUERY, type=openapi.TYPE_STRING, description="draft|published"),
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = Post.objects.select_related("category", "author")
        category = self.request.GET.get("category")
        search = self.request.GET.get("search")
        status = self.request.GET.get("status", "published")

        if category:
            qs = qs.filter(category__slug=category)
        if search:
            qs = qs.filter(Q(title__icontains=search) | Q(summary__icontains=search) | Q(content__icontains=search))
        if status:
            qs = qs.filter(status=status)

        return qs.order_by("-published_date", "-created_at")


class PostDetailView(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.select_related("category", "author")
    serializer_class = PostDetailSerializer

    @swagger_auto_schema(
        operation_id="v1_blog_posts_read",
        operation_summary="Bitta blog posti tafsilotlari"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
