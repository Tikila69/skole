public class Hare extends Dyr{

    String type;
    String farge;

    public Hare(String kjønn, Double lengde, Double vekt, String type, String farge) {
        super(kjønn, lengde, vekt);
        this.type = type;
        this.farge = farge;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getFarge() {
        return farge;
    }

    public void setFarge(String farge) {
        this.farge = farge;
    }

    @Override
    public String toString() {
        return "Hare{" +
                "type='" + type + '\'' +
                ", farge='" + farge + '\'' +
                ", kjønn='" + kjønn + '\'' +
                ", lengde=" + lengde +
                ", vekt=" + vekt +
                '}';
    }
}
