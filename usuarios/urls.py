from django.urls import path
from .views import UserLoginView, UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('usuarios_viewset', UsuarioViewSet, basename='usuarios_viewset')

urlpatterns = [
        path('login/', UserLoginView.as_view(), name='user-login'),
] + router.urls
