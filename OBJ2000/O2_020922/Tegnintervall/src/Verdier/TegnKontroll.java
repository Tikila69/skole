package Verdier;

public class TegnKontroll {
    public String lagVerdeir(char start, char slutt) {
        //Vi skal bygge opp en String skal skal returneres
        //Vi lager først en tom String:
        String uttekst = "";
        //Konverterer start og slutt
        int startverdi = start; //En char er egentlig en integer i java
        int sluttverdi = slutt;
        //Stare en løkke
        for (int i = startverdi;i<sluttverdi+1;i++) {
            uttekst+="Tegnet "+start+" har unicode verdien "+i+"\n";
            start++;
        } //Slutt løkke

        return uttekst;
    }

}
