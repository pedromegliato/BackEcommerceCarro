from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import pagination

from produtos.models import Carro, FotosCarro
from produtos.serializers import CarroSerializer, FotosCarroSerializer



class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def get_permissions(self):
        user = self.request.user
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ] 
            # if(user.is_superuser == False):
            #      pagination.PageNumberPagination.page_size = 8
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(CarroViewSet, self).get_permissions()

class FotoViewSet(viewsets.ModelViewSet):
    queryset = FotosCarro.objects.all()
    serializer_class = FotosCarroSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]
        return super(FotoViewSet, self).get_permissions()

