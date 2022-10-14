import javax.swing.*;

public class PlussingAvHeltall {
    public static void main(String[] args) {
        int tall1 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn ett heltall:"));
        int tall2 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn ett nytt heltall:"));

        int sum = tall1 + tall2;

        JOptionPane.showMessageDialog(null,"Summen av de to tallene er "+sum);

    }
}
