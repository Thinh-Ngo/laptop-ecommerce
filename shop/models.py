from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Unit(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    desciption = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Unit, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title
