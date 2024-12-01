package main.java.days;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import processing.core.PApplet;

public class Day8 extends AbstractDay {

    String instructions;
    HashMap<String, Node> network;

    private class Node {
        String left;
        String right;

        public Node(String left, String right) {
            this.left = left;
            this.right = right;
        }
    }

    public Day8(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private long ggT(long a, long b) {
        if (b == 0) {
            return a;
        } else {
            return ggT(b, a % b);
        }
    }

    private long kGV(long a, long b) {
        return (a * b) / ggT(a, b);
    }

    private void buildNetwork(String[] input) {
        network = new HashMap<>();
        Pattern p = Pattern.compile("(\\w+) = \\((\\w+), (\\w+)\\)");

        for (int i = 2; i < input.length; i++) {
            Matcher m = p.matcher(input[i]);
            if (m.find()) {
                network.put(m.group(1), new Node(m.group(2), m.group(3)));
            }
        }
    }

    private int countSteps(String start) {
        String currentNode = start;
        int instructionsCounter = 0;
        int steps = 0;

        while (!currentNode.endsWith("Z")) {
            char direction = instructions.charAt(instructionsCounter);

            if (direction == 'L') {
                currentNode = network.get(currentNode).left;
            } else {
                currentNode = network.get(currentNode).right;
            }

            steps++;
            instructionsCounter = (instructionsCounter + 1) % instructions.length();
        }
        return steps;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");

        instructions = input[0];
        buildNetwork(input);

        int result = countSteps("AAA");

        System.out.println(result);

    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");

        instructions = input[0];
        buildNetwork(input);

        ArrayList<Integer> steps = new ArrayList<>();

        for (String start : network.keySet()) {
            if (start.endsWith("A"))
                steps.add(countSteps(start));
        }

        long result = steps.stream().map(i -> Long.valueOf(i)).reduce((a, b) -> kGV(a, b)).orElse(0l);

        System.out.println(result);

    }
}
