from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "PiDeck"

    SPOTIPY_CLIENT_ID: str
    SPOTIPY_CLIENT_SECRET: str
    SPOTIPY_REDIRECT_URI: str

    class Config:
        env_file = ".env"

settings = Settings()