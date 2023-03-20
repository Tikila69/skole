module com.example.demoenumogcombobox {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoenumogcombobox to javafx.fxml;
    exports com.example.demoenumogcombobox;
}