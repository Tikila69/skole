import javax.swing.*;

public class main {
    public static void main(String[] args) {
        String navn = JOptionPane.showInputDialog("Hva er navnet ditt?");
        String adresse = JOptionPane.showInputDialog("Hva er adressen din?");

        Person p1 = new Person(navn,adresse);

        JOptionPane.showMessageDialog(null,p1.toString());



    }
}
