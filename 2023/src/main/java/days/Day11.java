package main.java.days;

import processing.core.PApplet;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Objects;

public class Day11 extends AbstractDay {

    char[][] map;

    private class Tuple {
        public int x;
        public int y;

        public Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Tuple() {
            this.x = 0;
            this.y = 0;
        }

        public void set(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            Tuple tuple = (Tuple) o;
            return x == tuple.x && y == tuple.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public Day11(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private void fillMap() {
        map = new char[input[0].length()][input.length];
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length(); j++) {
                map[j][i] = input[i].charAt(j);
            }
        }
    }

    @Override
    public void puzzle1() {
        fillMap();

        HashSet<Integer> cols = new HashSet<>();
        HashSet<Integer> rows = new HashSet<>();

        for (int i = 0; i < input.length; i++) {
            boolean empty = true;
            for (int j = 0; j < input[i].length(); j++) {
                if (map[j][i] != '.') {
                    empty = false;
                    break;
                }
            }
            if (empty) {
                rows.add(i);
            }
        }
        for (int i = 0; i < input[0].length(); i++) {
            boolean empty = true;
            for (int j = 0; j < input.length; j++) {
                if (map[i][j] != '.') {
                    empty = false;
                    break;
                }
            }
            if (empty) {
                cols.add(i);
            }
        }

        ArrayList<Tuple> galaxies = new ArrayList<>();

        int temp_x = 0;
        int temp_y = 0;
        for (int i = 0; i < input.length; i++) {
            temp_x = 0;
            if (rows.contains(i)) {
                temp_y += 1;
            }
            for (int j = 0; j < input[i].length(); j++) {
                if (cols.contains(j)) {
                    temp_x += 1;
                } else if (map[j][i] == '#') {
                    galaxies.add(new Tuple(j + temp_x, i + temp_y));
                }
            }
        }

        int pairDistances = 0;

        for (int i = 0; i < galaxies.size(); i++) {
            for (int j = i + 1; j < galaxies.size(); j++) {
                Tuple first = galaxies.get(i);
                Tuple second = galaxies.get(j);
                pairDistances += (Math.abs(first.x - second.x) + (Math.abs(first.y - second.y)));
            }
        }

        System.out.println("Puzzle 1:");
        System.out.println(pairDistances);

    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        fillMap();

        HashSet<Integer> cols = new HashSet<>();
        HashSet<Integer> rows = new HashSet<>();

        for (int i = 0; i < input.length; i++) {
            boolean empty = true;
            for (int j = 0; j < input[i].length(); j++) {
                if (map[j][i] != '.') {
                    empty = false;
                    break;
                }
            }
            if (empty) {
                rows.add(i);
            }
        }
        for (int i = 0; i < input[0].length(); i++) {
            boolean empty = true;
            for (int j = 0; j < input.length; j++) {
                if (map[i][j] != '.') {
                    empty = false;
                    break;
                }
            }
            if (empty) {
                cols.add(i);
            }
        }

        ArrayList<Tuple> galaxies = new ArrayList<>();

        int temp_x = 0;
        int temp_y = 0;
        for (int i = 0; i < input.length; i++) {
            temp_x = 0;
            if (rows.contains(i)) {
                temp_y += 999999;
            }
            for (int j = 0; j < input[i].length(); j++) {
                if (cols.contains(j)) {
                    temp_x += 999999;
                } else if (map[j][i] == '#') {
                    galaxies.add(new Tuple(j + temp_x, i + temp_y));
                }
            }
        }

        long pairDistances = 0;

        for (int i = 0; i < galaxies.size(); i++) {
            for (int j = i + 1; j < galaxies.size(); j++) {
                Tuple first = galaxies.get(i);
                Tuple second = galaxies.get(j);
                pairDistances += (Math.abs(first.x - second.x) + (Math.abs(first.y - second.y)));
            }
        }

        System.out.println(pairDistances);
    }

}
