from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):
    # expired = False

    def expires_in(self,token):
        # return left time of tokens
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self,token):
        # return True if token is alive or False if token is expired
        return self.expires_in(token) < timedelta(seconds = 0)

    def token_expire_handler(self,token):
        """
        Return:
            * is_expire     : True if token is active, False if token is expired
            * token         : New token or actual token
        """
        is_expire = self.is_token_expired(token)
        if is_expire:
            # self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
            
        #return is_expire,token
        return token

    def authenticate_credentials(self,key):
        """
        Return: 
            * user    : Instance User that sended request
            * token   : New Token or actual token for user
            * message : Error message
            * expired : True if token is alive or False if token is expired
        """
        "message,token,user = None,None,None"
        user = None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
            token = self.token_expire_handler(token)
        except self.get_model().DoesNotExist:
            pass
            # message = 'Token inválido.'
            # self.expired = True
        
        """
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado'

            is_expired = self.token_expire_handler(token)
            
            if is_expired:
                message = 'Su Token ha expirado.'
        """

        #return (user,token,message,self.expired)
        return user 