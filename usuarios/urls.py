from urllib.parse import urlparse
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (UsersViewSet)

from . import views


router = SimpleRouter()
router.register('user', UsersViewSet, basename="User")


urlpatterns = [
    # path('cadastro/', CadastroAPIView.as_view(), name='cadastro'),
    # path('email/', views.email_adocao, name ='email_adocao'),
    # path('emailSistema/', views.email_sistema, name ='email_sistema')
]