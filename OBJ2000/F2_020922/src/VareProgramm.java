import javax.swing.*;

public class VareProgramm {
    public static void main(String[] args) {
        //Bruker JOptionPane for å lese inn verdier
        String varenavn = JOptionPane.showInputDialog("Varenavn:");
        String lestAntall = JOptionPane.showInputDialog("Antall på lager:");

        //Vi konverterertil heltall
        int antall = Integer.parseInt(lestAntall);

        //Leser inn pris
        String lestPris = JOptionPane.showInputDialog("Skriv pris:");
        double pris = Double.parseDouble(lestPris);

        //Oppretter et vareobject
        vare vare = new vare(varenavn,antall,pris);
        JOptionPane.showMessageDialog(null, vare.toString());
    }
}
