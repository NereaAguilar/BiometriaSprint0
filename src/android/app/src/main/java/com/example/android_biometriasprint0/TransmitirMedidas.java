package com.example.android_biometriasprint0;

//------------------------------------------------------------
//   Autor: Nerea Aguilar Forés
//   Descripción: Clase encargada de enviar las mediciones desde
//   la app Android hacia la API REST del servidor
//   Realiza peticiones HTTP POST con los datos en formato JSON
//------------------------------------------------------------

import android.util.Log;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

// -----------------------------------------------------------------------------------
// Clase encargada de enviar las mediciones a la API REST
// -----------------------------------------------------------------------------------
public class TransmitirMedidas {
    //private static final String API_URL = "http://10.0.2.2:8000/medida";

    //URL de la API REST, servidor en Plesk
    private static final String API_URL = "https://nagufor.upv.edu.es/app.php/medida";

    // -----------------------------------------------------------------------------------
    // Metodo: enviarMedida()
    // Envía una medida al servidor mediante POST en formato JSON
    // Parámetro: Medidas medida (tipo (int), medición (double))
    // Devuelve: true si la API responde con código 200, false en caso de error
    // -----------------------------------------------------------------------------------
    public static boolean enviarMedida(Medidas medida) {
        HttpURLConnection conn = null;
        try {
            URL url = new URL(API_URL);
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; utf-8");
            conn.setDoOutput(true);

            JSONObject json = new JSONObject();
            json.put("tipo", medida.getTipo());
            json.put("medicion", medida.getMedicion());

            // Enviar JSON al servidor
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = json.toString().getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            // Comprobar respuesta
            int code = conn.getResponseCode();
            BufferedReader br = new BufferedReader(new InputStreamReader(
                    code >= 400 ? conn.getErrorStream() : conn.getInputStream(), "utf-8"));
            StringBuilder sb = new StringBuilder();
            for (String line; (line = br.readLine()) != null; ) sb.append(line);
            Log.d("API", "HTTP " + code + " ← " + sb.toString());
            return (code == 200);


        } catch (Exception e) {
            e.printStackTrace();
            return false;
        } finally {
            if (conn != null) conn.disconnect();
        }
    }
}
