package main.java.days;

import processing.core.PApplet;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import java.util.HashMap;
import java.util.Map;

public class Day2 extends AbstractDay {

    public Day2(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private HashMap<Character, Integer> getMaxCounts(String game) {
        HashMap<Character, Integer> maxValues = new HashMap<Character, Integer>();
        Pattern p = Pattern.compile("(\\d+) (r|b|g)");
        Matcher m = p.matcher(game);
        while (m.find()) {
            int count = Integer.parseInt(m.group(1));
            char color = m.group(2).charAt(0);
            maxValues.put(color, Math.max(maxValues.getOrDefault(color, 0), count));
        }
        return maxValues;
    }

    @Override
    public void puzzle1() {
        Map<Character, Integer> allowedValues = Map.of('r', 12, 'g', 13, 'b', 14);

        int sum = 0;

        int gameCnt = 1;
        for (String game : input) {
            HashMap<Character, Integer> maxValues = getMaxCounts(game);

            boolean gamePossible = true;
            for (Map.Entry<Character, Integer> entry : allowedValues.entrySet()) {
                if (maxValues.get(entry.getKey()) > entry.getValue()) {
                    gamePossible = false;
                }
            }
            if (gamePossible)
                sum += gameCnt;

            gameCnt++;
        }

        System.out.println("Puzzle 1:");
        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        int sum = 0;

        for (String game : input) {
            HashMap<Character, Integer> maxValues = getMaxCounts(game);
            int temp = 1;
            for (Integer value : maxValues.values()) {
                temp *= value;
            }
            sum += temp;
        }

        System.out.println("Puzzle 2:");
        System.out.println(sum);
    }

}
