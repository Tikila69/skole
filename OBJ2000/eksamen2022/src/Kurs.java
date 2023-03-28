public class Kurs implements Comparable<Kurs>{
    private String kursid;
    private String kursnavn;

    public Kurs(String kursid, String kursnavn) {
        this.kursid = kursid;
        this.kursnavn = kursnavn;
    }

    @Override
    public int compareTo(Kurs kurs) {
        return 0;
    }
}
