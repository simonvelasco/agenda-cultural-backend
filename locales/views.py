from django.shortcuts import render

# Create your views here.
from .models import Local
from .serializers import LocalSerializer
from rest_framework import viewsets
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView




class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


@api_view(['DELETE'])
def eliminar_todos_los_locales(request):
    try:
        locals.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocalesSolicitadosAPIView(APIView):
    def get(self, request, format=None):
        locales_solicitados = Local.objects.filter(estado="solicitado")        
        serializer = LocalSerializer(locales_solicitados, many=True)

        return Response(serializer.data)
    

class PublicarLocalAPIView(APIView):
    def put(self, request, pk, format=None):
        try:
            local = Local.objects.get(pk=pk)
            local.estado = "publicado"
            local.save()

            return Response({'message': 'Local publicado con éxito'}, status=status.HTTP_200_OK)
        except Local.DoesNotExist:
            return Response({'error': 'Local no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class LocalesPublicadosAPIView(APIView):
    def get(self, request, format=None):
        try:
            locales_publicados = Local.objects.filter(estado="publicado")
            serializer = LocalSerializer(locales_publicados, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
