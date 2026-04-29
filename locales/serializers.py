from rest_framework import serializers
from .models import Local

class LocalSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Local
        fields = [
            'nombre',
            'ubicacion',
            'telefono',
            'web',
            'imagen',
            'estado'
        ]

    def get_imagen(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None