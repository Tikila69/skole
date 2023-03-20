module com.example.demosceneskifte {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demosceneskifte to javafx.fxml;
    exports com.example.demosceneskifte;
}