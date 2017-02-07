import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from .models import Usuario, Canal
from .serializers import UsuarioSerializer, AreaConocimientoSerializer, CanalSerializer
from django.shortcuts import render


# Create your views here.

class UsuarioList(APIView):
    """
    Lista de todos los usuarios, o crear un nuevo usuario
    """
    def get(self, request, format=None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    """
    Recuperar, actualizar o borrar una instancia de Usuario
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CanalList(generics.ListCreateAPIView):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

class CanalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer


