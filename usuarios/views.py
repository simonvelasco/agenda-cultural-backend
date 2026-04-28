# Create your views here.
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        try:
            user = Usuario.objects.get(nombre=username)

            if user.contrasena == password:
                return Response({'message': 'Usuario autenticado'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

        except Usuario.DoesNotExist:
            return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    

