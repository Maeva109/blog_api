from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from posts.views import PostViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('app2/', include(router.urls)),
]
