import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Kontroll {

    private ArrayList<Hare> hareArrayList = new ArrayList<>();
    private ArrayList<Gaupe> gaupeArrayList = new ArrayList<>();
    private ArrayList<Hare> gjenfangstHareArrayList = new ArrayList<>();
    private ArrayList<Gaupe> gjenfangstGaupeArrayList = new ArrayList<>();


    public void nyHare(Hare hare) {
        hareArrayList.add(hare);
    }

    public void nyGaupe(Gaupe gaupe) {
        gaupeArrayList.add(gaupe);
    }

    public void gjenfangstHare(Hare hare) {
        gjenfangstHareArrayList.add(hare);
    }

    public void gjenfangstGaupe(Gaupe gaupe) {
        gjenfangstGaupeArrayList.add(gaupe);
    }

    public Hare getHare(String harenr) {
        Collections.sort(hareArrayList);
        Hare dummy = new Hare(null,null,null,null,null,harenr, null,null);
        int index = Collections.binarySearch(hareArrayList, dummy);
        if (index>-1) return hareArrayList.get(index);
        else return null;
    }

    public Gaupe getGaupe (String gaupenr) {
        Collections.sort(gaupeArrayList);
        Gaupe dummy = new Gaupe(null,null,null,null,null, gaupenr,null);
        int index = Collections.binarySearch(gaupeArrayList, dummy);
        if (index>-1) return gaupeArrayList.get(index);
        else return null;
    }

    public ArrayList<Gaupe> getGjenfangstGaupeSortert (String gaupenr) {
        ArrayList<Gaupe> filterGaupe = new ArrayList<>();

        List<Gaupe> filtrert = gjenfangstGaupeArrayList.stream().filter(gaupe -> gaupe.getGaupenr().equals(gaupenr)).collect(Collectors.toList());
        for (Gaupe gaupe : filtrert) {
            filterGaupe.add(gaupe);
        }
        return filterGaupe;
    }

    public ArrayList<Hare> getGjenfangstHareSortert (String harenr) {
        ArrayList<Hare> filtrertHare = new ArrayList<>();

        List<Hare> filtrert =  gjenfangstHareArrayList.stream().filter(hare -> hare.getHarenr().equals(harenr)).collect(Collectors.toList());
        for (Hare hare : filtrert) {
            filtrertHare.add(hare);
        }
        return filtrertHare;
    }

    public ArrayList <Dyr> getAlleDyr () {
        ArrayList<Dyr> filtrertAlleDyr = new ArrayList<>();


        for (int i = 0; i<gaupeArrayList.size();i++) {
            String gaupenr = "G"+(i+1);
            List<Gaupe> filtrertGaupe = gaupeArrayList.stream().filter(gaupe -> gaupe.getGaupenr().
                    equals(gaupenr)).collect(Collectors.toList());
            for (Gaupe gaupe1 : filtrertGaupe) {
                filtrertAlleDyr.add(gaupe1);
                List<Gaupe> filtrertGaupeGjenfangst = gjenfangstGaupeArrayList.stream().filter(gaupe -> gaupe.getGaupenr().
                        equals(gaupenr)).collect(Collectors.toList());
                for (Gaupe gaupe2 : filtrertGaupeGjenfangst) {
                    filtrertAlleDyr.add(gaupe2);
                }
             }
        }

        for (int i = 0; i<hareArrayList.size();i++) {
            String harenr = "H"+(i+1);
            List<Hare> filtrertHare = hareArrayList.stream().filter(hare -> hare.getHarenr().
                    equals(harenr)).collect(Collectors.toList());
            for (Hare hare1 : filtrertHare) {
                filtrertAlleDyr.add(hare1);
                List<Hare> filtrertHareGjenfangst = gjenfangstHareArrayList.stream().filter(hare -> hare.getHarenr().
                        equals(harenr)).collect(Collectors.toList());
                for (Hare hare2 : filtrertHareGjenfangst) {
                    filtrertAlleDyr.add(hare2);
                }
            }
            System.out.println("Alle dyr så langt: " + filtrertAlleDyr);
        }
        return filtrertAlleDyr;
    }
}