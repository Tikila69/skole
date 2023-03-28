module com.example.demorektangelliste {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demorektangelliste to javafx.fxml;
    exports com.example.demorektangelliste;
}