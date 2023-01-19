import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Integer> samling = new ArrayList<>();
        samling.add(5);
        samling.add(7);
        samling.add(4);

        System.out.println("Skriver ut alle tall:");
        for (int i = 0; i<samling.size();i++){
            System.out.println(samling.get(i));
        }
        //Skriver ut alle partall
        System.out.println();
        System.out.println("Skriver ut partall:");
        samling.stream().filter(x -> x%2==0).forEach(x->System.out.println(x));

        //Skriver ut alle oddetall
        System.out.println();
        System.out.println("Skriver ut oddetall:");
        samling.stream().filter(x->x%2!=0).forEach(x->System.out.println(x));


    }
}