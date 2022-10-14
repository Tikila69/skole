import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        String navn = JOptionPane.showInputDialog("Skriv inn navn nr. 1:");
        Person p1 = new Person(navn);
        navn = JOptionPane.showInputDialog("Skriv inn navn nr. 2");
        Person p2 = new Person(navn);


        System.out.println("Navn person nr. 1: "+p1.toString());
        System.out.println("Navn person nr. 2: "+p2.toString());
    }
}
