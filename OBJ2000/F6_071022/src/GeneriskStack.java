import java.util.ArrayList;
import java.util.Objects;

public class GeneriskStack<Type> {
    //Opprette er ArrayList

    private ArrayList<Type> stack = new ArrayList<>();

    //Metode for å returnere antall objekter i stacken
    public int getSize() {
        return stack.size();
    }

    //Metode som tester på om stacken er tom:
    public boolean isEmpty() {
        return stack.isEmpty();
    }


    //Metode for å sette inn et nytt objekt:
    public void push(Type objekt) {
        stack.add(objekt);
    }

    //Metode for å ta ut et objekt fra stacken:
    //Metoden skal også returnere objektet:
    public Type pop(){
        //Lager en huskereferanse til det siste objektet i stacken
        Type t = stack.get(stack.size()-1);

        //Fjerner objektet ved å bruke en ArrayList-metode Remove:
        stack.remove(stack.size()-1);

        //Returnerer siste elementet lager i variabel t
        return t;
    }

    //Metode for å returnere referanse til siste objektet i arrayet
    public Type peep() {
        return stack.get(stack.size()-1);
    }

    //Metode for å skrive ut hele stacken
    public Object[] getInnhold () {
        return stack.toArray();
    }
}
