from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.humanize.templatetags import humanize
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from PIL import Image 


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="article_img/")
    alternative_text = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, unique=True)
    snippet = models.TextField()
    detail = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    is_interesting = models.BooleanField(default=False)
    is_mysterious = models.BooleanField(default=False)
    most_read = models.BooleanField(default=False)
    most_shared = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Articles'

    def get_date(self):
        return humanize.naturaltime(self.date_published)

    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="40" />' % (self.image.url))

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 850 or img.width > 1050:
            output_size = (850, 1050)      
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={'slug': self.slug})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.description, self.name)


class SubscribeContent(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email 

    