from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
from api.models import User
from api.serializers import UserSerializer, TokenSerializer

import re
import hashlib

class Registrar(APIView):
    #Para no tener que usar authentication
    #authentication_classes = ()
    #permission_classes = ()

    def post(self, request):
        data = request.data
        print(data)
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
    #authentication_classes = ()
    #permission_classes = ()

    def post(self, request):
        data = request.data
        email = data.get('email')
        passw = data.get('password')
        password = hashlib.sha256(str(passw).encode('utf-8')).hexdigest()

        # Validaciones de datos recividos
        patronPass = re.compile(r"^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$")
        # Correo
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
            if patronPass.search(passw) != None:
                pass
            else:
                mensaje = {
                    'message': 'La contraseña debe tener al entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula y al menos una mayúscula.'
                               + ' NO puede tener otros símbolos.'
                }
                return Response(mensaje, status=status.HTTP_400_BAD_REQUEST)
        else:
            mensaje = {
                'message': 'Formato de correo invalido.'
            }
            return Response(mensaje, status=status.HTTP_400_BAD_REQUEST)

        # Se verifica si el usuario existe
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            mensaje = {
                'message': 'Datos incorrectos.'
            }
            return Response(mensaje, status=status.HTTP_200_OK)

        if user:
            # Generamos token y lo guardamos
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            token = {
                'refresh': refresh_token,
                'access': access_token,
                'user': user.id
            }
            serializer = TokenSerializer(data=token)
            if serializer.is_valid():
                try:
                    serializer.save()
                except:
                    mensaje = {
                        'message': 'Algo salio mal al guardar token.'
                    }
                    return Response(mensaje, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                usuario = {
                    'name': user.name,
                    'lastName': user.lastName,
                    'date': user.date,
                    'age': user.age,
                    'email': user.email,
                    'tipo': user.tipo
                }
                respuesta = {
                    'token': token,
                    'usuario': usuario
                }
                return Response(respuesta, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # El ususario no existe
            mensaje = {
                'message': 'Datos incorrecto.'
            }
            return Response(mensaje, status=status.HTTP_200_OK)

class Logout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        #Valor recibificdo por url
        #data = request.data
        #id = data.get('id')
        #print(id)
        #print(request)
        mensaje = {
            'message': 'Exito.'
        }
        return Response(mensaje, status=status.HTTP_200_OK)
