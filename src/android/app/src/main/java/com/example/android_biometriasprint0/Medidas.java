package com.example.android_biometriasprint0;

//------------------------------------------------------------
//  Autor: Nerea Aguilar Forés
//  Descripción: Clase modelo que representa una medida.
//------------------------------------------------------------

// Clase que representa las medidas enviadas al servidor
public class Medidas {

    // --------------------------------------------------------
    // Atributos
    // tipo -> Identificador del tipo de medida (Z)
    // medicion -> Valor numérico de la medida (R)
    // --------------------------------------------------------
    private int tipo;
    private double medicion;

    // --------------------------------------------------------
    // Constructor
    // Inicializa una nueva medida con su tipo y valor
    // --------------------------------------------------------
    public Medidas(int tipo, double medicion) {
        this.tipo = tipo;
        this.medicion = medicion;
    }

    // --------------------------------------------------------
    // Getters
    // --------------------------------------------------------
    public int getTipo(){return tipo;}

    public double getMedicion(){return medicion;}

}
