# blog/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField

User = get_user_model()

class BlogCategory(models.Model):
    name = models.CharField("Nomi", max_length=255)
    slug = models.SlugField("Slug", unique=True, max_length=255)

    class Meta:
        verbose_name = "Blog kategoriya"
        verbose_name_plural = "Blog kategoriyalar"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Post(models.Model):
    DRAFT = "draft"
    PUBLISHED = "published"
    STATUS_CHOICES = [(DRAFT, "Qoralama"), (PUBLISHED, "Chop etilgan")]

    title = models.CharField("Sarlavha", max_length=255)
    slug = models.SlugField("Slug", unique=True, max_length=255)
    image = models.ImageField("Rasm", upload_to="blog/", blank=True, null=True)
    summary = models.TextField("Qisqa izoh", blank=True)
    content = RichTextField("Kontent")

    category = models.ForeignKey(BlogCategory, verbose_name="Kategoriya", on_delete=models.SET_NULL, null=True, related_name="posts")
    author = models.ForeignKey(User, verbose_name="Muallif", on_delete=models.SET_NULL, null=True, related_name="posts")

    published_date = models.DateTimeField("Chop etilgan sana", blank=True, null=True)
    status = models.CharField("Holat", max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    # SEO
    meta_title = models.CharField("Meta sarlavha", max_length=255, blank=True)
    meta_description = models.TextField("Meta tavsif", blank=True)
    meta_keywords = models.CharField("Meta kalit so‘zlar", max_length=500, blank=True)

    created_at = models.DateTimeField("Yaratildi", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilandi", auto_now=True)

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        ordering = ["-published_date", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

