import java.util.ArrayList;

public class Student extends Person {
    private String studieprogram;
    private ArrayList<Kurs> kursdeltagelse = new ArrayList<>();

    public Student(long personnummer, String navn, String adresse, String studieprogram, ArrayList<Kurs> kursdeltagelse) {
        super(personnummer, navn, adresse);
        this.studieprogram = studieprogram;
        this.kursdeltagelse = kursdeltagelse;
    }

    @Override
    public String toString() {
        return super.toString()+"Student{" +
                "studieprogram='" + studieprogram + '\'' +
                ", kursdeltagelse=" + kursdeltagelse +
                '}';
    }

    public void nyttKurs(Kurs kurset) {
        kursdeltagelse.add(kurset);
    }

    public ArrayList<Kurs> getKursdeltagelse(){
        return kursdeltagelse;
    }

}
