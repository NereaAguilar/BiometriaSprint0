package com.example.android_biometriasprint0;

//------------------------------------------------------------
//     Nerea Aguilar Forés
//------------------------------------------------------------

import org.json.JSONObject;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

// Clase encargada de enviar las mediciones a la API REST
public class TransmitirMedidas {
    private static final String API_URL = "http://10.0.2.2:8000/medida";

    // Envía una medida al servidor con POST
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
            return (code == 200);

        } catch (Exception e) {
            e.printStackTrace();
            return false;
        } finally {
            if (conn != null) conn.disconnect();
        }
    }
}
