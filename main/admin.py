from django.contrib import admin

from .models import Content, Twitter, Outlet, Author, Annotation

@admin.register(Content, Twitter, Outlet, Author, Annotation)
class PersonAdmin(admin.ModelAdmin):
    pass