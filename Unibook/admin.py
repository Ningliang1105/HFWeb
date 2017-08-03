from django.contrib import admin

# Register your models here.
from .models import Book,Category,Tag

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Book)
