public class Gaupe extends Dyr implements Comparable<Gaupe> {

    String gaupenr;
    Double øretuster;

    public Gaupe(String kjønn, Double lengde, Double vekt, String dato, String sted, String gaupenr, Double øretuster) {
        super(kjønn, lengde, vekt, dato, sted);
        this.gaupenr = gaupenr;
        this.øretuster = øretuster;
    }

    public String getGaupenr() {
        return gaupenr;
    }


    @Override
    public String toString() {
        return "gaupenr: " + gaupenr +
                ", " + øretuster +
                ", " + kjønn +
                ", " + lengde +
                ", " + vekt +
                ", " + dato +
                ", " + sted;
    }

    public int compareTo(Gaupe gaupe) {
        return this.gaupenr.compareTo(gaupe.getGaupenr());
    }


}
