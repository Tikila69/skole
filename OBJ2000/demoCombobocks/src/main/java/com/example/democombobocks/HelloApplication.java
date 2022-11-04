package com.example.democombobocks;

import javafx.application.Application;
import javafx.beans.property.SimpleObjectProperty;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    ComboBox<String> comboBox;
    String[] comboboxInnhold = {"Mandag","Tirsdag","Onsdag","Torsdag","Fredag","Lørdag","Søndag"};
    @Override
    public void start(Stage stage) throws IOException {


        comboBox = new ComboBox<String>();
        comboBox.getItems().addAll(comboboxInnhold);
        comboBox.setValue("Ukedag");

        comboBox.setOnAction(e-> behandleValg());

        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 400, 400);
        root.setCenter(comboBox);
        stage.setTitle("Combobox!");
        stage.setScene(scene);
        stage.show();
    }

    public void behandleValg() {
        //Skal lese hvilken dag som ble klikket på

        String valg = comboBox.getValue();
        System.out.println(valg);
    }

    public static void main(String[] args) {
        launch();
    }
}