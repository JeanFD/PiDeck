function updateTime() {
    const now = new Date();
    
    // Formata Hora (HH:MM)
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    
    document.getElementById('time-hours').innerText = hours;
    document.getElementById('time-min').innerText = minutes;

    // Formata Data (Ex: Segunda-feira, 25 de Dezembro)
    const optionsDay = { weekday: 'long' };
    const optionsFull = { day: 'numeric', month: 'long' };
    
    // pt-BR para garantir português
    document.getElementById('date-weekday').innerText = now.toLocaleDateString('pt-BR', optionsDay);
    document.getElementById('date-full').innerText = now.toLocaleDateString('pt-BR', optionsFull);
}

async function updateInfo() {
    try {
        // Chama nosso backend modular
        const res = await fetch('/api/clock/info');
        const data = await res.json();
        
        document.getElementById('greeting-text').innerText = data.greeting;
        document.getElementById('weather-temp').innerText = data.weather.temp;
        document.getElementById('weather-icon').innerText = data.weather.icon;
        
    } catch (error) {
        console.error("Erro ao buscar info do relógio", error);
    }
}

// Inicia
setInterval(updateTime, 1000); // Atualiza hora a cada segundo
setInterval(updateInfo, 60000); // Atualiza clima/saudação a cada 1 minuto
updateTime();
updateInfo();