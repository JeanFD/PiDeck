from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.modules.clock.router import router as clock_router

from app.modules.spotify.router import router as spotify_router

app = FastAPI(title="PiDeck Modulas OS")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(clock_router, prefix="/api/clock", tags=["Clock"])

app.include_router(spotify_router, prefix="/api/spotify", tags=["Spotify"])

@app.get("/")
async def desktop(request: Request):
    """Renderiza a tela principal (Dashboard)"""
    return templates.TemplateResponse("desktop.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    # Se rodar via python main.py
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)