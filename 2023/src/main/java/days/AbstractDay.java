package main.java.days;

import processing.core.PApplet;

public abstract class AbstractDay {

    protected PApplet sketch;
    protected String[] input;

    public AbstractDay(PApplet sketch, String path, int day, boolean useExample) {
        this.sketch = sketch;

        if (useExample) {
            path += "example.txt";
        } else if (day < 1 || day > 26) {
            throw new IllegalArgumentException("Use a value of 1-26 for day");
        } else {
            path += "day" + day + ".txt";
            System.out.println(path);
        }

        this.input = sketch.loadStrings(path);
        System.out.println("Loaded input for day " + day);
    }

    public void puzzle1() {
    };

    public void puzzle2() {
    };

}
