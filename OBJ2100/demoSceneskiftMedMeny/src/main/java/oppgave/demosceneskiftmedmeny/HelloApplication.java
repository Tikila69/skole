package oppgave.demosceneskiftmedmeny;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;


public class HelloApplication extends Application {

    MenuBar menylinje = new MenuBar();
    Menu fargemeny = new Menu("Fargevalg");
    MenuItem rød = new MenuItem("rød");
    MenuItem gul = new MenuItem("gul");
    MenuItem blå = new MenuItem("blå");

    Stage primærscene;


    @Override
    public void start(Stage stage) throws IOException {
        BorderPane root = new BorderPane();
        primærscene = stage;
        //Lager menyen
        fargemeny.getItems().addAll(rød,gul,blå);
        //Legger fargemenyen til menylinjen:
        menylinje.getMenus().addAll(fargemeny);
        root.setTop(menylinje);
        rød.setOnAction(e -> behandleRød());
        gul.setOnAction(e -> behandleGul());
        blå.setOnAction(e -> behandleblå());
        Scene scene = new Scene(root, 400, 400);
        stage.setTitle("Fargehelvette");
        stage.setScene(scene);
        stage.show();
    }

    public void behandleRød() {
        BorderPane rødP = new BorderPane();
        Scene sceneRød = new Scene(rødP,400,400);
        rødP.setTop(menylinje);
        rødP.setBackground(new Background(new BackgroundFill(Color.RED,new CornerRadii(0),Insets.EMPTY)));
        primærscene.setScene(sceneRød);
    }

    public void behandleGul() {
        BorderPane gulP = new BorderPane();
        Scene sceneGul = new Scene(gulP,400,400);
        gulP.setTop(menylinje);
        gulP.setBackground(new Background(new BackgroundFill(Color.YELLOW,new CornerRadii(0),Insets.EMPTY)));
        primærscene.setScene(sceneGul);
    }

    public void behandleblå() {
        BorderPane blåP = new BorderPane();
        Scene sceneBlå = new Scene(blåP,400,400);
        blåP.setTop(menylinje);
        blåP.setBackground(new Background(new BackgroundFill(Color.BLUE,new CornerRadii(0),Insets.EMPTY)));
        primærscene.setScene(sceneBlå);
    }

    public static void main(String[] args) {
        launch();
    }
}