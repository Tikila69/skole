public class vare {
    String varenavn;
    int antall;
    double pris;

    public vare(String varenavn, int antall, double pris) {
        this.varenavn = varenavn;
        this.antall = antall;
        this.pris = pris;
    }
    public String toString() {return "Varenavn: " + varenavn + " antall på lager: " + antall + " pris: " + pris;}
}
