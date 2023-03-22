package Klient;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class SocketKlient {
    public static void main(String[] args) {
        //definerer portnummeret:
        final int PORTNR = 1250;

        //Bruker scanner for å lese fra tastaturet:
        Scanner leser = new Scanner(System.in);
        System.out.println("Oppgi navnet på tjeneren:");
        String tjenermaskin = leser.nextLine();

        //Setter opp forbindelse:
        try {
            Socket forbindelse = new Socket(tjenermaskin,PORTNR);
            System.out.println("Jarvis: Forbindelsen er opprettet, sir");

            //Åpner leserforbindelse:
            InputStreamReader leserforbindelse = new InputStreamReader(forbindelse.getInputStream());
            BufferedReader leseren = new BufferedReader(leserforbindelse);

            //Åpner skriveforbindelse:
            PrintWriter skriveren = new PrintWriter(forbindelse.getOutputStream(),true);

            //Leser fra tjener og skriver til konsollet:
            String inn1 = leseren.readLine();
            String inn2 = leseren.readLine();

            //Skriver ut som en kontroll:
            System.out.println(inn1 + "\n" + inn2);
            String enlinje = leser.nextLine();

            while (!enlinje.equals("")){
                //Sender enlinje til tjener:
                skriveren.println(enlinje);

                //leser responsen fra tjeneren:
                String respons = leseren.readLine();

                //Skriver ut:
                System.out.println("Jarvis: " + respons);
                enlinje = leser.nextLine();
            }

            leseren.close();
            leser.close();
            skriveren.close();

        }catch (Exception e){

        }

    }
}
