# blog/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import BlogCategory, Post

@register(BlogCategory)
class BlogCategoryTR(TranslationOptions):
    fields = ("name",)

@register(Post)
class PostTR(TranslationOptions):
    fields = ("title", "summary", "content", "meta_title", "meta_description", "meta_keywords")
