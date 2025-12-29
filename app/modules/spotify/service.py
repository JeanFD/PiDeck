import spotipy
from spotipy.oauth2 import SpotifyOAuth
from app.core.config import settings
import os

class SpotifyService:
    def __init__(self):
        # O ficheiro .spotify_cache será criado na raiz para manter a sessão ligada
        self.sp_oauth = SpotifyOAuth(
            client_id=settings.SPOTIPY_CLIENT_ID,
            client_secret=settings.SPOTIPY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIPY_REDIRECT_URI,
            scope="user-read-playback-state user-modify-playback-state",
            cache_path=".spotify_cache"
        )

    def get_auth_url(self):
        return self.sp_oauth.get_authorize_url()

    def get_token(self, code):
        return self.sp_oauth.get_access_token(code)

    def get_current_playback(self):
        token_info = self.sp_oauth.get_cached_token()
        if not token_info:
            return {"status": "unauthorized"}

        sp = spotipy.Spotify(auth=token_info['access_token'])
        
        try:
            current = sp.current_playback()
            if current and current['is_playing']:
                item = current['item']
                return {
                    "status": "playing",
                    "title": item['name'],
                    "artist": item['artists'][0]['name'],
                    "album": item['album']['name'],
                    "cover": item['album']['images'][0]['url'],
                    "progress_ms": current['progress_ms'],
                    "duration_ms": item['duration_ms'],
                    "is_playing": current['is_playing']
                }
            return {"status": "paused"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

# Instância única para ser usada pelo Router
spotify_service = SpotifyService()