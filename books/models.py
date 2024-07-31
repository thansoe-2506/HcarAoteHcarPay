from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    # slug = models.SlugField(unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
            
    #         # Ensure the slug is unique
    #         unique_slug = self.slug
    #         num = 1
    #         while Book.objects.filter(slug=unique_slug).exists():
    #             unique_slug = '{}-{}'.format(self.slug, num)
    #             num += 1
    #         self.slug = unique_slug

    #     super().save(*args, **kwargs)


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

