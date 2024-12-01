package main.java.days;

import processing.core.PApplet;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Day13 extends AbstractDay {

    public Day13(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
        input = Arrays.copyOf(input, input.length + 1);
        input[input.length - 1] = "";
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");
        ArrayList<String> lines = new ArrayList<>();
        List<Integer> rows = new ArrayList<>();
        ArrayList<Integer> cols = new ArrayList<>();

        int sum = 0;

        for (String line : input) {
            if (line.isEmpty()) {
                // fill cols
                for (int i = 0; i < lines.get(0).length(); i++) {
                    String number = "";
                    for (String convertedLine : lines) {
                        number += convertedLine.charAt(i);
                    }
                    try {
                        cols.add(Integer.parseInt(number, 2));
                    } catch (NumberFormatException e) {
                        System.out.println("Error: The binary string is not valid");
                    }
                }

                rows = lines.stream().map(s -> Integer.parseInt(s, 2)).toList();
                boolean foundReflection = false;

                for (int i = 1; i < cols.size(); i++) {
                    int spaceToSide = Math.min(i, cols.size() - i);
                    boolean symmetrical = true;
                    for (int j = 1; j <= spaceToSide; j++) {
                        if (!cols.get(i - j).equals(cols.get(i + j - 1))) {
                            symmetrical = false;
                            break;
                        }
                    }
                    if (symmetrical) {
                        sum += i;
                        break;
                    }
                }

                if (foundReflection) {
                    cols.clear();
                    lines.clear();
                    continue;
                }

                for (int i = 1; i < rows.size(); i++) {
                    int spaceToSide = Math.min(i, rows.size() - i);
                    boolean symmetrical = true;
                    for (int j = 1; j <= spaceToSide; j++) {
                        if (!rows.get(i - j).equals(rows.get(i + j - 1))) {
                            symmetrical = false;
                            break;
                        }
                    }
                    if (symmetrical) {
                        sum += 100 * i;
                        break;
                    }
                }

                cols.clear();
                lines.clear();
                continue;
            }
            line = line.replaceAll("\\.", "0");
            line = line.replaceAll("#", "1");
            lines.add(line);
        }

        System.out.println(sum);
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        ArrayList<String> lines = new ArrayList<>();
        List<Integer> rows = new ArrayList<>();
        ArrayList<Integer> cols = new ArrayList<>();

        int sum = 0;
        int k = 0;

        for (String line : input) {
            k++;
            if (line.isEmpty()) {
                // fill cols
                for (int i = 0; i < lines.get(0).length(); i++) {
                    String number = "";
                    for (String convertedLine : lines) {
                        number += convertedLine.charAt(i);
                    }
                    try {
                        cols.add(Integer.parseInt(number, 2));
                    } catch (NumberFormatException e) {
                        System.out.println("Error: The binary string is not valid");
                    }
                }

                rows = lines.stream().map(s -> Integer.parseInt(s, 2)).toList();

                boolean foundReflection = false;
                for (int i = 1; i < cols.size(); i++) {
                    int spaceToSide = Math.min(i, cols.size() - i);
                    boolean symmetrical = true;
                    boolean smudge = false;
                    for (int j = 1; j <= spaceToSide; j++) {
                        if (!cols.get(i - j).equals(cols.get(i + j - 1))) {
                            if (!smudge && Integer
                                    .bitCount(Integer.valueOf(cols.get(i - j))
                                            ^ Integer.valueOf(cols.get(i + j - 1))) == 1) {
                                smudge = true;
                                continue;
                            }
                            symmetrical = false;
                            break;
                        }
                    }
                    if (symmetrical && smudge) {
                        foundReflection = true;
                        sum += i;
                        break;
                    }
                }

                if (foundReflection) {
                    cols.clear();
                    lines.clear();
                    continue;
                }

                for (int i = 1; i < rows.size(); i++) {
                    int spaceToSide = Math.min(i, rows.size() - i);
                    boolean symmetrical = true;
                    boolean smudge = false;
                    for (int j = 1; j <= spaceToSide; j++) {
                        if (!rows.get(i - j).equals(rows.get(i + j - 1))) {
                            if (!smudge && Integer
                                    .bitCount(Integer.valueOf(rows.get(i - j))
                                            ^ Integer.valueOf(rows.get(i + j - 1))) == 1) {
                                smudge = true;
                                continue;
                            }
                            symmetrical = false;
                            break;
                        }
                    }
                    if (symmetrical && smudge) {
                        if (foundReflection) {
                            System.out.println(k);
                        }
                        sum += 100 * i;
                        break;
                    }
                }

                cols.clear();
                lines.clear();
                continue;
            }
            line = line.replaceAll("\\.", "0");
            line = line.replaceAll("#", "1");
            lines.add(line);
        }

        System.out.println(sum);

    }

}
