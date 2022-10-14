import javax.swing.*;
import java.util.Formatter;

public class Oppgave3 {
    public static void main(String[] args) {
        //Leser radius for en sirkel:
        double radius = Double.parseDouble(JOptionPane.showInputDialog("Skriv inn radius"));
        double areal = Math.PI * radius * radius;
        //Formaterer arealet
        Formatter f = new Formatter();

        f.format("%.0f",areal);

        //Arealet av en sirkel er Pi*radius**2
        JOptionPane.showMessageDialog(null,"Arealet er: " + f.toString());
    }
}
