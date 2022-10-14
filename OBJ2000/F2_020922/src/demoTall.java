import javax.swing.*;
import java.util.Formatter;

public class demoTall {
    public static void main(String[] args) {
        String lestTall = JOptionPane.showInputDialog("Les inn ett tall:");
        int tall1 = Integer.parseInt(lestTall);
        lestTall = JOptionPane.showInputDialog("Les inn ett nytt tall:");
        int tall2= Integer.parseInt(lestTall);

        //Foretar en heltallsdivison:
        int svar = tall1/tall2;

        //Presenterer svaret:
        JOptionPane.showMessageDialog(null,tall1 + "/" + tall2 + "=" + svar + " ved heltallsdivisjon");

        //Utfører en vanlig division:
        double svar2 = (double)tall1/tall2;
        JOptionPane.showMessageDialog(null,"Vanlig divisjon: " + svar2);

        //Bruker modulus:
        int rest = tall1%tall2;
        JOptionPane.showMessageDialog(null,"Restdivision: " + rest);

        //Tester formatering i konsollet:
        System.out.printf("%.2f",svar2);

        //Formatert melding i meldingsboks
        //Oppretter Formater objektet
        Formatter f = new Formatter();

        //Formaterer desimaltallet:
        f.format("%.2f",svar2);
        JOptionPane.showMessageDialog(null,f.toString());



    }
}
