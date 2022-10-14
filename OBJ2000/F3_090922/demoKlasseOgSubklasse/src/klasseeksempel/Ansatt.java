package klasseeksempel;

public class Ansatt extends Person {
    private int lønnstrinn;

    public int getLønnstrinn() {
        return lønnstrinn;
    }

    public void setLønnstrinn(int lønnstrinn) {
        this.lønnstrinn = lønnstrinn;
    }

    public Ansatt(String navn, String adresse, int fødselsår, int lønnstrinn) {
        super(navn, adresse, fødselsår);
        this.lønnstrinn = lønnstrinn;
    }

    @Override
    public String toString() {
        return super.toString() + "Ansatt{" +
                "lønnstrinn=" + lønnstrinn +
                '}';
    }
}
