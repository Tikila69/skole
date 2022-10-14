import javax.swing.*;
import java.lang.reflect.Array;

public class menyProgram {


    //Definere knappene i menyen:
    private static final String[] ALTERNATIVER = {"Gjør ditt", "Gjør datt", "Avslutt"};


    public static void main(String[] args) {
        start();
    }
    //Metode for å lage meny og returnere menyvalget:
    public static int lesValg() {
        //Lager menyen og leser valget
        int valg = JOptionPane.showOptionDialog(
                null, //Vi gjøre ikke noe med denne
                "Velg hva som skal gjøres",//Ledetekst
                null, //Gjør ie+kke noe med denne
                JOptionPane.DEFAULT_OPTION, //Bruker default
                JOptionPane.PLAIN_MESSAGE, //Bruker default
                null, //Bryr oss ikke med denne
                ALTERNATIVER, //Listen med menyvalg
                ALTERNATIVER[0]); //Default menyvalg
        return valg;
    }


    //Metode for å lese menyvalg helt til vi velger avslutt
    public static void start() {
        //Definere en boolean for å kontrollere løkke
        boolean fortsett = true;
        while (fortsett) {
            //Kaller menyvalgmetoden
            int valg = lesValg();
            //Bruker en case-blokk til å bestemme handling
            switch (valg) {
                case 0 : System.out.println("Du valgte å gjøre ditt");
                break;
                case 1 : System.out.println("Du valgte å gjøre datt");
                break;
                default : fortsett=false;
            }
        }
    }
}

