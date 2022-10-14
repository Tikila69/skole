package klasseeksempel;

public class Person {
    private String navn;
    private String adresse;
    private  int fødselsår;

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public int getFødselsår() {
        return fødselsår;
    }

    public void setFødselsår(int fødselsår) {
        this.fødselsår = fødselsår;
    }

    @Override //Egen versjon av toString(), som er definert i Object
    public String toString() {
        return "person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", fødselsår=" + fødselsår +
                '}';
    }

    public Person(String navn, String adresse, int fødselsår) {
        super();
        this.navn = navn;
        this.adresse = adresse;
        this.fødselsår = fødselsår;
    }
}

