//-------------------------------------------------------------
// Nerea Aguilar Forés
// Lógica de la web: muestra la última medida recibida
//-------------------------------------------------------------
const API = "https://nagufor.upv.edu.es/app.php";

// Realiza una petición GET a la API para obtener la última medida
// si es válida, se muestra en la web
async function obtenerUltima() {
    const div = document.getElementById("resultado");

    try {
        const res = await fetch(API + "/medida/ultima");

        // Si la API no responde correctamente
        if (!res.ok) {
            div.innerHTML = "No hay medidas en la base de datos.";
            return;
        }

        const data = await res.json();
		let tipoMedida;
		
        if (data.tipo === 11) {
            tipoMedida = "CO₂";
        } else if (data.tipo === 12) {
            tipoMedida = "Temperatura";
        } else {
            tipoMedida = data.tipo;
        }

        // Mostrar
        div.innerHTML = `
            <b>ID:</b> ${data.id}<br>
            <b>Tipo:</b> ${tipoMedida}<br>
            <b>Medición:</b> ${data.medicion}<br>
            <b>Fecha:</b> ${data.fecha}
        `;

    } catch (err) {
        div.innerHTML = "Error al conectar con la API.";
    }
}

//Carga cada 5 segundos
window.onload = () => {
    obtenerUltima();
    setInterval(obtenerUltima, 5000);
};
