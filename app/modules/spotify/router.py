from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from .service import spotify_service

router = APIRouter()

@router.get("/status")
async def get_status():
    """Retorna o que está tocando atualmento no Spotify"""
    return spotify_service.get_current_playback()

@router.get("/login")
async def login():
    """Retorna a URL de login do Spotify"""
    return {"auth_url": spotify_service.get_auth_url()}

@router.get("/callback")
async def callback(code: str = Query(None)):
    """Recebe o código do Spotify após o login e redireciona para a Home"""
    if code:
        spotify_service.get_token(code)
    return RedirectResponse(url="/")