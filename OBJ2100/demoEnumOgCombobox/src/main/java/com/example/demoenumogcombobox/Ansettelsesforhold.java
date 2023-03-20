package com.example.demoenumogcombobox;

public enum Ansettelsesforhold {
    FAST, MIDLERTIDIG, PROSJEKT, SLUTTET;

    public String toString(){
        //VI tester på verdien:
        switch (this){
            case FAST -> {
                return "Fast Ansatt";
            }
            case SLUTTET -> {
                return "Sluttet";
            }
            case MIDLERTIDIG -> {
                return "Midlertidig Ansatt";
            }
            case PROSJEKT -> {
                return "Prosjektansatt";
            }
        }
        return null;
    }
}
