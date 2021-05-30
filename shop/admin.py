from django.contrib import admin

# Register your models here.
from .models import Unit, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Unit)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Unit


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
