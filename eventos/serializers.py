from locales.serializers import LocalSerializer
from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [
            'id',
            'nombre',
            'fecha',
            'hora',
            'horario',
            'precio',
            'categoria',
            'local',
            'descripcion',
            'imagen',
            'estado'
        ]


class EventoYLocalSerializer(serializers.ModelSerializer):
    local = serializers.SerializerMethodField()

    class Meta:
        model = Evento
        fields = '__all__'

    def get_local(self, obj):
        local = obj.local
        if local:
            local_serializer = LocalSerializer(local)
            return local_serializer.data
        return None