"""
URL configuration for seminar_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('util.urls')), # util이라는 앱에서 사용하는 url은 항상 util.urls에서 관리해라
    path('lion/', include('lionapp.urls')), # lionapp의 urls.py에 작성한 url들을 seminar_project/urls.py에서 관리해라
    path('users/', include('users.urls'))
]