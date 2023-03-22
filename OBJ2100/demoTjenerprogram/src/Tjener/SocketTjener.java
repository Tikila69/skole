package Tjener;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class SocketTjener {

    public static void main(String[] args) {
        //Definerer et portnr:
        final int PORTNR = 1250;
        try {
            //oppretter et objekt for tjener:
            ServerSocket tjener = new ServerSocket(PORTNR);
            System.out.println("Jarvis: Nå venter vi....");

            //Oppretter en forbindelse:
            Socket forbindelse = tjener.accept();

            //Åpner en strøm for kommunikasjon:
            InputStreamReader leseforbindelse = new InputStreamReader(forbindelse.getInputStream());
            BufferedReader leser = new BufferedReader(leseforbindelse);
            PrintWriter skriver = new PrintWriter(forbindelse.getOutputStream(),true);
            skriver.println("Jarvis: Hei! Du har nå kontakt med meg");
            skriver.println("Jarvis: Skriv hva du vil, så skal jeg gjenta det.");

            //leser input fra klienten:
            String linje = leser.readLine();

            //Starter en løkke som gjentar det hele:
            while (linje != null){
                skriver.println("Jarvis: Du skrev " + linje);
                linje = leser.readLine();
            }

            leser.close();
            skriver.close();
            forbindelse.close();

        }catch(Exception e){}
    }

}
