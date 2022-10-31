public class Gaupe extends Dyr {

    Double øretuster;

    public Gaupe(String kjønn, Double lengde, Double vekt, Double øretuster) {
        super(kjønn, lengde, vekt);
        this.øretuster = øretuster;
    }

    public Double getØretuster() {
        return øretuster;
    }

    public void setØretuster(Double øretuster) {
        this.øretuster = øretuster;
    }

    @Override
    public String toString() {
        return "Gaupe{" +
                "øretuster=" + øretuster +
                ", kjønn='" + kjønn + '\'' +
                ", lengde=" + lengde +
                ", vekt=" + vekt +
                '}';
    }
}
