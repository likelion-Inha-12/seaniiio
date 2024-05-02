import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import *

# POST api
def create_post(request):
    if request.method == 'POST':

        data = json.loads(request.body) # 요청 데이터
        title = data.get('title') # title이라는 key에 대한 value를 title에 넣음
        content = data.get('content') # content라는 key에 대한 value를 content에 넣음

        post = Post(
            title = title, # title에는 위에서 받은 title에 대한 value를 넣어줌
            content = content # content에는 위에서 받은 content에 대한 value를 넣어줌
        )
        post.save()

        return JsonResponse({'message' : 'success'})
    return JsonResponse({'message':'POST 요청만 허용합니다.'})

# READ api
def get_post(request, pk): # 어떤 데이터를 읽을 것인지 명시하기 위해 pk 사용(고유 식별자)
    post = get_object_or_404(Post, pk = pk) # pk가 pk인 Post를 찾았다면 get object를 하고, 못 찾았다면 404를 띄워라
    data = {
        'id': post.pk,
        '제목': post.title,
        '내용': post.content,
        '메시지': '조회 성공'
    }
    return JsonResponse(data, status=200) # read이기 때문에 data를 return, 응답 코드는 200

# DELETE api
def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk = pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

# post에 대한 comment 가져오는 api
def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all() # Post에 comments필드가 있는 것은 아니지만, models.py에 related_name으로 정의해주었음. // comments => comment_set으로 변경해도 같은 기능을 하지만, relate_name을 설정해놓으면 작동 안함
        return HttpResponse(comment_list, status=200)
    
# user_id와 post_id를 request로 받고 좋아요를 누르는 api
def post_like(request, post_id, user_id):
    if request.method == 'POST':

        # 이미 사용자가 해당 게시물에 좋아요를 누른 경우
        if UserPost.objects.filter(user_id=user_id, post_id=post_id).exists():
            return HttpResponse("이미 좋아요를 눌렀습니다.", status=409)
        
        user = Member.objects.get(pk = user_id)
        post = Post.objects.get(pk = post_id)

        userPost = UserPost(
            user_id = user,
            post_id = post
        )
        userPost.save()

        return HttpResponse(status=204)

# post_id를 request로 받아 좋아요 개수를 반환하는 api
def get_like_count(request, post_id):
    if request.method == 'GET':

        # 해당 post가 존재하지 않는 경우 404
        post = get_object_or_404(Post, pk=post_id)

        like_count = UserPost.objects.filter(post_id = post_id).count()

        return JsonResponse({"like_count":like_count})

# 댓글이 많이 달린 순으로 post를 정렬하여 리스트로 반환하는 api 
def get_post_sorted(request):
    if request.method == 'GET':

        post_comment_counts = [] # 모든 post에 대해 (post, comment 개수) 형태로 저장

        posts = Post.objects.all() # post들 불러오기

        for post in posts:
            # 역참조를 이용해서 댓글 개수 읽어오기
            comment_count = post.comments.all().count() # related_name = 'comments'
            post_comment_counts.append((post, comment_count))
        
        # sort
        post_comment_counts.sort(key = lambda x:-x[1]) # comment_count가 높은 순서대로 sort
        sorted_post_list = [p[0] for p in post_comment_counts] # post만 빼와서 return할 리스트 생성

        return HttpResponse(sorted_post_list, status=200)
# sorted_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count') 