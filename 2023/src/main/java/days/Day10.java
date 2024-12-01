package main.java.days;

import processing.core.PApplet;
import java.util.HashSet;
import java.util.Objects;

public class Day10 extends AbstractDay {

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

    private enum Dir {
        UP,
        RIGHT,
        DOWN,
        LEFT
    }

    public Day10(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private Tuple fillMapAndFindStart() {
        map = new char[input[0].length()][input.length];
        Tuple start = new Tuple();
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length(); j++) {
                map[j][i] = input[i].charAt(j);
                if (input[i].charAt(j) == 'S') {
                    start.x = j;
                    start.y = i;
                }
            }
        }
        return start;
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");
        Tuple start = fillMapAndFindStart();

        Tuple curr = new Tuple();
        Dir direction;
        int circleSize = 1;

        // Ausgang aus S suchen
        if (map[start.x + 1][start.y] == '-' || map[start.x + 1][start.y] == 'J' || map[start.x + 1][start.y] == '7') {
            curr.set(start.x + 1, start.y);
            direction = Dir.LEFT;
        } else if (map[start.x - 1][start.y] == '-' || map[start.x - 1][start.y] == 'F'
                || map[start.x - 1][start.y] == 'L') {
            curr.set(start.x - 1, start.y);
            direction = Dir.RIGHT;
        } else if (map[start.x][start.y - 1] == '|' || map[start.x][start.y - 1] == 'F'
                || map[start.x][start.y - 1] == '7') {
            curr.set(start.x, start.y + 1);
            direction = Dir.DOWN;
        } else {
            curr.set(start.x, start.y - 1);
            direction = Dir.UP;
        }

        // solange knoten nicht gleich S ist
        while (!(curr.x == start.x && curr.y == start.y)) {
            switch (map[curr.x][curr.y]) {
                case '-':
                    if (direction == Dir.RIGHT) {
                        curr.x -= 1;
                    } else {
                        curr.x += 1;
                        direction = Dir.LEFT;
                    }
                    break;
                case '|':
                    if (direction == Dir.DOWN) {
                        curr.y -= 1;
                    } else {
                        curr.y += 1;
                        direction = Dir.UP;
                    }
                    break;
                case 'L':
                    if (direction == Dir.RIGHT) {
                        curr.y -= 1;
                        direction = Dir.DOWN;
                    } else {
                        curr.x += 1;
                        direction = Dir.LEFT;
                    }
                    break;
                case 'J':
                    if (direction == Dir.LEFT) {
                        curr.y -= 1;
                        direction = Dir.DOWN;
                    } else {
                        curr.x -= 1;
                        direction = Dir.RIGHT;
                    }
                    break;
                case '7':
                    if (direction == Dir.LEFT) {
                        curr.y += 1;
                        direction = Dir.UP;
                    } else {
                        curr.x -= 1;
                        direction = Dir.RIGHT;
                    }
                    break;
                case 'F':
                    if (direction == Dir.DOWN) {
                        curr.x += 1;
                        direction = Dir.LEFT;
                    } else {
                        curr.y += 1;
                        direction = Dir.UP;
                    }
                    break;
                default:
                    System.out.println("💥 Irgendwas ist hier falsch gelaufen!");
                    break;
            }
            circleSize++;
        }
        System.out.println(circleSize / 2);
        // methode aus predecessor und knoten nachfolger bestimmen
        // -> -,J,7 ; <- -,F,L ; unten |,L,J; oben |,7,F

    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        Tuple start = fillMapAndFindStart();

        HashSet<Tuple> circle = new HashSet<Tuple>();
        circle.add(start);

        Tuple curr = new Tuple();
        Dir direction;

        // Ausgang aus S suchen
        if (map[start.x + 1][start.y] == '-' || map[start.x + 1][start.y] == 'J' || map[start.x + 1][start.y] == '7') {
            curr.set(start.x + 1, start.y);
            direction = Dir.LEFT;
        } else if (map[start.x - 1][start.y] == '-' || map[start.x - 1][start.y] == 'F'
                || map[start.x - 1][start.y] == 'L') {
            curr.set(start.x - 1, start.y);
            direction = Dir.RIGHT;
        } else if (map[start.x][start.y - 1] == '|' || map[start.x][start.y - 1] == 'F'
                || map[start.x][start.y - 1] == '7') {
            curr.set(start.x, start.y + 1);
            direction = Dir.DOWN;
        } else {
            curr.set(start.x, start.y - 1);
            direction = Dir.UP;
        }

        // solange knoten nicht gleich S ist
        while (!(curr.x == start.x && curr.y == start.y)) {
            circle.add(new Tuple(curr.x, curr.y));
            switch (map[curr.x][curr.y]) {
                case '-':
                    if (direction == Dir.RIGHT) {
                        curr.x -= 1;
                    } else {
                        curr.x += 1;
                        direction = Dir.LEFT;
                    }
                    break;
                case '|':
                    if (direction == Dir.DOWN) {
                        curr.y -= 1;
                    } else {
                        curr.y += 1;
                        direction = Dir.UP;
                    }
                    break;
                case 'L':
                    if (direction == Dir.RIGHT) {
                        curr.y -= 1;
                        direction = Dir.DOWN;
                    } else {
                        curr.x += 1;
                        direction = Dir.LEFT;
                    }
                    break;
                case 'J':
                    if (direction == Dir.LEFT) {
                        curr.y -= 1;
                        direction = Dir.DOWN;
                    } else {
                        curr.x -= 1;
                        direction = Dir.RIGHT;
                    }
                    break;
                case '7':
                    if (direction == Dir.LEFT) {
                        curr.y += 1;
                        direction = Dir.UP;
                    } else {
                        curr.x -= 1;
                        direction = Dir.RIGHT;
                    }
                    break;
                case 'F':
                    if (direction == Dir.DOWN) {
                        curr.x += 1;
                        direction = Dir.LEFT;
                    } else {
                        curr.y += 1;
                        direction = Dir.UP;
                    }
                    break;
                default:
                    System.out.println("💥 Irgendwas ist hier falsch gelaufen!");
                    break;
            }
        }
        map[start.x][start.y] = 'L';

        int innerBlocks = 0;

        for (int i = 0; i < map[0].length; i++) {
            boolean inside = false;
            boolean downToUp = false;
            for (int j = 0; j < map.length; j++) {
                if (circle.contains(new Tuple(j, i))) {
                    char a = map[j][i];
                    switch (map[j][i]) {
                        case 'J':
                            if (downToUp) {
                                inside = !inside;
                            }
                            break;
                        case 'L':
                            downToUp = false;
                            break;
                        case '7':
                            if (!downToUp) {
                                inside = !inside;
                            }
                            break;
                        case 'F':
                            downToUp = true;
                            break;
                        case '|':
                            inside = !inside;
                            break;
                        default:
                            break;
                    }
                } else {
                    if (inside) {
                        innerBlocks++;
                    }
                }
            }
        }

        System.out.println(innerBlocks);

    }

}
