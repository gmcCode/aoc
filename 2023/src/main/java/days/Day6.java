package main.java.days;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import processing.core.PApplet;

public class Day6 extends AbstractDay {

    public Day6(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");

        Pattern p = Pattern.compile("\\d+");

        // parse times
        Matcher timeMatcher = p.matcher(input[0]);
        List<Integer> times = new ArrayList<>();
        while (timeMatcher.find()) {
            times.add(Integer.parseInt(timeMatcher.group()));
        }

        // parse distances
        Matcher distanceMatcher = p.matcher(input[1]);
        List<Integer> distances = new ArrayList<>();
        while (distanceMatcher.find()) {
            distances.add(Integer.parseInt(distanceMatcher.group()) + 1);
        }

        ArrayList<Integer> results = new ArrayList<>();

        for (int i = 0; i < times.size(); i++) {
            double time = times.get(i).doubleValue();
            double dist = distances.get(i).doubleValue();
            double t = (time / 2.0) + Math.sqrt(Math.pow(time / 2.0, 2.0) - dist);

            int t_int = (int) Math.floor(t);
            int result = t_int - ((int) time - t_int) + 1;
            results.add(result);
        }

        System.out.println(results.stream().reduce(1, (a, b) -> a * b));
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        Pattern p = Pattern.compile("\\d+");

        // parse times
        Matcher timeMatcher = p.matcher(input[0].replace(" ", ""));
        List<Integer> times = new ArrayList<>();
        while (timeMatcher.find()) {
            times.add(Integer.parseInt(timeMatcher.group()));
        }

        // parse distances
        Matcher distanceMatcher = p.matcher(input[1].replace(" ", ""));
        List<Long> distances = new ArrayList<>();
        while (distanceMatcher.find()) {
            distances.add(Long.parseLong(distanceMatcher.group()) + 1);
        }

        ArrayList<Integer> results = new ArrayList<>();

        for (int i = 0; i < times.size(); i++) {
            int time = times.get(i);
            double dist = distances.get(i).doubleValue();
            double t = ((double) time / 2.0) + Math.sqrt((Math.pow(time / 2, 2) - dist));

            int t_int = (int) Math.floor(t);
            int result = t_int - (time - t_int) + 1;
            results.add(result);
        }

        System.out.println(results.stream().reduce(1, (a, b) -> a * b));
    }
}
