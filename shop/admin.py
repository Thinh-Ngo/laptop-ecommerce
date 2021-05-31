from django.contrib import admin

# Register your models here.
from .models import Unit, PostImage, PolicyContent


admin.site.register(PolicyContent)


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
