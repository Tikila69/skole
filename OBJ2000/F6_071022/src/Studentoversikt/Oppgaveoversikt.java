package Studentoversikt;

import java.lang.reflect.Array;
import java.security.KeyStore;
import java.util.Arrays;

public class Oppgaveoversikt {
    //Denne skal holde rede på studentene
    //Hver student holder rede på eegne godkjente oppgaver

    private Student[] studenter = new Student[2];
    private int antallStudenter = 0;


    //Metode for å sette inn en ny student:
    public boolean nyStudent (Student student) {
        //Tester om det er plass til et nytt objekt

        if (antallStudenter<studenter.length) {
            studenter[antallStudenter] = student;
            antallStudenter++;
            return true;
        }
        else return false;
    }

    public void sorter () {
        //Bruker hjelpeklassen Arrays;
        Arrays.sort(studenter);
    }

    public Student finnStudent(String søkenavn) {
        String navn;

        for (int i=0;i<antallStudenter;i++){
            navn=studenter[i].getNavn();
            if(søkenavn.equals(navn)) return studenter[i];
        }
        return null;
    }
}
