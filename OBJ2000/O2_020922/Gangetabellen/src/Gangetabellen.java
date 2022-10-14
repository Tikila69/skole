import javax.swing.*;

public class Gangetabellen {
    public static void main(String[] args) {
        int tall1 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn det første tallet:"));
        int tall2 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn det andre tallet:"));

        for (int teller1 = tall1;teller1<tall2+1;teller1++) {
            System.out.println(tall1+"-gangen:");
            for (int teller2 = 1;teller2<11;teller2++) {
                //System.out.println("teller2: "+teller2);
                int sum = tall1 * teller2;
                System.out.println(tall1+" x "+teller2+" = "+sum);
            }
            tall1++;
        }

    }
}
