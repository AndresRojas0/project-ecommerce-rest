#from datetime import datetime

#from django.contrib.sessions.models import Session

from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.authtoken.models import Token
#from rest_framework.authtoken.views import ObtainAuthToken

#from apps.users.api.serializers import UserTokenSerializer
#from apps.users.authentication_mixins import Authentication

from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import (
    CustomTokenObtainPairSerializer,
    CustomUserSerializer
)
from apps.users.models import User
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesión Exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, 
            status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user',''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, 
            status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)


'''
class UserToken(Authentication, APIView):
    """
    Return Token for for an username sended
    """
    def get(self,request,*args,**kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user = self.user)
            user = UserTokenSerializer(self.user)
            return Response({
                'token': user_token.key,
                'user': user.data
            })
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas.'
            },status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):

    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            print(login_serializer.validated_data['user'])
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created= Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    },status = status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status= status.HTTP_201_CREATED)
                    """
                    return Response({
                        'error': 'Ya se ha iniciado sesión con este usuario.'
                    }, status = status.HTTP_409_CONFLICT)
                    """
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, 
                    status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, 
                status = status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Hola desde response'}, status = status.HTTP_200_OK)

class Logout(APIView):

    def get(self,request,*args,**kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user
                # delete all sessions for user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            # search auth_user_id, this field is primary_key's user on the session
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                # delete user token
                token.delete()

                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({'token_message': token_message, 'session_message': session_message}, 
                status = status.HTTP_200_OK)

            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'},
                status = status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error': 'No se ha encontrado token en la petición.'},
            status = status.HTTP_409_CONFLICT)
'''