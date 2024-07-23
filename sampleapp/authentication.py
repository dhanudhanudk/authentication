from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from.models import APIKey

class APIkeyAuth(BaseAuthentication):
    def authenticate(self, request):
        api_key=request.headers.get('autharization')
        if not api_key:
            return  None
        try:
            key=APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('invaild key')
        return(None,None)
    
