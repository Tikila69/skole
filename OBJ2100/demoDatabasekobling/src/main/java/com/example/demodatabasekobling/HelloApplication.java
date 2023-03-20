package com.example.demodatabasekobling;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.layout.Border;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    Kontroll kontroll  = new Kontroll();
    private TableView tabell = new TableView();
    private ObservableList<Kunde> data = FXCollections.observableArrayList();
    //tekstfelt for oppdatering:
    TextField nyttKnr, nyttFnavn, nyttEnavn, nyAdresse, nyttPostnr, nyttKjønn;
    @Override
    public void start(Stage stage) throws IOException {
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Databasehevette");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}