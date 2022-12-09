from urllib.parse import urlparse
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CarroViewSet,
    FotoViewSet
    )

from . import views



routerProduto = SimpleRouter()
routerProduto.register('carro', CarroViewSet)
routerProduto.register('fotosCarro', FotoViewSet) 



urlpatterns = [
    # path('cadastro/', CadastroAPIView.as_view(), name='cadastro'),
    # path('email/', views.email_adocao, name ='email_adocao'),
    # path('emailSistema/', views.email_sistema, name ='email_sistema')
]