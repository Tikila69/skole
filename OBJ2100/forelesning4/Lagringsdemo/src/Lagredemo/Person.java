package Lagredemo;

import java.util.Objects;

public class Person {
    private String navn;
    private String etternavn;
    private int fødselsår;

    public Person(String navn, String etternavn, int fødselsår) {
        this.navn = navn;
        this.etternavn = etternavn;
        this.fødselsår = fødselsår;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getEtternavn() {
        return etternavn;
    }

    public void setEtternavn(String etternavn) {
        this.etternavn = etternavn;
    }

    public int getFødselsår() {
        return fødselsår;
    }

    public void setFødselsår(int fødselsår) {
        this.fødselsår = fødselsår;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return Objects.equals(navn, person.navn);
    }

    @Override
    public int hashCode() {
        return Objects.hash(navn);
    }

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", etternavn='" + etternavn + '\'' +
                ", fødselsår=" + fødselsår +
                '}';
    }

    public String toFile(){
        return navn+","+etternavn+","+fødselsår;
    }
}
