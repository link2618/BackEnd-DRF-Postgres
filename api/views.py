from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
from api.models import User
from api.serializers import UserSerializer

import re
import hashlib

class Registrar(APIView):
    #Para no tener que usar authentication
    authentication_classes = ()
    permission_classes = ()

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
                    print(patron)
                    print(patron.search(passw))
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


class Login(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        data = request.data
        email = data.get('email')
        passw = data.get('password')
        password = hashlib.sha256(str(passw).encode('utf-8')).hexdigest()
        print(data)
        print(password)
        try:
            queryset = User.objects.filter(email=email, password=password)
            if queryset:
                print('Datos correctos')
                print(queryset[0])
                # token = Token.objects.create()
                mensaje = {
                    'message': 'success'
                }
                return Response(mensaje, status=status.HTTP_200_OK)
            else:
                #El ususario no existe
                mensaje = {
                    'message': 'Datos incorrecto.'
                }
                return Response(mensaje, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            mensaje = {
                'message': 'Datos incorrecto.'
            }
            return Response(mensaje, status=status.HTTP_200_OK)
