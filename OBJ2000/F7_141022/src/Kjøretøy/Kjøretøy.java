package Kjøretøy;

public class Kjøretøy implements Comparable<Kjøretøy> {
    private String regnr;//Tjener som identifikator
    private String produsent;
    private String modell;
    private int regår;

    public Kjøretøy(String regnr, String produsent, String modell, int regår) {
        super();
        this.regnr = regnr;
        this.produsent = produsent;
        this.modell = modell;
        this.regår = regår;
    }

    public Kjøretøy(String regnr) {

        this.regnr=regnr;
    }

    public String getRegnr() {

        return regnr;
    }

    public String getProdusent() {

        return produsent;
    }

    public String getModell() {

        return modell;
    }

    public int getRegår() {
        return regår;
    }

    public void setRegnr(String regnr) {
        this.regnr = regnr;
    }

    public void setProdusent(String produsent) {

        this.produsent = produsent;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public void setRegår(int regår) {

        this.regår = regår;
    }

    @Override
    public String toString() {
        return "Kjøretøy{" +
                "regnr='" + regnr + '\'' +
                ", produsent='" + produsent + '\'' +
                ", modell='" + modell + '\'' +
                ", regår='" + regår + '\'' +
                '}';
    }

    public int compareTo(Kjøretøy denandre) {

        return this.regnr.compareTo(denandre.getRegnr());
    }

    public boolean equals(Kjøretøy denandre) {

        return this.regnr.equals(denandre.getRegnr());
    }
}
