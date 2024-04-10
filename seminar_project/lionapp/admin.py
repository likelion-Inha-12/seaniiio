from django.contrib import admin

from .models import Post, Comment

# Register your models here.
admin.site.register(Post) # admin으로 Post를 관리하겠다
admin.site.register(Comment)