package main.java.days;

import processing.core.PApplet;

public class Day1 extends AbstractDay {

    public Day1(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    @Override
    public void puzzle1() {
        int sum = 0;
        String helper;
        for (String i : input) {
            helper = i.replaceAll("\\D+", "");

            // Breaks if there are no digits left
            sum += (Character.getNumericValue(helper.charAt(0))) * 10
                    + Character.getNumericValue(helper.charAt(helper.length() - 1));
        }
        System.out.println("Puzzle 1:");
        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        int sum = 0;
        String helper;
        for (String i : input) {
            helper = i.replaceAll("one", "o1e");
            helper = helper.replaceAll("two", "t2o");
            helper = helper.replaceAll("three", "t3e");
            helper = helper.replaceAll("four", "4");
            helper = helper.replaceAll("five", "5e");
            helper = helper.replaceAll("six", "6");
            helper = helper.replaceAll("seven", "n7");
            helper = helper.replaceAll("eight", "8t");
            helper = helper.replaceAll("nine", "9e");
            helper = helper.replaceAll("\\D+", "");
            sum += (Character.getNumericValue(helper.charAt(0))) * 10
                    + Character.getNumericValue(helper.charAt(helper.length() - 1));
        }
        System.out.println("Puzzle 2:");
        System.out.println(sum);
    }

}
