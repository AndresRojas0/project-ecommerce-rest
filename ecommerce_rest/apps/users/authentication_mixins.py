from rest_framework import status, authentication, exceptions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(authentication.BaseAuthentication):
    user = None
    # user_token_expired = False

    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            # user,token,message,self.user_token_expired = token_expire.authenticate_credentials(token)
            user = token_expire.authenticate_credentials(token)
            
            if user != None:
                self.user = user
                return user
            # return message

        return None

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales.')

        return (self.user, None)

'''
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        # found token in request
        if user is not None:
            return super().dispatch(request, *args, **kwargs)
            """
            Possible value of variable user:
            * User Instance
            * Message like: Token Inválido, Usuario no activo o eliminado, Su Token ha expirado
            """
            """
            if type(user) == str:
                response = Response({'error':user,'expired': self.user_token_expired},
                                    status = status.HTTP_401_UNAUTHORIZED)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            """
            # only user_token_expired = True, the request can be continue
            #if not self.user_token_expired:
            

        # response = Response({'error': 'No se han enviado las credenciales.',
        #    'expired': self.user_token_expired},status = status.HTTP_400_BAD_REQUEST)
        response = Response({'error': 'No se han enviado las credenciales.',
            },status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response
'''