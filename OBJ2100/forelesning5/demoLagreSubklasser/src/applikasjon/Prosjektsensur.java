package applikasjon;

import javax.naming.CannotProceedException;

public class Prosjektsensur extends Sensur{

    private int antallBesvarelser;
    public final double PROSJEKTSENSUR = 8;

    //Implementerer metoden finnTimeforbruk
    @Override
    public double finnTimeforbruk() {
        return antallBesvarelser*PROSJEKTSENSUR;
    }

    public Prosjektsensur(String fag, String eksamenstype, int antallBesvarelser) {
        super(fag, eksamenstype);
        this.antallBesvarelser = antallBesvarelser;
    }

    @Override
    public String toString() {
        return "Prosjektsensur{" +
                "antallBesvarelser=" + antallBesvarelser +
                ", PROSJEKTSENSUR=" + PROSJEKTSENSUR +
                ", FORBEREDELSER=" + FORBEREDELSER +
                '}';
    }

    //toFile skal legge til et attributt som identifiserer klassen:
    public String toFile(){
        return "P;" + super.toFile() + ";" + antallBesvarelser;
    }
}
