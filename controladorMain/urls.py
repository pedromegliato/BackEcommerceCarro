from os import stat
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from usuarios.urls import router
from produtos.urls import routerProduto
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Ecommerce Carros API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/', include(router.urls)),
    path('api/v1/', include(routerProduto.urls)),
    path('api/v1/', include('usuarios.urls')),
]

urlpatterns += [
    path('api/v1/reset/', include('djoser.urls')),
    path('api/v1/reset/auth/', include('djoser.urls.authtoken')),
    path('api/v1/reset/auth/', include('djoser.urls.jwt')),
]

urlpatterns += [
    url(r'^$', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
