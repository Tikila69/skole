import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.TreeMap;

public class Kontroll {
    //private HashMap<Integer,Vare> vareliste = new HashMap<>();
    private TreeMap<Integer,Vare> vareliste = new TreeMap<>();

    public void nyVare (int varenr, Vare vare){
        vareliste.put(varenr,vare);
    }

    public Vare getVare(int varenr){
        return vareliste.get(varenr);
    }

    public void removeVare(int varenr){
        vareliste.remove(varenr);
    }

    public Iterator<Vare> getVarer() {
        Collection<Vare> innhold = vareliste.values();
        Iterator<Vare> oppramsing = innhold.iterator();
        return oppramsing;
    }

    public void endreBeholdning (int varenr, int beholdning){
        Vare vare  = getVare(varenr);

        if(vare!=null) vare.endreBeholdning(beholdning);
    }
}
