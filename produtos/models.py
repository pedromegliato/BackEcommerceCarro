from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)
    kilometragem = models.CharField(max_length=255)
    valor = models.FloatField()
    valorPromocao = models.FloatField(blank=True, null=True)
    is_promocao = models.BooleanField(default=False, blank=True, null=True)
    is_disponivel = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['valor']


class FotosCarro(models.Model):
    fotos = models.ForeignKey(Carro, related_name='fotos', on_delete=models.CASCADE)
    foto = models.FileField(blank=True, null=True, default='')
    is_principal = models.BooleanField(default=True, blank=True, null=True)
