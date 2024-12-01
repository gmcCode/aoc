package main.java.days;

import processing.core.PApplet;

import java.util.Arrays;
import java.util.HashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Objects;

public class Day12 extends AbstractDay {

    public Day12(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    // private class Tuple {
    // public String x;
    // public int[] y;

    // public Tuple(String x, int[] y) {
    // this.x = x;
    // this.y = y;
    // }

    // @Override
    // public boolean equals(Object o) {
    // if (this == o)
    // return true;
    // if (o == null || getClass() != o.getClass())
    // return false;
    // Tuple tuple = (Tuple) o;
    // return x == tuple.x && Arrays.equals(y, tuple.y);
    // }

    // @Override
    // public int hashCode() {
    // return Objects.hash(x, y);
    // }
    // }

    // HashMap<Tuple, Long> cache = new HashMap<>();

    private long findPossibilities(String springs, int[] numbers) {
        if (numbers == null || Arrays.stream(numbers).sum() + numbers.length - 1 > springs.length()) {
            return 0;
        }
        // Tuple key = new Tuple(springs, numbers);
        // if (cache.containsKey(key)) {
        // return cache.get(key);
        // }
        String firstBlock;
        if (springs.contains(".")) {
            firstBlock = springs.split("\\.")[0];
        } else {
            return possInBlock(springs, numbers);
        }
        long possibilities = 0;
        int sum = numbers[0];
        int i = 0;
        long temp2 = 0;
        long temp3 = 0;
        while (sum <= firstBlock.length()) {
            temp2 = possInBlock(firstBlock, Arrays.copyOfRange(numbers, 0, i + 1));
            if (i == numbers.length - 1) {
                if (!springs.substring(firstBlock.length() + 1).contains("#")) {
                    possibilities += temp2;
                }
                break;
            }
            if (temp2 > 0) {
                temp3 = findPossibilities(springs.substring(firstBlock.length() + 1),
                        Arrays.copyOfRange(numbers, i + 1, numbers.length));
            }
            if (temp3 > 0) {
                possibilities += temp2 * temp3;
            }
            i++;
            sum += numbers[i] + 1;
        }
        if (!firstBlock.contains("#")) {
            possibilities += findPossibilities(springs.substring(firstBlock.length() + 1), numbers);
        }
        // cache.put(key, possibilities);
        return possibilities;
    }

    private long possInBlock(String springs, int[] numbers) {
        if (numbers == null) {
            return 0;
        }
        // Tuple key = new Tuple(springs, numbers);
        // if (cache.containsKey(key)) {
        // return cache.get(key);
        // }
        long possibilities = 0;
        int i = 0;
        int lengthRestOfBlocks = Arrays.stream(numbers).sum() + numbers.length - 2 - numbers[0];
        if (numbers.length == 1) {
            lengthRestOfBlocks++;
        }
        while (springs.length() - (numbers[0] + i) >= lengthRestOfBlocks) {
            if (numbers[0] + i >= springs.length()) {
                possibilities++;
                break;
            }
            if (springs.charAt(numbers[0] + i) != '#') {
                if (numbers.length == 1) {
                    if (!springs.substring(numbers[0] + i + 1).contains("#")) {
                        possibilities++;
                    }
                } else {
                    possibilities += possInBlock(springs.substring(numbers[0] + i + 1),
                            Arrays.copyOfRange(numbers, 1, numbers.length));
                }
            }
            if (springs.charAt(i) == '#') {
                break;
            }
            i++;
        }
        // cache.put(key, possibilities);
        return possibilities;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");
        int sum = 0;

        for (String line : input) {
            String[] temp = line.split(" ");
            String springs = temp[0];
            int[] numbers = Arrays.stream(temp[1].split(",")).mapToInt(Integer::parseInt).toArray();
            int possibilities = 0;
            springs = springs.replaceAll("\\.+", ".");
            springs = springs.replaceAll("^\\.|\\.$", "");
            int lengthOfBlocks = Arrays.stream(numbers).sum() + numbers.length - 1;
            int puffer = springs.length() - lengthOfBlocks;
            if (puffer == 0) {
                possibilities++;
            } else {
                possibilities += findPossibilities(springs, numbers);
            }
            sum += possibilities;
        }
        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");

        long sum = 0;
        int count = 0;

        for (String line : input) {
            String[] temp = line.split(" ");
            String springs = temp[0] + "?" + temp[0] + "?" + temp[0] + "?" + temp[0] + "?" + temp[0];
            int[] numbersInput = Arrays.stream(temp[1].split(",")).mapToInt(Integer::parseInt).toArray();
            int[] numbers = new int[numbersInput.length * 5];
            for (int j = 0; j < 5; j++) {
                for (int i = 0; i < numbersInput.length; i++) {
                    numbers[j * numbersInput.length + i] = numbersInput[i];
                }
            }
            long possibilities = 0;
            springs = springs.replaceAll("\\.+", ".");
            springs = springs.replaceAll("^\\.|\\.$", "");
            int lengthOfBlocks = Arrays.stream(numbers).sum() + numbers.length - 1;
            int puffer = springs.length() - lengthOfBlocks;
            if (puffer == 0) {
                possibilities++;
            } else {
                possibilities += findPossibilities(springs, numbers);
            }
            System.out.println(count++);
            sum += possibilities;
        }
        System.out.println(sum);
    }

}
