public class Person {

    String navn;
    String adresse;

    public Person(String navn, String adresse) {
        this.navn = navn;
        this.adresse = adresse;
    }

    @Override
    public String toString() {
        return "Person{" +
                "Navn='" + navn + '\'' +
                ", Adresse='" + adresse + '\'' +
                '}';
    }
}
