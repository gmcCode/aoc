package main.java.days;

import processing.core.PApplet;

import java.util.ArrayList;
import java.util.HashSet;

public class Day3 extends AbstractDay {

    public Day3(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    char[][] numbers;

    public class Tuple {
        public final int x;
        public final int y;

        public Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public ArrayList<Tuple> getNeighbors(Tuple coord) {
        ArrayList<Tuple> neighbors = new ArrayList<>();
        neighbors.add(new Tuple(coord.x - 1, coord.y - 1));
        neighbors.add(new Tuple(coord.x, coord.y - 1));
        neighbors.add(new Tuple(coord.x + 1, coord.y - 1));
        neighbors.add(new Tuple(coord.x - 1, coord.y));
        neighbors.add(new Tuple(coord.x + 1, coord.y));
        neighbors.add(new Tuple(coord.x - 1, coord.y + 1));
        neighbors.add(new Tuple(coord.x, coord.y + 1));
        neighbors.add(new Tuple(coord.x + 1, coord.y + 1));
        return neighbors;
    }

    public boolean testCoordinate(Tuple coord) {
        for (Tuple neighbor : getNeighbors(coord)) {
            try {
                char value = numbers[neighbor.x][neighbor.y];
                if (!Character.isDigit(value) && value != '.') {
                    return true;
                }
            } catch (IndexOutOfBoundsException e) {
            }
        }
        return false;
    }

    @Override
    public void puzzle1() {
        numbers = new char[input[0].length()][input.length];
        for (int row = 0; row < input.length; row++) {
            for (int col = 0; col < input[row].length(); col++) {
                numbers[row][col] = input[row].charAt(col);
            }
        }

        int sum = 0;
        for (int row = 0; row < input.length; row++) {
            String tempNumber = "";
            boolean number = false;
            ArrayList<Tuple> coordinates = new ArrayList<>();
            for (int col = 0; col < input[row].length(); col++) {
                if (Character.isDigit(numbers[row][col])) {
                    tempNumber += numbers[row][col];
                    coordinates.add(new Tuple(row, col));
                    number = true;
                } else {
                    number = false;
                }
                if (!number || col == input[row].length() - 1) {
                    // number ended because of symbol
                    boolean foundSymbol = false;
                    for (Tuple coord : coordinates) {
                        if (testCoordinate(coord)) {
                            foundSymbol = true;
                            break;
                        }
                    }
                    if (foundSymbol) {
                        sum += Integer.parseInt(tempNumber);
                    }
                    tempNumber = "";
                    coordinates.clear();
                }
            }
        }

        System.out.println("Puzzle 1:");
        System.out.println(sum);

    }

    public int buildNumber(Tuple coord) {
        String tempNumber = Character.toString(numbers[coord.x][coord.y]);
        // to the left
        for (int col = coord.y - 1; col >= 0; col--) {
            char value = numbers[coord.x][col];
            if (Character.isDigit(value)) {
                tempNumber = value + tempNumber;
            } else {
                break;
            }
        }
        // to the right
        for (int col = coord.y + 1; col < numbers[coord.x].length; col++) {
            char value = numbers[coord.x][col];
            if (Character.isDigit(value)) {
                tempNumber += value;
            } else {
                break;
            }
        }
        return Integer.parseInt(tempNumber);
    }

    public Integer[] getGearValues(Tuple gear) {
        HashSet<Integer> gearValues = new HashSet<>();

        for (Tuple neighbor : getNeighbors(gear)) {
            try {
                char value = numbers[neighbor.x][neighbor.y];
                if (Character.isDigit(value)) {
                    // build number
                    gearValues.add(buildNumber(neighbor));
                }
            } catch (IndexOutOfBoundsException e) {
            }
        }
        return gearValues.toArray(new Integer[0]);
    }

    @Override
    public void puzzle2() {
        // Assumption: a gear does not have the same two gearvalues!
        System.out.println("Puzzle 2:");

        numbers = new char[input[0].length()][input.length];
        for (int row = 0; row < input.length; row++) {
            for (int col = 0; col < input[row].length(); col++) {
                numbers[row][col] = input[row].charAt(col);
            }
        }

        int sum = 0;
        for (int row = 0; row < input.length; row++) {
            for (int col = 0; col < input[row].length(); col++) {
                if (numbers[row][col] == '*') {
                    Integer[] gearValues = getGearValues(new Tuple(row, col));
                    if (gearValues.length == 2) {
                        sum += gearValues[0] * gearValues[1];
                    }
                }
            }
        }

        System.out.println(sum);
    }
}
