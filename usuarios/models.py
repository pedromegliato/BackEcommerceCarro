from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    nivelAcesso = models.CharField(max_length=25, default='1')
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)
    sobre = models.CharField(max_length=255, blank=True, null=True)