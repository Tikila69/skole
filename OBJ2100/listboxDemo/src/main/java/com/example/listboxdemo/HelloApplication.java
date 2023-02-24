package com.example.listboxdemo;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableArray;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    //Definerer en listeboks
    private ListView liste;

    //Lager modell-delen her som en ArrayList med String:
    private ArrayList<String> ukedager = new ArrayList<>();
    @Override
    public void start(Stage stage) throws IOException {
        //Lager listeboksen
        liste = new ListView<>();
        //Legger inn ukedagene i arraylisten
        ukedager.add("Mandag");
        ukedager.add("Tirsdag");
        ukedager.add("Onsdag");
        ukedager.add("Torsdag");
        ukedager.add("Fredag");
        ukedager.add("Lørdag");
        ukedager.add("Søndag");
        //Lager kontrollobjektet
        ObservableList<String> innhold = FXCollections.observableArrayList();
        //Legger Arraylisten med ukedagene inn i kontrollobjektet:
        innhold.addAll(ukedager);
        //Knytter kontrollobjektet til listeboksen:
        liste.setItems(innhold);
        Button knapp = new Button("Les valg");
        //Knytter knappen til lytteren:
        knapp.setOnAction(e -> behandleValg());

        BorderPane root= new BorderPane();
        Scene scene = new Scene(root, 400, 400);
        stage.setTitle("Demo av listeboks");
        stage.setScene(scene);
        stage.show();

        root.setCenter(liste);
        root.setBottom(knapp);
    }

    //Lytter for knappen:
    public void behandleValg(){
        //Vi skal hente ut det som er valgt i listeboksen:
        //Dette skjer i form av en ObservableList.
        ObservableList valgteElementer = liste.getSelectionModel().getSelectedIndices();
        //Siden vi har Single Selection, er det bare ett onjekt i valgteElementer.
        //Dette vil ha index 0.
        int index = (int)valgteElementer.get(0);
        //Vi bruker indeksen til å hente ut ukedagen fra den opprinnelige Arraylisten
        System.out.println(ukedager.get(index));
    }

    public static void main(String[] args) {
        launch();
    }
}