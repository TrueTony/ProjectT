from django.contrib import admin

from .models import Author, Type, Course

admin.site.register(Author)
admin.site.register(Type)
admin.site.register(Course)
