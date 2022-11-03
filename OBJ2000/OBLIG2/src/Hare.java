import java.util.Comparator;

public class Hare extends Dyr implements Comparable<Hare> {

    String harenr;
    String type;
    String farge;


    public Hare(String kjønn, Double lengde, Double vekt, String dato, String sted, String harenr, String type, String farge) {
        super(kjønn, lengde, vekt, dato, sted);
        this.harenr = harenr;
        this.type = type;
        this.farge = farge;
    }

    public String getHarenr() {
        return harenr;
    }

    @Override
    public String toString() {
        return "harenr: " + harenr +
                ", " + type +
                ", " + farge +
                ", " + kjønn +
                ", " + lengde +
                ", " + vekt +
                ", " + dato +
                ", " + sted;
    }

    public int compareTo(Hare hare) {
        return this.harenr.compareTo(hare.getHarenr());
    }


}