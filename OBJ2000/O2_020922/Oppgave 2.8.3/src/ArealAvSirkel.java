import javax.swing.*;
import java.util.Formatter;

public class ArealAvSirkel {
    public static void main(String[] args) {
        double radius = Double.parseDouble(JOptionPane.showInputDialog("Skriv inn radius av sirkelen:"));

        double areal = (radius * radius) * Math.PI;

        Formatter f = new Formatter();
        f.format("%.0f",areal);

        JOptionPane.showMessageDialog(null,"Arealet av sirkelen rundet opp til nærmeste heltall er: "+f.toString());
    }
}
