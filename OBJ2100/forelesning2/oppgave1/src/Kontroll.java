import java.util.ArrayList;

public class Kontroll implements Filtrering {

    private ArrayList<Integer> talliste = new ArrayList<>();

    public boolean filtrer(int tall, int deltall){
        if(tall%deltall==0){
            return true;
        }else return false;
    }

    //Metode for å fylle tallisten med ønskede tall:
    public void fyllListe(int maxtall){
        talliste.clear();
        for (int i = 1; i<maxtall+1;i++) {
            talliste.add(i);
        }
    }

    //Metode som bruker lambda-programmering:
    public void lambdaBruk(int maxtall, int deltall){
        fyllListe(maxtall);
        System.out.println("Med Lambda:");
        talliste.stream().filter(x->x%deltall == 0).forEach(x->System.out.println(x));
    }

    //Metode som bruker løkke i stedet for lambda-programmering:
    public void lokkeBruk(int maxtall, int deltall) {
        fyllListe(maxtall);
        //Lager en string for utskrift med JOptionPane
        String utstring = "";
        //Starter løkka:
        for(int i = 0; i<maxtall;i++){
            int tall = talliste.get(i);
            //Bruker medtoden fitrer(). Hvis delelig så legges tallet til utstringen:
            if(filtrer(tall, deltall)){
                utstring+=tall;
                utstring+="\n";
            }
        }
        System.out.println("Med løkke:");
        System.out.println(utstring);
    }
}
