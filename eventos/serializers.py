from locales.serializers import LocalSerializer
from rest_framework import serializers

from .models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [  'id',
                    'nombre',
                    'fecha',
                    'hora',
                    'horario',
                    'precio',
                    'categoria',
                    'local',
                    'descripcion',
                    'imagen',
                    'estado' ]



class EventoYLocalSerializer(serializers.ModelSerializer):
    # Define los campos del modelo Evento que deseas incluir
    local = serializers.SerializerMethodField()  # Campo personalizado para la información del local
    
    class Meta:
        model = Evento
        fields = '__all__'  # Incluye todos los campos del modelo Evento

    def get_local(self, obj):
        # Serializa la información del local
        local = obj.local
        if local:
            local_serializer = LocalSerializer(local)
            return local_serializer.data
        return None
    

    