import javax.swing.*;

public class ArealAvRektangel {
    public static void main(String[] args) {
        double lengde = Double.parseDouble(JOptionPane.showInputDialog("Skriv inn lengden av rektangelet:"));
        double bredde = Double.parseDouble(JOptionPane.showInputDialog("Skriv inn bredden av rektangelet:"));

        double areal = lengde * bredde;

        JOptionPane.showMessageDialog(null,"Arealet av rektangelet er: "+areal);
    }
}
