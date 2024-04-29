from django.db import models

# model을 수정하고 나면, makemigrations -> migrate과정을 거쳐야 함

# 게시글 모델
# 제목, 내용, 생성일자 ← 의 필드를 갖고 있는 모델
class Post(models.Model):
    title = models.CharField(max_length=50) # 50글자가 최대인 문자열
    content = models.TextField(null=True, blank=True) # 글자 수 제한이 없는 긴 문자열
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성시, 현재시간 저장

    def __str__(self):
        return self.title

# models.py안에 Post를 만듦으로써 model을 건듦 -> 데이터베이스에 넣기 전에 변경사항들을 쌓아놓음 -> migration

class Member(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class Comment(models.Model):
    content = models.CharField(max_length = 200, null = True, blank = True) # blank => ""
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments") # verbose_name => admin에서 보이는 이름 // cascade => Post를 지우면 관련된 Comment 싹다 지워짐

    def __str__(self):
        return self.content

class UserPost(models.Model):
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)