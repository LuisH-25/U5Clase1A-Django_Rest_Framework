from rest_framework import serializers
from .models import Pais

class PaisSerializador(serializers.ModelSerializer):
    class Meta:
        model = Pais                        # de que modelo viene
        fields = ('nombre','moneda')        # que campos son aceptados
        read_only_fields = ('creado_en')    # eviatr que el campo sea modificado en la db, solo es de lectura

