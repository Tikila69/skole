import javax.swing.*;
import java.util.Formatter;

public class oppgave4 {
    public static void main(String[] args) {
        double kurs = 8.89;
        double usd = Double.parseDouble(JOptionPane.showInputDialog("USD:"));
        double nok = usd * kurs;

        Formatter f = new Formatter();

        f.format("%.2f",nok);

        JOptionPane.showMessageDialog(null,"NOK: " + f.toString());
    }
}
