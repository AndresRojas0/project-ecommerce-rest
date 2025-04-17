from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication

class Authentication(object):

    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            user,token,message = token_expire.authenticate_credentials(token)
            if user != None and token != None:
                return user
            return message
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        # found token in request
        if user is not None:
            if type(user) == str:
                return Response({'error':user})
            return super().dispatch(request, *args, **kwargs)
        return Response({'error': 'No se han enviado las credenciales.'})

