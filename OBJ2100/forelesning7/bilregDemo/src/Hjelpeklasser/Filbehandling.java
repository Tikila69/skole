package Hjelpeklasser;

import java.io.*;

public class Filbehandling {
    //Metode for å lage en skriveforbindelse til en tekstfil:

    //Lager metodene som klassemetoder:
    public static PrintWriter lagSkriveforbindelse(String filnavn){
        try {
            FileWriter filforbindelse = new FileWriter(filnavn);
            BufferedWriter skrivebuffer = new BufferedWriter(filforbindelse);
            PrintWriter skriver = new PrintWriter(skrivebuffer);
            return skriver;
        }catch (Exception e) {
            return null;
        }
    }
    public static BufferedReader lagLeseforbindelse (String filnavn){
        try {
            FileReader filforbindelse = new FileReader(filnavn);
            BufferedReader leser = new BufferedReader(filforbindelse);
            return leser;
        } catch (Exception e){
            return null;
        }
    }

    public static ObjectOutputStream lagSkriveforbindelseBin (String filnavn) {
        try {
            FileOutputStream utstrøm  = new FileOutputStream(filnavn);
            ObjectOutputStream ut = new ObjectOutputStream(utstrøm);
            return ut;
        }
        catch (IOException e){
            return null;
        }
    }

    public static ObjectInputStream lagLeseforbindelseBin(String filnavn){
        try {
            FileInputStream innstrøm = new FileInputStream(filnavn);
            ObjectInputStream inn = new ObjectInputStream(innstrøm);
            return inn;
        }
        catch (IOException e){
            return null;
        }
    }
}
