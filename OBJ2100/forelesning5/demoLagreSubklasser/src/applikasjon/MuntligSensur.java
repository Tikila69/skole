package applikasjon;

public class MuntligSensur extends Sensur {
    double lengde;


    public MuntligSensur(String fag, String eksamenstype, double lengde) {
        super(fag, eksamenstype);
        this.lengde = lengde;
    }

    public double finnTimeforbruk() {
        return lengde + FORBEREDELSER;
    }

    @Override
    public String toString() {
        return "MuntligSensur{" +
                "lengde=" + lengde +
                ", FORBEREDELSER=" + FORBEREDELSER +
                '}';
    }

    public String toFile(){
        return "M;" + super.toFile() + ";" + lengde;
    }
}
