from django.urls import path
from .views import LocalViewSet, LocalesPublicadosAPIView, LocalesSolicitadosAPIView, PublicarLocalAPIView, eliminar_todos_los_locales
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('locales_viewset', LocalViewSet, basename='locales_viewset')

urlpatterns = [
    path('eliminar-todos/', eliminar_todos_los_locales, name='eliminar-todos'),
    path('locales-solicitados/', LocalesSolicitadosAPIView.as_view(), name='locales-solicitados'),
    path('publicar-local/<str:pk>/', PublicarLocalAPIView.as_view(), name='publicar-local'),
    path('locales-publicados/', LocalesPublicadosAPIView.as_view(), name='locales-publicados'),

] + router.urls
