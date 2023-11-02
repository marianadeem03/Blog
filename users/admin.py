from django.contrib import admin
from users.models import User
from blog_app.models import Category, Post, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
