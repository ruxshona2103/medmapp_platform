# blog/admin.py
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import BlogCategory, Post

@admin.register(BlogCategory)
class BlogCategoryAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    list_display = ("title", "category", "status", "published_date")
    list_filter = ("status", "category")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"
    fieldsets = (
        ("Asosiy", {"fields": ("title", "slug", "image", "summary", "content")}),
        ("Teglar", {"fields": ("category", "author")}),
        ("Holat", {"fields": ("status", "published_date")}),
        ("SEO", {"fields": ("meta_title", "meta_description", "meta_keywords")}),
    )
