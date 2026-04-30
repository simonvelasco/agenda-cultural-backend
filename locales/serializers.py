from rest_framework import serializers
from .models import Local

class LocalSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Local
        fields = [
            'nombre',
            'ubicacion',
            'telefono',
            'web',
            'imagen',
            'imagen_url',
            'estado'
        ]

    def get_imagen_url(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None