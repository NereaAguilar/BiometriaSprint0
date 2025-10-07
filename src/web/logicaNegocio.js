const API = "https://nagufor.upv.edu.es/app.php";

async function obtenerUltima() {
    const div = document.getElementById("resultado");
    try {
        const res = await fetch(API + "/medida/ultima");
        if (!res.ok) {
            div.innerHTML = "No hay medidas en la base de datos.";
            return;
        }
        const data = await res.json();
        div.innerHTML = `
            <b>ID:</b> ${data.id}<br>
            <b>Tipo:</b> ${nombreTipo(data.tipo)}<br>
            <b>Medición:</b> ${data.medicion}<br>
            <b>Fecha:</b> ${data.fecha}
        `;
    } catch (err) {
        div.innerHTML = "Error al conectar con la API.";
    }
}

function nombreTipo(tipo) {
    if (tipo === 11) return "CO₂ (ppm)";
    if (tipo === 12) return "Temperatura (°C)";
    if (tipo === 13) return "Ruido (dB)";
    return "Desconocido";
}

window.onload = () => {
    obtenerUltima();
    setInterval(obtenerUltima, 5000);
};
