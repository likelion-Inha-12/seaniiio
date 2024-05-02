from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.health),
]

def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)