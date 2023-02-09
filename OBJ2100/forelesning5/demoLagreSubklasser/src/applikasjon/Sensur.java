package applikasjon;

public abstract class Sensur {
    public final int FORBEREDELSER = 3;
    private String fag;
    private String eksamenstype;

    public Sensur(String fag, String eksamenstype) {
        this.fag = fag;
        this.eksamenstype = eksamenstype;
    }

    public int getFORBEREDELSER() {
        return FORBEREDELSER;
    }

    public String getFag() {
        return fag;
    }

    public void setFag(String fag) {
        this.fag = fag;
    }

    public String getEksamenstype() {
        return eksamenstype;
    }

    public void setEksamenstype(String eksamenstype) {
        this.eksamenstype = eksamenstype;
    }

    //Definerer en abstrakt metode:
    public abstract double finnTimeforbruk();

    @Override
    public String toString() {
        return "Sensur{" +
                "FORBEREDELSER=" + FORBEREDELSER +
                ", fag='" + fag + '\'' +
                ", eksamenstype='" + eksamenstype + '\'' +
                '}';
    }

    public String toFile (){
        return fag + ";" + eksamenstype;
    }
}
