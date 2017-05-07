from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

from udemy_api.serializers import UsuarioSerializer
from udemy_api.models import Usuario


class UserViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
