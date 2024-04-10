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