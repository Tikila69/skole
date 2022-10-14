package Sawkins.Diktgenerator;

import javax.swing.*;
import java.util.ArrayList;


public class Grensesnitt {

    Diktkontroll kontroll = new Diktkontroll();
    LagLister lagLister = new LagLister();

    private final String[] ALTERNATIVERHOVED = {"Enkelt dikt","Avansert dikt","Avslutt"};
    private final String[] ALTERNATIVERENKELT = {"Registrer ord","Skriv dikt","Tilbake"};
    private final String[] ALTERNATIVERAVANSERT = {"Registrer ord","Skriv dikt","Tilbake"};
    private final String[] ORDTYPER = {"Artikkel","Adjektiv","Substantiv","Verb","Tilbake"};


    public int lesValgHoved() {

        int valg = JOptionPane.showOptionDialog(
                null,
                "Velg dikttype:",
                "Sawkins/Diktgenerator",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIVERHOVED,
                ALTERNATIVERHOVED[0]
        );
        return valg;
    }

    public int lesValgEnkelt (){
        int valg = JOptionPane.showOptionDialog(
                null,
                "Hva ønsker du å gjøre?",
                "Diktgenerator: Enkelt dikt",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIVERENKELT,
                ALTERNATIVERENKELT[0]
        );
        return valg;
    }

    public int lesValgAvansert () {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Hva ønsker du å gjøre?",
                "Diktgenerator: Avansert dikt",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                ALTERNATIVERAVANSERT,
                ALTERNATIVERAVANSERT[0]
        );
        return valg;
    }

    public int lesValgOrd () {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Hva slags ord ønsker du å registrere?",
                "Diktgenerator: Ordregistrering",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,ORDTYPER,
                ORDTYPER[0]);
        return valg;
    }

    public void hovedmeny (){
        lagLister.fyllLister();
        boolean fortsette = true;

        while (fortsette) {
            int valg = lesValgHoved();

            switch (valg) {
                case 0: enkelmeny();
                break;
                case 1: avansertmeny();
                break;
                default:fortsette=false;
            }
        }
    }

    public void enkelmeny (){

        boolean fortsette = true;

        while (fortsette) {
            int valg = lesValgEnkelt();

            switch (valg) {
                case 0:registrerEnkleOrd();
                    break;
                case 1:skrivEnkeltDikt();
                    break;
                default:fortsette=false;
            }
        }
    }

    public void avansertmeny (){

        boolean fortsette = true;

        while (fortsette) {
            int valg = lesValgAvansert();

            switch (valg) {
                case 0:ordmeny();
                    break;
                case 1:skrivAvansertDikt();
                    break;
                default:fortsette=false;
            }
        }
    }

    public void ordmeny() {
        boolean fortsette = true;
        while (fortsette){
            int valg = lesValgOrd();

            switch (valg) {
                case 0:registrerArtikkel();
                break;
                case 1:registrerAdjektiv();
                break;
                case 2:registrerSubstantiv();
                break;
                case 3:registrerVerb();
                break;
                default:fortsette=false;

            }
        }
    }
    public void skrivEnkeltDikt() {

        ArrayList<String> enkleOrd=lagLister.hentEnkelListe();

        String enkeltDikt = kontroll.skrivEnkeltDikt(enkleOrd);

        JOptionPane.showMessageDialog(null,enkeltDikt);
    }

    public void registrerEnkleOrd() {

        ArrayList<String> enkleOrd=lagLister.hentEnkelListe();

        kontroll.registrerOrdEnkel(enkleOrd);
    }


    public void skrivAvansertDikt() {

        ArrayList<String> artikkel = lagLister.getArtikkel();
        ArrayList<String> adjektiv = lagLister.getAdjektiv();
        ArrayList<String> substantiv = lagLister.getSubstantiv();
        ArrayList<String> verb = lagLister.getVerb();


        String avansertDikt = kontroll.skrivAvansertDikt(artikkel,adjektiv,substantiv,verb);

        JOptionPane.showMessageDialog(null,avansertDikt);

    }

    public void registrerArtikkel() {
        ArrayList<String> artikkel = lagLister.getArtikkel();
        kontroll.registrerArtikkel(artikkel);
    }

    public void registrerAdjektiv() {
        ArrayList<String> adjektiv = lagLister.getAdjektiv();
        kontroll.registrerAdjektiv(adjektiv);
    }

    public void registrerSubstantiv() {
        ArrayList<String> substantiv = lagLister.getSubstantiv();
        kontroll.registrerSubstantiv(substantiv);
    }

    public void registrerVerb() {
        ArrayList<String> verb = lagLister.getVerb();
        kontroll.registrerVerb(verb);
    }

}