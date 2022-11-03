import javax.swing.*;
import java.util.ArrayList;

public class Grensesnitt {

    int hi = 0;

    int gi = 0;

    String kjønn;
    Double lengde;
    Double vekt;
    String dato;
    String sted;
    String harenr;
    String type;
    String farge;
    String gaupenr;
    Double øretuster;

    Kontroll kontroll = new Kontroll();
    Gaupe gaupe = new Gaupe(kjønn, lengde, vekt, dato, sted, gaupenr, øretuster);
    Hare hare = new Hare(kjønn, lengde, vekt, dato, sted, harenr, type, farge);


    private final String[] alternnativer = {
            "Registrer Hare",
            "Registrer Gaupe",
            "Registrer omfangst Hare",
            "Registrer omfangst Gaupe",
            "Haresøk",
            "Gaupesøk",
            "Vis alle dyr",
            "Avslutt"
    };

    public int lesValg() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Hva ønsker du å gjøre?",
                "Hare og Gauperegister",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                alternnativer,
                alternnativer[0]
        );
        return valg;
    }

    public void meny() {
        boolean fortsette = true;

        while (fortsette){
            int valg = lesValg();
            switch (valg){
                case 0: registrerNyHare();
                break;
                case 1: registrerNyGaupe();
                break;
                case 2: registrerOmfangstHare();
                break;
                case 3: registrerOmfangstGaupe();
                break;
                case 4: haresøk();
                break;
                case 5: gaupesøk();
                break;
                case 6: alleDyr();
                break;
                default: fortsette = false;
                break;
            }
        }
    }

    public void registrerNyHare() {
        int hareindex = hi+1;
        hi = hareindex;

        dato = JOptionPane.showInputDialog("Dato:");
        sted = JOptionPane.showInputDialog("Sted:");

        kjønn = JOptionPane.showInputDialog("Kjønn:");
        lengde = Double.parseDouble(JOptionPane.showInputDialog("Lengde:"));
        vekt = Double.parseDouble(JOptionPane.showInputDialog("Vekt:"));
        harenr ="H"+hareindex;
        type = JOptionPane.showInputDialog("Type:");
        farge = JOptionPane.showInputDialog("Farge:");


        hare = new Hare(kjønn, lengde, vekt, dato, sted, harenr, type, farge);
        kontroll.nyHare(hare);

        JOptionPane.showMessageDialog(null,"Hare registrert: "+ hare.toString());

    }

    public void registrerNyGaupe() {
        int gaupeindex = gi + 1;
        gi = gaupeindex;

        dato = JOptionPane.showInputDialog("Dato:");
        sted = JOptionPane.showInputDialog("Sted:");
        kjønn = JOptionPane.showInputDialog("Kjønn:");
        lengde = Double.parseDouble(JOptionPane.showInputDialog("Lengde:"));
        vekt = Double.parseDouble(JOptionPane.showInputDialog("Vekt:"));
        gaupenr ="G"+gaupeindex;
        øretuster = Double.parseDouble(JOptionPane.showInputDialog("Øretustlengde:"));

        gaupe = new Gaupe(kjønn, lengde, vekt, dato, sted, gaupenr, øretuster);
        kontroll.nyGaupe(gaupe);

        JOptionPane.showMessageDialog(null,"Gaupe registrert: "+gaupe.toString());
    }

    public void registrerOmfangstHare() {

        harenr =JOptionPane.showInputDialog("Hare ID:");
        dato = JOptionPane.showInputDialog("Dato:");
        sted = JOptionPane.showInputDialog("sted:");
        lengde = Double.parseDouble(JOptionPane.showInputDialog("Lengde:"));
        vekt = Double.parseDouble(JOptionPane.showInputDialog("Vekt:"));
        type = JOptionPane.showInputDialog("Type:");
        farge = JOptionPane.showInputDialog("Farge:");

        hare = new Hare(hare.getKjønn(harenr), lengde, vekt, dato, sted, harenr, type, farge);
        kontroll.gjenfangstHare(hare);

        JOptionPane.showMessageDialog(null,"Hare registrert: "+ hare.toString());
    }

    public void registrerOmfangstGaupe() {

        gaupenr =JOptionPane.showInputDialog("Gaupe ID");
        dato = JOptionPane.showInputDialog("Dato:");
        sted = JOptionPane.showInputDialog("sted:");
        lengde = Double.parseDouble(JOptionPane.showInputDialog("Lengde:"));
        vekt = Double.parseDouble(JOptionPane.showInputDialog("Vekt:"));
        øretuster = Double.parseDouble(JOptionPane.showInputDialog("Øretustlengde:"));

        gaupe = new Gaupe(gaupe.getKjønn(gaupenr), lengde, vekt, dato, sted, gaupenr, øretuster);
        kontroll.gjenfangstGaupe(gaupe);

        JOptionPane.showMessageDialog(null,"Gaupe registrert: "+gaupe.toString());
    }

    public void haresøk() {
        harenr = JOptionPane.showInputDialog("Hare ID;");
        JOptionPane.showMessageDialog(null,
                "Orginal registrering:\n" +
                        kontroll.getHare(harenr) +
                        "\nGjenfangst:\n"+
                        kontroll.getGjenfangstHareSortert(harenr));

    }
    public void gaupesøk(){
        gaupenr = JOptionPane.showInputDialog("Gaupe ID;");
        JOptionPane.showMessageDialog(null,
                "Orginal registrering:\n" +
                        kontroll.getGaupe(gaupenr) +
                        "\nGjenfangst:\n" +
                        kontroll.getGjenfangstGaupeSortert(gaupenr));

    }

    public void alleDyr(){
        ArrayList<Dyr> dyreliste = new ArrayList<>();
        dyreliste = kontroll.getAlleDyr();
        String utprint = "";

        for (int i = 0; i<dyreliste.size(); i++){
            utprint += (dyreliste.get(i) + "\n");
        }

        JOptionPane.showMessageDialog(null,utprint);
    }
}
