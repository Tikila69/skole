package Verdier;

import javax.swing.*;

public class VerdiProgram {

    public static void main(String[] args) {
        //Oppretter et objekt for klassen TengKontorll
        TegnKontroll kontroll = new TegnKontroll();
        //Leser første tegn
        String lestTegn = JOptionPane.showInputDialog("Skriv første tegn:");
        //I en string ligger teskten som en String[]
        //Vi henter ut det første tegne i teksten:
        char start = lestTegn.charAt(0);
        //Leser neste tegn:
        lestTegn = JOptionPane.showInputDialog("Skriv siste tegn:");
        char slutt = lestTegn.charAt(0);
        //Kaller metoden lagVerdier i Tegnkontroll
        String uttekst = kontroll.lagVerdeir(start, slutt);

        JOptionPane.showMessageDialog(null,uttekst);
    }
}
