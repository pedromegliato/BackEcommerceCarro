from dataclasses import fields
from rest_framework import serializers

from produtos.models import Carro, FotosCarro


class FotosCarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotosCarro
        fields = (
            'id',
            'fotos',
            'foto',
            'is_principal',
        )


class CarroSerializer(serializers.ModelSerializer):
    fotos = FotosCarroSerializer(many=True, read_only=True)
    class Meta:
        model = Carro
        fields = (
            'id',
            'nome',
            'marca',
            'modelo',
            'ano',
            'kilometragem',
            'valor',
            'valorPromocao',
            'is_promocao',
            'is_disponivel',
            'fotos',
        )