module com.example.democombobocks {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.democombobocks to javafx.fxml;
    exports com.example.democombobocks;
}