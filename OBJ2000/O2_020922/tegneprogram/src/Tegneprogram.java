import javax.swing.*;

public class Tegneprogram {

    public static void main(String[] args) {
        int antall = Integer.parseInt(JOptionPane.showInputDialog("Hvor mange linjer vil du ha?"));

        for (int i=0;i<antall+1;i++) {
            String tegning = new String(new char[i]).replace("\0","*");
            System.out.println(tegning);
        }
    }
}
