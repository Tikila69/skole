package Stjerner;

import javax.swing.*;

public class Grensesnitt {
    Tengekontroll kontroll = new Tengekontroll();
    private final String[] ALTERNATIVER = {"Trekant","Pyramide","Avslutt"};


    public int lesValg() {
        //Denne metoden setter opp menyen, leser valget og returerer dette
        //Vi bruker JOptionPane - metoden ShowOptionDialog som returnrere en int:
        int valg = JOptionPane.showOptionDialog(
                null,
                "Gjør et valg:",
                "Tegneprogram",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIVER,
                ALTERNATIVER[0]
                );
        return valg; //Possisjonen i arrayet ALTERNATIVER
    }

    public void meny(){
        //Bruker en løkke styrt av en bolsk
        boolean fortsett= true;

        while (fortsett){
            //Setter opp menyen og leser valg
            int valg = lesValg();
            //Bruker en case-blokk for å behandle valget
            switch (valg){
                case 0:tegnTrekant();
                break;
                case 1:tegnPyramide();
                break;
                default:fortsett=false;
            }
        }
    }

    public void tegnTrekant(){
        //Ber bruker skrive antall linjer
        int antall = Integer.parseInt(JOptionPane.showInputDialog("Oppgi antall linjer:"));

        String tegning = kontroll.tegnTrekant(antall);

        JOptionPane.showMessageDialog(null,tegning);


    }

    public void tegnPyramide(){
        int antall = Integer.parseInt(JOptionPane.showInputDialog("Oppgi antall linjer:"));

        String tegning = kontroll.tegnPyramide(antall);
        JOptionPane.showMessageDialog(null,tegning);

    }
}
