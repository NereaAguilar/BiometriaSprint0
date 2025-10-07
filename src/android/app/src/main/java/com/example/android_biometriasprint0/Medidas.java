package com.example.android_biometriasprint0;

//------------------------------------------------------------
//     Nerea Aguilar Forés
//------------------------------------------------------------

// Clase que representa las medidas enviadas al servidor
public class Medidas {
    private int tipo;
    private double medicion;

    public Medidas(int tipo, double medicion) {
        this.tipo = tipo;
        this.medicion = medicion;
    }

    public int getTipo(){return tipo;}

    public double getMedicion(){return medicion;}

}
