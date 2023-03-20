package com.example.demorektangelliste;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    ListView liste;
    ArrayList<String> farger = new ArrayList<>();
    Rectangle rektangel;
    @Override
    public void start(Stage stage) throws IOException {

        BorderPane root = new BorderPane();
        VBox listepanel = new VBox();

        liste = new ListView();
        farger.add("Rød");
        farger.add("Blå");
        farger.add("Gul");
        ObservableList<String> innhold = FXCollections.observableArrayList();
        innhold.addAll(farger);
        liste.setItems(innhold);
        listepanel.getChildren().add(liste);
        //Vi trenger en knapp:
        Button knapp = new Button("Farge valgt");
        //Kobler knappen til en lytter:
        knapp.setOnAction(e-> behandleValg());
        //Opprette rektangelet:
        rektangel = new Rectangle();
        //Setter størrelse og farge:
        rektangel.setX(150.0f);
        rektangel.setY(75.0f);
        rektangel.setWidth(200.0f);
        rektangel.setHeight(100.0f);
        rektangel.setFill(Color.RED);
        root.setLeft(listepanel);
        root.setRight(rektangel);
        root.setBottom(knapp);
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Rektangelhelvette");
        stage.setScene(scene);
        stage.show();
    }

    public void behandleValg(){
        //Henter valget som en observableList
        ObservableList valg = liste.getSelectionModel().getSelectedIndices();
        //I dette programmet har vi singel valg. Valget ligger da på plsas 0 i valg.
        int index = (int)valg.get(0);
        //med dette får vi ut indeksen til valget i arraylisten (modellen).

        //Henter fargen fra modellen
        String valget = farger.get(index);
        if (valget=="Rød"){
            behandleRød();
        } else if (valget == "Blå") {
            behandleBlå();
        } else {
            behandleGul();
        }
    }

    public void behandleRød() {
        rektangel.setFill(Color.RED);
    }

    public void behandleBlå() {
        rektangel.setFill(Color.BLUE);
    }
    public void behandleGul() {
        rektangel.setFill(Color.YELLOW);
    }
    public static void main(String[] args) {
        launch();
    }
}