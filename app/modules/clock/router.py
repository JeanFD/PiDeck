from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/time")
async def get_current_time():
    """
    Simula os dados extras que o InkyPi mostra:
    - Saudação baseada na hora
    - Clima (Simulado por enquanto)
    """
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Bom dia"
    elif 12 <= hour < 18:
        greeting = "Boa tarde"
    else:
        greeting = "Boa noite"

    return {
        "greeting": greeting,
        "weather": {
            "temp": "24°C",        # Futuro: Pegar do OpenWeather
            "condition": "Céu Limpo",
            "icon": "☀️"
        }
    }