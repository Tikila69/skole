package com.example.demosingleton;

public class Utvalg {
    String etternavn;
    String ordredato;
    String betegnelse;
    String antall;

    public Utvalg(String etternavn, String ordredato, String betegnelse, String antall) {
        this.etternavn = etternavn;
        this.ordredato = ordredato;
        this.betegnelse = betegnelse;
        this.antall = antall;
    }

    public String getEtternavn() {
        return etternavn;
    }

    public String getOrdredato() {
        return ordredato;
    }

    public String getBetegnelse() {
        return betegnelse;
    }

    public String getAntall() {
        return antall;
    }
}
