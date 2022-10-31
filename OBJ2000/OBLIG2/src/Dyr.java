public class Dyr {

    String kjønn;
    Double lengde;
    Double vekt;

    public Dyr(String kjønn, Double lengde, Double vekt) {
        super();
        this.kjønn = kjønn;
        this.lengde = lengde;
        this.vekt = vekt;
    }

    public String getKjønn() {
        return kjønn;
    }

    public void setKjønn(String kjønn) {
        this.kjønn = kjønn;
    }

    public Double getLengde() {
        return lengde;
    }

    public void setLengde(Double lengde) {
        this.lengde = lengde;
    }

    public Double getVekt() {
        return vekt;
    }

    public void setVekt(Double vekt) {
        this.vekt = vekt;
    }

    @Override
    public String toString() {
        return "Dyr{" +
                "kjønn='" + kjønn + '\'' +
                ", lengde=" + lengde +
                ", vekt=" + vekt +
                '}';
    }


}
