import java.util.Objects;

public class Person {

    private String navn;
    private String adresse;

    public Person(String navn, String adresse) {
        this.navn = navn;
        this.adresse = adresse;
    }


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

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                '}';
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return Objects.equals(navn, person.navn) && Objects.equals(adresse, person.adresse);
    }

    @Override
    public int hashCode() {
        return Objects.hash(navn, adresse);
    }
}
