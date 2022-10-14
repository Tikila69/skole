import javax.swing.*;

public class Datoprint {
    public static void main(String[] args) {
        int dag = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn dagens dato:"));
        int måned = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn dagens måned:"));
        int år = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn dagens år:"));

        JOptionPane.showMessageDialog(null,"Dagens dato er: "+dag+"."+måned+"."+år);
    }
}
