package Sawkins.Diktgenerator;

import javax.swing.*;
import java.util.ArrayList;

public class Diktkontroll {

    public void registrerOrdEnkel(ArrayList<String> enkleOrd) {

        String nyttOrd = JOptionPane.showInputDialog("Registrer nytt ord:");

        if (nyttOrd!=null){
            enkleOrd.add(nyttOrd);
        }

        JOptionPane.showMessageDialog(null,"Ord: "+nyttOrd+" lagt til i ordlista.\n" +
                "Ordlista så langt: "+enkleOrd);
    }

    public String skrivEnkeltDikt(ArrayList<String> enkleOrd) {
        String enkeltDikt = "";

        for (int counter = 0; counter<4;counter++ )  {
            String linje = "";
            for (int n = 0; n < 4; n++) {
                int tilfeldigtall = (int) (Math.random() * enkleOrd.size());
                String nyttOrd = enkleOrd.get(tilfeldigtall);
                linje = linje + nyttOrd + " ";
            }
            enkeltDikt=enkeltDikt+linje+"\n";
        }
        return enkeltDikt;
    }

    public String skrivAvansertDikt(ArrayList<String> artikkel, ArrayList<String> adjektiv, ArrayList<String> substantiv, ArrayList<String> verb) {
        String avansertDikt = "";
        for (int counter1 = 0;counter1<3;counter1++){
            String linje = "";
            int tall1 = (int)(Math.random()*artikkel.size());
            int tall2 = (int)(Math.random()*adjektiv.size());
            int tall3 = (int)(Math.random()*substantiv.size());
            int tall4 = (int)(Math.random()*verb.size());
            String artikkelNy = artikkel.get(tall1);
            String adjektivNy = adjektiv.get(tall2);
            String substantivNy = substantiv.get(tall3);
            String verbNy = verb.get(tall4);
            linje+=artikkelNy+" "+adjektivNy+" "+substantivNy+" "+verbNy;
            avansertDikt+=linje+"\n";
            if (counter1==2){
                String sisteArtikkel = artikkel.get(tall1);
                String sisteAdjetiv = adjektiv.get(tall2);
                String sisteSubstantiv = substantiv.get(tall3);
                String sisteVerb = verb.get(tall4);
                avansertDikt+=sisteVerb+" "+sisteArtikkel+" "+sisteAdjetiv+" "+sisteSubstantiv+"?";
            }

        }
        return avansertDikt;
    }

    public void registrerArtikkel(ArrayList<String> artikkel) {
        String ord = JOptionPane.showInputDialog("Registrer ny artikkel:");
        if (ord!=null){
            artikkel.add(ord);
        }

        JOptionPane.showMessageDialog(null,"Ordet: "+ord+" er lagt til i ordlista \n" +
                "Ordlista til nå: "+artikkel);
    }

    public void registrerAdjektiv(ArrayList<String> adjektiv) {
        String ord = JOptionPane.showInputDialog("Registrer nytt adjektiv:");
        if (ord!=null){
            adjektiv.add(ord);
        }
        JOptionPane.showMessageDialog(null,"Ordet: "+ord+" er lagt til i ordlista \n" +
                "Ordlista til nå: "+adjektiv);

    }

    public void registrerSubstantiv(ArrayList<String> substantiv) {
        String ord = JOptionPane.showInputDialog("Registrer nytt substantiv:");
        if (ord!=null){
            substantiv.add(ord);
        }
        JOptionPane.showMessageDialog(null,"Ordet: "+ord+" er lagt til i ordlista \n" +
                "Ordlista til nå: "+substantiv);

    }

    public void registrerVerb(ArrayList<String> verb) {
        String ord = JOptionPane.showInputDialog("Registrer nytt verb:");
        if (ord!=null){
            verb.add(ord);
        }
        JOptionPane.showMessageDialog(null,"Ordet: "+ord+" er lagt til i ordlista \n" +
                "Ordlista til nå: "+verb);

    }
}