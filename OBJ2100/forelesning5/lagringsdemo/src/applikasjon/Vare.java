package applikasjon;

import java.util.Objects;

public class Vare {
    private int varenr;
    private String varenavn;
    private int beholdning;

    public Vare(int varenr, String varenavn, int beholdning) {
        this.varenr = varenr;
        this.varenavn = varenavn;
        this.beholdning = beholdning;
    }

    public int getVarenr() {
        return varenr;
    }

    public String getVarenavn() {
        return varenavn;
    }

    public int getBeholdning() {
        return beholdning;
    }

    public void setBeholdning(int beholdning) {
        this.beholdning = beholdning;
    }

    @Override
    public String toString() {
        return "Vare{" +
                "varenr=" + varenr +
                ", varenavn='" + varenavn + '\'' +
                ", beholdning=" + beholdning +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Vare vare = (Vare) o;
        return varenr == vare.varenr;
    }

    @Override
    public int hashCode() {
        return Objects.hash(varenr);
    }

    public String toFile() {
        return varenr + ";" +varenavn+";"+beholdning;
    }


}
