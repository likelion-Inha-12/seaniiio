from django.contrib import admin

from .models import Post, Comment, Member, UserPost

# Register your models here.
admin.site.register(Post) # admin으로 Post를 관리하겠다
admin.site.register(Comment)
admin.site.register(Member)
admin.site.register(UserPost)
