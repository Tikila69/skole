module com.example.demoradiobuttons {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoradiobuttons to javafx.fxml;
    exports com.example.demoradiobuttons;
}