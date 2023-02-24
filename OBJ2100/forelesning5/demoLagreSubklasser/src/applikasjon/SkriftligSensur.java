package applikasjon;

public class SkriftligSensur extends Sensur{
    private double lengde;
    int antallBesvarelser;

    public SkriftligSensur(String fag, String eksamenstype, double lengde, int antallBesvarelser) {
        super(fag, eksamenstype);
        this.lengde = lengde;
        this.antallBesvarelser = antallBesvarelser;
    }

    public double getLengde() {
        return lengde;
    }

    public void setLengde(double lengde) {
        this.lengde = lengde;
    }

    public int getAntallBesvarelser() {
        return antallBesvarelser;
    }

    public void setAntallBesvarelser(int antallBesvarelser) {
        this.antallBesvarelser = antallBesvarelser;
    }

    @Override
    public double finnTimeforbruk() {

        double timessum=antallBesvarelser * (super.FORBEREDELSER+lengde) *0.15;
        if (antallBesvarelser>10){
            int rest = antallBesvarelser-10;
            double restsum = rest * (super.FORBEREDELSER+lengde) * 0.1;
            timessum = timessum + restsum;

        }
        return timessum;
    }

    @Override
    public String toString() {
        return "SkriftligSensur{" +
                "lengde=" + lengde +
                ", antallBesvarelser=" + antallBesvarelser +
                ", FORBEREDELSER=" + FORBEREDELSER +
                '}';
    }

    public String toFile(){
        return "S;" + super.toFile() + ";" + lengde + ";" + antallBesvarelser;
    }
}
