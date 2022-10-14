import javax.swing.*;
import java.util.Formatter;

public class ValuttaKonvertør {
    public static void main(String[] args) {
        double usd = Double.parseDouble(JOptionPane.showInputDialog("USD: "));

        double kurs = 9.91;
        double nok = usd * kurs;

        Formatter f = new Formatter();

        f.format("%.2f",nok);

        JOptionPane.showMessageDialog(null,"NOK: "+f.toString());
    }
}
