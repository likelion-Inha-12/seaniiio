from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_post), # 이 urls.py에는 ‘lion/create/’ 로 요청이 들어올 때, 우리가 만든 views.py 의 create_post 함수를 실행시키는 로직을 담고 있습니다.
    path('<int:pk>/', views.get_post), # int라는 타입의 pk 인자를 받겠다. get_post함수에 pk라고 정의했기 때문에 꼭 pk라고 적어줘야 함. ex) `lion/1`
    path('delete/<int:pk>/', views.delete_post),
    path('comments/<int:post_id>', views.get_comment)
]