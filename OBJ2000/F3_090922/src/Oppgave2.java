import javax.swing.*;

public class Oppgave2 {
    public static void main(String[] args) {
        //Leser lengde:
        String lengde = JOptionPane.showInputDialog("Skriv lengden:");

        //Konverterer til Double
        double lengdeDouble = Double.parseDouble(lengde);

        //Leser inn bredde på en bedre/mer kompakt måte:
        double bredde = Double.parseDouble(JOptionPane.showInputDialog("Skriv Bredde"));

        //Matte as...
        JOptionPane.showMessageDialog(null,"Areal: "+lengdeDouble*bredde);
    }
}
