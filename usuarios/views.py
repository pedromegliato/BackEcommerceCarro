from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import viewsets
from usuarios.models import User
from usuarios.serializers import UsersSerializer



class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(UsersViewSet, self).get_permissions()

    def get_queryset(self):
        user = self.request.user
        if(user.is_staff == True):
            return User.objects.all()
        else:
            return User.objects.filter(id=user.id)

