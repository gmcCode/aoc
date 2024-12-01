package main.java.days;

import processing.core.PApplet;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Day5 extends AbstractDay {

    public Day5(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private ArrayList<Long> mapValues(List<Long> inputs, ArrayList<long[]> map) {
        ArrayList<Long> newTypes = new ArrayList<>();
        for (Long type : inputs) {
            boolean mapped = false;
            for (long[] range : map) {
                if (type >= range[0] && type < range[0] + range[2]) {
                    newTypes.add(type + (range[1] - range[0]));
                    mapped = true;
                    break;
                }
            }
            if (!mapped) {
                newTypes.add(type);
            }
        }
        return newTypes;
    }

    private ArrayList<long[]> mapAndSplitValues(ArrayList<long[]> inputs, ArrayList<long[]> map) {
        ArrayList<long[]> newTypes = new ArrayList<>();
        for (long[] type : inputs) {
            long start = type[0];
            long length = type[1];
            boolean mapable = false;
            outerloop: while (length > 0) {
                mapable = false;
                long[] minimalNext = null;
                for (long[] range : map) {
                    if (start >= range[0] && start < range[0] + range[2]) {
                        mapable = true;
                        long lengthIntervall = range[0] + range[2] - start;
                        if (lengthIntervall >= length) {
                            newTypes.add(new long[] { start + (range[1] - range[0]), length });
                            break outerloop;
                        } else {
                            newTypes.add(new long[] { start + (range[1] - range[0]), lengthIntervall });
                            start += lengthIntervall;
                            length -= lengthIntervall;
                            break;
                        }
                    }
                    if (range[0] > start && (minimalNext == null
                            || (minimalNext != null && minimalNext[0] > range[0]))) {
                        minimalNext = range;
                    }
                }
                if (!mapable) {
                    if (minimalNext == null) {
                        newTypes.add(new long[] { start, length });
                        break outerloop;
                    }
                    long lengthIntervall = minimalNext[0] - start;
                    if (lengthIntervall >= length) {
                        newTypes.add(new long[] { start, length });
                        break outerloop;
                    }
                    newTypes.add(new long[] { start, minimalNext[0] - start });
                    start = minimalNext[0];
                    length -= minimalNext[0] - start;
                }
            }
        }
        return newTypes;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");
        List<Long> seeds = Arrays.stream(input[0].split(":")[1].trim().split(" ")).map(Long::parseLong)
                .toList();

        ArrayList<ArrayList<long[]>> maps = new ArrayList<>(new ArrayList<>());

        boolean foundMap = false;
        int currentMap = 0;
        long[] values = new long[3];
        for (int i = 2; i < input.length; i++) {
            String line = input[i];
            if (!foundMap && line.contains("map:")) {
                foundMap = true;
                maps.add(new ArrayList<long[]>());
                continue;
            }
            if (foundMap && line.length() <= 2) {
                foundMap = false;
                currentMap++;
                continue;
            }
            // parse map
            List<Long> numbers = Arrays.stream(line.trim().split(" ")).map(Long::parseLong).toList();
            values[0] = numbers.get(1);
            values[1] = numbers.get(0);
            values[2] = numbers.get(2);
            maps.get(currentMap).add(values.clone());
        }

        for (ArrayList<long[]> map : maps) {
            seeds = mapValues(seeds, map);
        }

        System.out.println(Collections.min(seeds));

    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");

        String[] temp = input[0].split(":")[1].trim().split(" ");
        ArrayList<long[]> seeds = new ArrayList<long[]>();
        for (int i = 0; i < temp.length; i += 2) {
            seeds.add(new long[] { Long.parseLong(temp[i]), Long.parseLong(temp[i + 1]) });
        }

        ArrayList<ArrayList<long[]>> maps = new ArrayList<>(new ArrayList<>());

        boolean foundMap = false;
        int currentMap = 0;
        long[] values = new long[3];
        for (int i = 2; i < input.length; i++) {
            String line = input[i];
            if (!foundMap && line.contains("map:")) {
                foundMap = true;
                maps.add(new ArrayList<long[]>());
                continue;
            }
            if (foundMap && line.length() <= 2) {
                foundMap = false;
                currentMap++;
                continue;
            }
            // parse map
            List<Long> numbers = Arrays.stream(line.trim().split(" ")).map(Long::parseLong).toList();
            values[0] = numbers.get(1);
            values[1] = numbers.get(0);
            values[2] = numbers.get(2);
            maps.get(currentMap).add(values.clone());
        }

        for (ArrayList<long[]> map : maps) {
            seeds = mapAndSplitValues(seeds, map);
        }

        long min = Long.MAX_VALUE;
        for (long[] interval : seeds) {
            min = Math.min(interval[0], min);
        }

        System.out.println(min);
    }
}
