import javax.imageio.ImageTranscoder;
import javax.swing.*;

public class FinneMinste {
    public static void main(String[] args) {
        int tall1 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn det første tallet:"));
        int tall2 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn det andre tallet:"));
        int tall3 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn det tredje tallet:"));
        int tall4 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn det fjerde tallet:"));

        int minst= Math.min(Math.min(tall1,tall2),Math.min(tall3,tall4));

    JOptionPane.showMessageDialog(null,"Det misnte tallet er: "+minst);

    }
}
