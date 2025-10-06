package com.example.android_biometriasprint0;

import java.util.Random;
public class LogicaFake {
    private static final Random random = new Random();

    public static final int CO2 = 11;
    public static final int TEMPERATURA = 12;

    // Funcion para generar y devolver Medidas
    public static Medidas generar() {

        int tipo = random.nextBoolean() ? CO2 : TEMPERATURA;
        double valor;
        if (tipo == CO2) {
            valor = 400 + random.nextDouble() * 1800;
        } else {
            valor = 15 + random.nextDouble() * 10;
        }
        
        return new Medidas(tipo, valor);
    }
}
