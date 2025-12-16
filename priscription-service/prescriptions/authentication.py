import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        
        if not auth_header:
            return None
        
        try:
            prefix, token = auth_header.split(' ')
            if prefix.lower() != 'bearer':
                return None
            
            payload = jwt.decode(
                token, 
                settings.JWT_SECRET_KEY, 
                algorithms=['HS256']
            )
            
            email = payload.get('email')
            role = payload.get('role')
            
            if not email:
                raise exceptions.AuthenticationFailed('Invalid token')
            
            # Create a simple user object
            class User:
                def __init__(self, email, role):
                    self.email = email
                    self.role = role
                    self.is_authenticated = True
                    self.is_admin = role == 'ROLE_ADMIN'
            
            user = User(email, role)
            return (user, None)
            
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))