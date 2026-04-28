from django.shortcuts import render

from .models import Evento
from .serializers import EventoSerializer, EventoYLocalSerializer
from rest_framework import viewsets
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import DateField
from datetime import datetime
from django.db.models.functions import Cast



class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


@api_view(['DELETE'])
def eliminar_todos_los_eventos(request):
    try:
        Evento.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class EventosPorFechaAPIView(APIView):
    def get(self, request, fecha, format=None):
        try:
            data = request.query_params
            categorias = request.GET.getlist('categorias', [])  # Obtiene las categorías como una lista
            horarios = data.getlist('horarios')

            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()            
            eventos = Evento.objects.filter(fecha=fecha).exclude(estado='solicitado').select_related('local')  


            if horarios:
                eventos = eventos.filter(horario__in=horarios)

            if categorias:
                eventos = eventos.filter(categoria__in=categorias)
                      
            serializer = EventoYLocalSerializer(eventos, many=True)            
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


        


class EventosFiltradosAPIView(APIView):
    def post(self, request):
        data = request.data
        categorias = data.get('categorias', [])

        # Comienza con una consulta sin filtros
        eventos = Evento.objects.all()

        # Aplica el filtro de horario si se seleccionó

        # Aplica el filtro de categorías si se seleccionaron
        if categorias:
            eventos = eventos.filter(categoria__in=categorias)

        # Serializa los eventos y devuelve la respuesta
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        
class EventoYLocalAPIView(APIView):
    def get(self, request, pk, format=None):
        try:
            evento = Evento.objects.filter(pk=pk).select_related('local').first()
            serializer = EventoYLocalSerializer(evento)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class EliminarEventosAnterioresAPIView(APIView):
    def delete(self, request, fecha, format=None):
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()            
            eventos_anteriores = Evento.objects.filter(fecha__lt=fecha)
            eventos_anteriores.delete()
            
            return Response({'message': 'Eventos anteriores eliminados con éxito'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

        
class EventosDestacadosAPIView(APIView):
    def get(self, request, format=None):
        try:
            eventos_destacados = Evento.objects.filter(estado='destacado').order_by('fecha')
            serializer = EventoYLocalSerializer(eventos_destacados, many=True)          
            response_data = serializer.data
            
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EventosPublicadosAPIView(APIView):
    def get(self, request, format=None):
        try:
            eventos_destacados = Evento.objects.exclude(estado='solicitado').order_by('fecha')
            serializer = EventoYLocalSerializer(eventos_destacados, many=True)          
            response_data = serializer.data
            
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class EventosSolicitadosAPIView(APIView):
    def get(self, request, format=None):
        eventos_solicitados = Evento.objects.filter(estado="solicitado").order_by('fecha')        
        serializer = EventoSerializer(eventos_solicitados, many=True)

        return Response(serializer.data)
    

class MarcarEventoComoDestacado(APIView):
    def put(self, request, pk, format=None):
        try:
            evento = Evento.objects.get(pk=pk)
            evento.estado = "destacado"
            evento.save()

            return Response({'message': 'El evento se ha marcado como destacado.'}, status=status.HTTP_200_OK)
        except Evento.DoesNotExist:
            return Response({'error': 'El evento no existe.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PublicarEventoAPIView(APIView):
    def put(self, request, pk, format=None):
        try:
            evento = Evento.objects.get(pk=pk)            
            evento.estado = "publicado"
            evento.save()
            
            return Response({'message': 'Evento publicado con éxito'}, status=status.HTTP_200_OK)
        except Evento.DoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class EventosPorCategoriaAPIView(APIView):
    def get(self, request, categoria, format=None):
        try:
            # Filtra los eventos por la categoría proporcionada y selecciona el campo 'local' relacionado
            eventos = Evento.objects.filter(categoria=categoria).exclude(estado='solicitado').select_related('local').order_by('fecha')
            
            # Utiliza un serializador que incluya información de ambos modelos (Evento y Local)
            serializer = EventoYLocalSerializer(eventos, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class EventosPorLocalAPIView(APIView):
    def get(self, request, nombre_local, format=None):
        try:
            # Filtra los eventos por el nombre del local proporcionado y selecciona el campo 'local' relacionado
            eventos = Evento.objects.filter(local__nombre=nombre_local, estado='publicado').select_related('local').order_by('fecha')
            
            # Utiliza un serializador que incluya información de ambos modelos (Evento y Local)
            serializer = EventoYLocalSerializer(eventos, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



