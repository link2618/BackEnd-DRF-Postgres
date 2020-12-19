from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from api.serializers import UserSerializer

import re

class Registrar(APIView):
    def post(self, request):
        data = request.data
        tipo = data.get("tipo")
        passw = data.get("password")
        nombre = data.get("name")
        apellido = data.get("lastName")
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            if tipo == 'CLIENTE' or tipo == 'ADMIN' or tipo == '':
                if bool(re.search(r'\d', nombre)) or bool(re.search(r'\d', apellido)):
                    mensaje = {
                        'message': 'El nombre y appellido no pueden contener numeros.'
                    }
                    return Response(mensaje, status=status.HTTP_400_BAD_REQUEST)
                else:
                    patron = re.compile(r"^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$")
                    if patron.search(passw) != None:
                        serializer.save()
                        mensaje = {
                            'message': 'success'
                        }
                        return Response(mensaje, status=status.HTTP_201_CREATED)
                    else:
                        mensaje = {
                            'message': 'La contraseña debe tener al entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula y al menos una mayúscula.'
                                        + ' NO puede tener otros símbolos.'
                        }
                        return Response(mensaje, status=status.HTTP_400_BAD_REQUEST)
            else:
                mensaje = {
                    'message': 'El tipo es incorrecto.'
                }
                return Response(mensaje, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
