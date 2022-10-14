import javax.swing.*;

public class Terrsumerer {
    public static void main(String[] args) {
        int tall = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn ett heltall:"));

        int tall1 = tall%10;

        int tall2 = (tall - tall1)/10%10;

        int tall3 = (tall - tall1 - tall2)/100%10;

        int tall4 = (tall - tall1 - tall2 - tall3)/1000%10;

        int sum = tall1 + tall2 + tall3 + tall4;

        System.out.println("Tall1: "+tall4);
        System.out.println("Tall2: "+tall3);
        System.out.println("Tall3: "+tall2);
        System.out.println("Tall3: "+tall1);


        JOptionPane.showMessageDialog(null,"Tverrsummen av tallet er: "+sum);
    }
}
