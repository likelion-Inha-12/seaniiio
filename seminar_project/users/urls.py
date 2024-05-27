from django.urls import include, path
from . import views

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('refresh', views.refresh),
    path('v2/refresh', jwt_views.TokenRefreshView.as_view()), # rest_framework_simplejwt 이용
]