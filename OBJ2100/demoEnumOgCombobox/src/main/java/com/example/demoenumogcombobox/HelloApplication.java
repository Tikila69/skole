package com.example.demoenumogcombobox;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;

public class HelloApplication extends Application {
    ComboBox<String> status = new ComboBox<>();
    String[] innhold;
    @Override
    public void start(Stage stage) throws IOException {
        BorderPane root = new BorderPane();
        //Klargjør innholdet i comboboxen:
        Ansettelsesforhold[] ramse = Ansettelsesforhold.values();
        innhold = new String[ramse.length];
        for (int i = 0; i < ramse.length; i++) {
            innhold[i] = ramse[i].toString();
        }

        //Fyller comboboxen:
        status.getItems().addAll(innhold);
        status.setValue("Arbeidsforhold");
        status.setOnAction(e -> behandleValg());
        root.setCenter(status);
        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Enum og Combobox helvette!");
        stage.setScene(scene);
        stage.show();
    }

    public void behandleValg() {
        String valg = status.getValue();
        System.out.println("Du har valgt " + valg);
    }

    public static void main(String[] args) {
        launch();
    }
}