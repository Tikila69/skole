public class Main {
    public static void main(String[] args) {
        Tallskriver tallskriver1 = new Tallskriver(1);
        Tallskriver tallskriver2 = new Tallskriver(2);
        Tallskriver tallskriver3 = new Tallskriver(3);
        Tallskriver tallskriver4 = new Tallskriver(4);
        Tallskriver tallskriver5 = new Tallskriver(5);

        tallskriver1.start();
        tallskriver2.start();
        tallskriver3.start();
        tallskriver4.start();
        tallskriver5.start();
    }
}