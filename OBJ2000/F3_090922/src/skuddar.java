import javax.swing.*;

public class skuddar {
    public static void main(String[] args) {
        int årstall = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn ett årstall:"));
        //Kaller metoden sjekkÅr:
        boolean erSkuddår = sjekkÅr(årstall);

        if (erSkuddår) JOptionPane.showMessageDialog(null,"Året " +årstall+" er et skuddår");
        else JOptionPane.showMessageDialog(null,"Året "+årstall+ " er ikke ett skuddår");
        }

    public static boolean sjekkÅr(int årstall) {

        boolean ok;
        ok=(årstall%4==0 && årstall%100!=0) || (årstall%400==0);
        return ok;
    }

}




