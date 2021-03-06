"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('room-detail@<str:page>/', RoomDetail.as_view()),
    path('news-create@<str:page>/',NewsCreate.as_view()),
    path('feedback-detail@<str:page>/',FeedbackDetail.as_view()),
    path('<str:page>/', Page.as_view()),
    path('a/', include('admin_end.urls')),
    path('u/', include('user_end.urls')),
]
