from django.db import models

# 게시글 모델
# 제목, 내용, 생성일자 ← 의 필드를 갖고 있는 모델
class Post(models.Model):
    title = models.CharField(max_length=100) # 100글자가 최대인 문자열
    content = models.TextField() # 글자 수 제한이 없는 긴 문자열
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성시, 현재시간 저장

# models.py안에 Post를 만듦으로써 model을 건듦 -> 데이터베이스에 넣기 전에 변경사항들을 쌓아놓음 -> migration
