from django.db import models
from account.models import User
from django.utils import timezone
from django.utils.html import format_html
from config import settings
from django.urls import reverse
from extensions.utils import date_converter
from .managers import ArticleManager, CategoryManager


# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True,
                               blank=True, on_delete=models.SET_NULL, related_name='children')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        # if settings.LANGUAGE_CODE == 'fa-ir':
        #     verbose_name = "مقاله"
        #     verbose_name_plural = "مقالات"
        ordering = ['parent__id', 'position']

    def __str__(self) -> str:
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    if settings.LANGUAGE_CODE == 'fa-ir':
        STATUS_CHOICES = (
            ('d', 'پیش نویس'),
            ('p', 'منتشر شده'),
        )
        title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
        slug = models.SlugField(max_length=100, unique=True,
                                verbose_name="آدرس مقاله")
        description = models.TextField(verbose_name="محتوا")
        thumbnail = models.ImageField(
            upload_to="images", verbose_name="تصویر مقاله")
        publish = models.DateTimeField(
            default=timezone.now, verbose_name="زمام انتشار")
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(
            max_length=1, choices=STATUS_CHOICES, verbose_name="موضوعات")
    else:
        STATUS_CHOICES = (
            ('d', 'Draft'),
            ('pb', 'Publish'),
            ('pd', 'Pending'),
            ('b', 'Back'),
        )
        author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles")
        title = models.CharField(max_length=200)
        slug = models.SlugField(max_length=100, unique=True)
        category = models.ManyToManyField(Category, related_name="articles")
        description = models.TextField()
        thumbnail = models.ImageField(upload_to="images")
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        is_special = models.BooleanField(default=False)
        status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    # for making persian only for this class Article
    class Meta:
        if settings.LANGUAGE_CODE == 'fa-ir':
            verbose_name = "مقاله"
            verbose_name_plural = "مقالات"
        ordering = ["-publish"]

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("account:home")

    def jpublish(self):
        return date_converter(self.publish)

    def thumbnail_tag(self):
        return format_html("<img src = '{}' width = 120px style = 'border-radius: 5px;'>".format(self.thumbnail.url))
    
    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])

    objects = ArticleManager()

# In order to use this in user front end of your site import this class in your base_tag


# class siteSetting:
    # title = models.CharField(max_length=255)
    # blog_title = models.CharField(max_length=255)
