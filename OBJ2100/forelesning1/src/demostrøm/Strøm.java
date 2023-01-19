package demostrøm;

import java.util.ArrayList;

public class Strøm {
    public static void main(String[] args) {
        //Lager en ArrayList med heltall:
        ArrayList<Integer> samlling = new ArrayList<>();
        samlling.add(5);
        samlling.add(7);
        samlling.add(4);
        samlling.add(2);

        //Skriver ut:
        for(int i = 0; i<samlling.size();i++){
            System.out.println(samlling.get(i));
        }
        //Lage en strøm og bruker den til å sortere tallene:
        System.out.println("Sortert tallrekke:");
        samlling.stream().sorted().forEach(x ->System.out.println(x));

        //Sorterer på partall:
        System.out.println("Plukker ut partall");
        samlling.stream().filter(x ->x%2 == 0).forEach(x->System.out.println(x));
    }
}
