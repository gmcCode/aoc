package main.java.days;

import processing.core.PApplet;

import java.util.Objects;
import java.util.ArrayList;
import java.util.List;

public class Day15 extends AbstractDay {

    public Day15(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private class Tuple {
        public String label;
        public int value;

        public Tuple(String label, int value) {
            this.label = label;
            this.value = value;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            Tuple tuple = (Tuple) o;
            return label.equals(tuple.label) && value == tuple.value;
        }

        @Override
        public int hashCode() {
            return Objects.hash(label, value);
        }
    }

    public int hashString(String s) {
        int hashValue = 0;
        for (char c : s.toCharArray()) {
            hashValue += (int) c;
            hashValue = (hashValue * 17) % 256;
        }
        return hashValue;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");
        String[] useableInput = input[0].split(",");
        int sum = 0;

        for (String sequence : useableInput) {
            sum += hashString(sequence);
        }

        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        String[] useableInput = input[0].split(",");
        List<List<Tuple>> boxes = new ArrayList<>(256);
        for (int i = 0; i < 256; i++) {
            boxes.add(new ArrayList<Tuple>());
        }

        for (String sequence : useableInput) {
            if (sequence.contains("-")) {
                // remove lens from box
                String label = sequence.split("-")[0];
                List<Tuple> box = boxes.get(hashString(label));
                for (int i = 0; i < box.size(); i++) {
                    if (box.get(i).label.equals(label)) {
                        box.remove(i);
                    }
                }
            }
            if (sequence.contains("=")) {
                String[] instructions = sequence.split("=");
                Tuple curr = new Tuple(instructions[0], Integer.parseInt(instructions[1]));
                List<Tuple> box = boxes.get(hashString(curr.label));
                boolean containsLens = false;
                for (int i = 0; i < box.size(); i++) {
                    if (box.get(i).label.equals(curr.label)) {
                        box.get(i).value = curr.value;
                        containsLens = true;
                    }
                }
                if (!containsLens) {
                    box.add(curr);
                }
            }
        }

        int sum = 0;
        for (int i = 0; i < boxes.size(); i++) {
            for (int j = 0; j < boxes.get(i).size(); j++) {
                sum += (i + 1) * (j + 1) * boxes.get(i).get(j).value;
            }
        }

        System.out.println(sum);
    }

}
