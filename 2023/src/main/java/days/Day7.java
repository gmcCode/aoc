package main.java.days;

import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.Arrays;
import java.util.Comparator;

import processing.core.PApplet;

public class Day7 extends AbstractDay {

    public Day7(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private long mapHandToNumber(int[] input) {
        long handValue = 0;
        int[] count = new int[14];
        Arrays.fill(count, 0);
        int temp = 0;
        for (int i = 0; i < input.length; i++) {
            temp = input[i];
            count[temp - 1]++;
        }
        Arrays.sort(count);
        if (count[13] == 5) {
            handValue = 6;
        } else if (count[13] == 4) {
            handValue = 5;
        } else if (count[13] == 3) {
            if (count[12] == 2) {
                handValue = 4;
            } else {
                handValue = 3;
            }
        } else if (count[13] == 2) {
            if (count[12] == 2) {
                handValue = 2;
            } else {
                handValue = 1;
            }
        } else {
            handValue = 0;
        }
        for (int i = 0; i < input.length; i++) {
            handValue = handValue * 100 + input[i];
        }
        return handValue;
    }

    private long mapHandToNumberPartTwo(int[] input) {
        long handValue = 0;
        int[] count = new int[14];
        Arrays.fill(count, 0);
        int temp = 0;
        for (int i = 0; i < input.length; i++) {
            temp = input[i];
            count[temp - 1]++;
        }
        int joker = count[0];
        count[0] = 0;
        Arrays.sort(count);
        count[13] += joker;

        // dasselbe wie bei der Funktion oben, nur kompakter
        if (count[13] > 3) {
            handValue = count[13] + 1;
        } else if (count[13] > 1) {
            handValue = (count[13] - 2) * 2 + count[12];
        }

        for (int i = 0; i < input.length; i++) {
            handValue = handValue * 100 + input[i];
        }
        return handValue;
    }

    private int[] mapCharToNumber(String input, boolean partOne) {
        Map<Character, Integer> charMap = new HashMap<>();
        charMap.put('T', 10);
        if (partOne) {
            charMap.put('J', 11);
        } else {
            charMap.put('J', 1);
        }
        charMap.put('Q', 12);
        charMap.put('K', 13);
        charMap.put('A', 14);

        return input.chars().map(c -> charMap.getOrDefault((char) c, Character.getNumericValue(c))).toArray();
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");

        List<long[]> hands = new ArrayList<>();
        for (String line : input) {
            String hand = line.split(" ")[0];
            String bid = line.split(" ")[1];
            int[] temp = mapCharToNumber(hand, true);
            long handValue = mapHandToNumber(temp);
            hands.add(new long[] { handValue, Long.parseLong(bid) });
        }
        hands.sort(Comparator.comparingLong(arr -> arr[0]));

        int sum = 0;
        for (int i = 0; i < hands.size(); i++) {
            sum += hands.get(i)[1] * (i + 1);
        }
        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        List<long[]> hands = new ArrayList<>();
        for (String line : input) {
            String hand = line.split(" ")[0];
            String bid = line.split(" ")[1];
            int[] temp = mapCharToNumber(hand, false);
            long handValue = mapHandToNumberPartTwo(temp);
            hands.add(new long[] { handValue, Long.parseLong(bid) });
        }
        hands.sort(Comparator.comparingLong(arr -> arr[0]));

        int sum = 0;
        for (int i = 0; i < hands.size(); i++) {
            sum += hands.get(i)[1] * (i + 1);
        }
        System.out.println(sum);
    }
}
