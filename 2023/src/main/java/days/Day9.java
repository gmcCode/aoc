package main.java.days;

import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.stream.IntStream;

import processing.core.PApplet;

public class Day9 extends AbstractDay {

    public Day9(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private int[] nextRow(int[] currRow) {
        int[] newRow = new int[currRow.length - 1];
        for (int i = 0; i < currRow.length - 1; i++) {
            newRow[i] = currRow[i + 1] - currRow[i];
        }
        return newRow;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");

        int result = 0;
        for (String report : input) {
            int[] values = Arrays.stream(report.split(" ")).mapToInt(Integer::parseInt).toArray();

            // loop bis null
            int innerSum = values[values.length - 1];
            while (!Arrays.stream(values).allMatch(i -> i == 0)) {
                values = nextRow(values);
                innerSum += values[values.length - 1];
            }
            result += innerSum;
        }

        System.out.println(result);
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");

        int result = 0;
        for (String report : input) {
            int[] values = Arrays.stream(report.split(" ")).mapToInt(Integer::parseInt).toArray();
            final int[] finalArray = Arrays.copyOf(values, values.length);
            values = IntStream.rangeClosed(1, finalArray.length)
                    .map(i -> finalArray[finalArray.length - i]).toArray();

            // loop bis null
            int innerSum = values[values.length - 1];
            while (!Arrays.stream(values).allMatch(i -> i == 0)) {
                values = nextRow(values);
                innerSum += values[values.length - 1];
            }
            result += innerSum;
        }

        System.out.println(result);
    }
}
