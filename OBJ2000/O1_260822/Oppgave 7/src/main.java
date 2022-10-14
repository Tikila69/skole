import javax.swing.*;

public class main {
    public static void main(String[] args) {
        String navn = JOptionPane.showInputDialog("Hva er navnet ditt?");

        Person p1 = new Person(navn);

        JOptionPane.showMessageDialog(null,p1.toString());



    }
}
