package main.java.days;

import processing.core.PApplet;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Day4 extends AbstractDay {

    public Day4(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private int getWinningNumberCount(String card) {
        int internalSum = 0;
        ArrayList<Integer> winningNumbers = new ArrayList<>();
        ArrayList<Integer> ourNumbers = new ArrayList<>();
        String[] allNumbers = card.split(":")[1].split("\\|");
        winningNumbers.addAll(
                Arrays.stream(allNumbers[0].trim().replaceAll("\\s+", " ").split(" ")).map(Integer::parseInt)
                        .toList());
        ourNumbers.addAll(
                Arrays.stream(allNumbers[1].trim().replaceAll("\\s+", " ").split(" ")).map(Integer::parseInt)
                        .toList());

        for (int ourNumber : ourNumbers) {
            if (winningNumbers.contains(ourNumber)) {
                internalSum++;
            }
        }
        return internalSum;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");

        int sum = 0;
        for (String card : input) {
            int numberOfWins = getWinningNumberCount(card);
            if (numberOfWins != 0)
                sum += Math.pow(2, numberOfWins - 1);

        }

        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        int[] cardsWon = new int[input.length];
        Arrays.fill(cardsWon, 1);

        for (int i = 0; i < input.length; i++) {
            int numberOfWins = getWinningNumberCount(input[i]);
            for (int j = 1; j <= numberOfWins; j++) {
                cardsWon[i + j] += cardsWon[i];
            }
        }
        System.out.println(IntStream.of(cardsWon).sum());
    }
}
