from django.db import models
from tinymce import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()


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


class PolicyContent(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)
    content = HTMLField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.start_date)
