package com.example.demodatabasekobling;

public class Kunde {
    int kundenr;
    String fornavn;
    String etternavn;
    String adresse;
    int postnr;
    String kjønn;

    public Kunde(int kundenr, String fornavn, String etternavn, String adresse, int postnr, String kjønn) {
        this.kundenr = kundenr;
        this.fornavn = fornavn;
        this.etternavn = etternavn;
        this.adresse = adresse;
        this.postnr = postnr;
        this.kjønn = kjønn;
    }

    public int getKundenr() {
        return kundenr;
    }

    public void setKundenr(int kundenr) {
        this.kundenr = kundenr;
    }

    public String getFornavn() {
        return fornavn;
    }

    public void setFornavn(String fornavn) {
        this.fornavn = fornavn;
    }

    public String getEtternavn() {
        return etternavn;
    }

    public void setEtternavn(String etternavn) {
        this.etternavn = etternavn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public int getPostnr() {
        return postnr;
    }

    public void setPostnr(int postnr) {
        this.postnr = postnr;
    }

    public String getKjønn() {
        return kjønn;
    }

    public void setKjønn(String kjønn) {
        this.kjønn = kjønn;
    }
}


