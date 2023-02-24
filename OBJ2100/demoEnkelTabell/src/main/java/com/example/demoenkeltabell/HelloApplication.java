package com.example.demoenkeltabell;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.ListView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    private TableView tabell = new TableView();
    //Lager et objekt av klassen ObservableList:
    private ArrayList<Person> personer = new ArrayList<>();
    private ObservableList<Person> data = FXCollections.observableArrayList(personer);

    @Override
    public void start(Stage stage) throws IOException {
        personer.add(new Person("Didrik","Benterudstranda 4","95767711"));
        personer.add(new Person("Robin","Madafakka 420","42069420"));
        System.out.println(data);
        System.out.println(personer);
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 400, 400);
        stage.setTitle("Enkel tabell demo");

        //Oppretter tabellkolonner:
        TableColumn colNavn = new TableColumn("Navn");
        colNavn.setMinWidth(100);
        //Vi trenger et objekt som henter ut navnene fra personene:
        colNavn.setCellFactory(new PropertyValueFactory<Person,String>("navn"));


        TableColumn colAdressse = new TableColumn("Adresse:");
        colAdressse.setMinWidth(100);
        colAdressse.setCellFactory(new PropertyValueFactory<Person,String>("adresse"));


        TableColumn colTelefon = new TableColumn("Telefonnr:");
        colTelefon.setMinWidth(100);
        colTelefon.setCellFactory(new PropertyValueFactory<Person,String>("telefon"));

        //Legger til kolonnene i tabelle:
        tabell.getColumns().addAll(colNavn,colAdressse,colTelefon);

        //Legger til personene i Observablelist'en
        tabell.setItems(data);

        root.setCenter(tabell);
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}