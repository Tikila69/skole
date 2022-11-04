package com.example.demoradiobuttons;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.RadioButton;
import javafx.scene.control.Toggle;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    RadioButton button1, button2, button3;
    ToggleGroup toggleGroup;
    VBox sidePanel;
    @Override
    public void start(Stage stage) throws IOException {
        toggleGroup = new ToggleGroup();
        sidePanel = new VBox();
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 400, 400);

        button1 = new RadioButton("OBJ2000");
        button2 = new RadioButton("PRG1100");
        button3 = new RadioButton("APP2000");

        stage.setTitle("Hello!");
        stage.setScene(scene);

        button1.setSelected(true);

        button1.setToggleGroup(toggleGroup);
        button2.setToggleGroup(toggleGroup);
        button3.setToggleGroup(toggleGroup);

        sidePanel.getChildren().addAll(button1,button2,button3);
        root.setLeft(sidePanel);

        button1.setOnAction(e -> {if(button1.isSelected())System.out.println("OBJ1000");});
        button2.setOnAction(e -> {if(button2.isSelected())System.out.println("PRG1000");});
        button3.setOnAction(e -> {if(button3.isSelected())System.out.println("APP2000");});
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}