from django.contrib import admin
from .models import Category,Post,Author,Comment,Reply

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Reply)