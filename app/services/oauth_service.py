from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from app.config import settings

class OAuth2Service:
    def __init__(self):
        config = Config(environ={
            'GOOGLE_CLIENT_ID': settings.GOOGLE_CLIENT_ID,
            'GOOGLE_CLIENT_SECRET': settings.GOOGLE_CLIENT_SECRET,
        })
        
        self.oauth = OAuth(config)
        self.oauth.register(
            name='google',
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET,
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_kwargs={
                'scope': 'openid email profile'
            }
        )
    
    def get_google_client(self):
        return self.oauth.google

oauth2_service = OAuth2Service()