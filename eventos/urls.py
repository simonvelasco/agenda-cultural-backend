from django.urls import path
from .views import EventoViewSet, EventoYLocalAPIView, EventosPorCategoriaAPIView, EventosPorLocalAPIView, EventosSolicitadosAPIView, PublicarEventoAPIView, eliminar_todos_los_eventos, EventosPorFechaAPIView, EliminarEventosAnterioresAPIView, EventosDestacadosAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('eventos_viewset', EventoViewSet, basename='eventos_viewset')

urlpatterns = [
    path('eliminar-todos/', eliminar_todos_los_eventos, name='eliminar-todos'),
    path('eventos-fecha/<str:fecha>/', EventosPorFechaAPIView.as_view() , name='eventos-fecha'),
    path('eliminar-eventos-anteriores/<str:fecha>/', EliminarEventosAnterioresAPIView.as_view() , name='eliminar-eventos-anteriores'),
    path('eventos-destacados/', EventosDestacadosAPIView.as_view(), name='eventos-destacados'),
    path('eventos-solicitados/', EventosSolicitadosAPIView.as_view(), name='eventos-solicitados'),
    path('publicar-evento/<int:pk>/', PublicarEventoAPIView.as_view(), name='publicar-evento'),
    path('evento-local/<int:pk>/', EventoYLocalAPIView.as_view(), name='evento-local'),
    path('eventos-categoria/<str:categoria>/', EventosPorCategoriaAPIView.as_view(), name='eventos-categoria'),
    path('eventos-local/<str:nombre_local>/', EventosPorLocalAPIView.as_view(), name='eventos-local'),
] + router.urls
