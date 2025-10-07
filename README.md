🌱 **Proyecto Biometría Sprint 0 – 2025**  
📍 *Universitat Politècnica de València*  
👩‍💻 *Autora:* **Nerea Aguilar Forés**

---

**Web del proyecto (Plesk):**  
[https://nagufor.upv.edu.es](https://nagufor.upv.edu.es)

Repositorio del sistema completo de monitorización de datos ambientales.  
Integra hardware (Arduino), aplicación Android, servidor PHP y visualización web.

---

## Contenido del Proyecto

- **Arduino (C++)** → Emisión de tramas BLE (iBeacon) con tipo, valor y contador.  
- **Android (Java)** → Escaneo BLE, interpretación de tramas y envío de medidas al servidor.  
- **Servidor (PHP + SQLite)** → API REST que guarda y devuelve las medidas.  
- **Web (HTML + JS)** → Interfaz que muestra la última medida y se actualiza cada 5 s.  
- **Tests (Mocha + Request)** → Validación automática de la API REST.

---

## Tecnologías y Herramientas

- **Arduino IDE** – Emisor BLE  
- **Android Studio (Java)** – Receptor BLE y comunicación HTTP  
- **PHP + SQLite** – Backend REST y base de datos ligera  
- **JavaScript (Fetch API)** – Actualización dinámica del frontend  
- **Mocha + Request (Node.js)** – Framework para tests automáticos  
- **Plesk (UPV)** – Despliegue del servidor y la web  

---

## Despliegue

El proyecto está alojado en el panel **Plesk (UPV)**:  
- **API REST** → `https://nagufor.upv.edu.es/app.php`  
- **Web** → `https://nagufor.upv.edu.es/index.html`  
- **Base de datos** → SQLite (generada automáticamente en el servidor)

**Aplicación Android:**  
1. Abrir en Android Studio.  
2. Permitir Bluetooth y ubicación.  
3. Pulsar *“Buscar nuestro dispositivo”* para iniciar la lectura BLE.  

---

## Ejecución de Tests

Los tests automáticos se encuentran en la carpeta `test/`  
y validan la inserción y consulta de medidas desde la API REST.

### Pasos:
```bash
npm install   # Instalar dependencias
npm test      # Ejecutar suite de pruebas
Resultado esperado:
API de Medidas
  ✓ POST /medida inserta una medida válida
  ✓ GET /medida/ultima devuelve una medida
2 passing (500ms)