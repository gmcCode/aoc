package main.java.days;

import processing.core.PApplet;

import java.util.HashSet;
import java.util.EnumMap;
import java.util.Objects;

public class Day16 extends AbstractDay {

    char[][] map;
    int mapLength, mapHeigth;
    HashSet<Position> visited;
    HashSet<Tuple> visitedEdgeNodes;

    EnumMap<Dir, Tuple> lookupTable;

    private class Position {
        public int x;
        public int y;
        public Dir direction;

        public Position(int x, int y, Dir direction) {
            this.x = x;
            this.y = y;
            this.direction = direction;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            Position pos = (Position) o;
            return x == pos.x && y == pos.y && direction == pos.direction;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, direction);
        }
    }

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

        public void add(Tuple other) {
            this.x += other.x;
            this.y += other.y;
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

    public Day16(PApplet sketch, String path, int day, boolean useExample) {
        super(sketch, path, day, useExample);
    }

    private void fillMap() {
        map = new char[input[0].length()][input.length];
        mapLength = input[0].length();
        mapHeigth = input.length;
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length(); j++) {
                map[j][i] = input[i].charAt(j);
            }
        }
    }

    private void fillTable() {
        lookupTable = new EnumMap<>(Dir.class);
        lookupTable.put(Dir.UP, new Tuple(0, -1));
        lookupTable.put(Dir.RIGHT, new Tuple(1, 0));
        lookupTable.put(Dir.DOWN, new Tuple(0, 1));
        lookupTable.put(Dir.LEFT, new Tuple(-1, 0));
    }

    private void checkPath(Tuple curr, Dir direction) {
        // todo loop bis rand oder Kreis
        while (curr.x >= 0 && curr.y >= 0 && curr.x < mapLength && curr.y < mapHeigth
                && !visited.contains(new Position(curr.x, curr.y, direction))) {
            visited.add(new Position(curr.x, curr.y, direction));

            switch (map[curr.x][curr.y]) {
                case '.':
                    break;
                case '/':
                    switch (direction) {
                        case UP:
                            direction = Dir.RIGHT;
                            break;
                        case RIGHT:
                            direction = Dir.UP;
                            break;
                        case DOWN:
                            direction = Dir.LEFT;
                            break;
                        case LEFT:
                            direction = Dir.DOWN;
                            break;
                    }
                    break;
                case '\\':
                    switch (direction) {
                        case UP:
                            direction = Dir.LEFT;
                            break;
                        case RIGHT:
                            direction = Dir.DOWN;
                            break;
                        case DOWN:
                            direction = Dir.RIGHT;
                            break;
                        case LEFT:
                            direction = Dir.UP;
                            break;
                    }
                    break;
                case '-':
                    switch (direction) {
                        case UP:
                        case DOWN:
                            checkPath(new Tuple(curr.x - 1, curr.y), Dir.LEFT);
                            checkPath(new Tuple(curr.x + 1, curr.y), Dir.RIGHT);
                            return;
                    }
                    break;
                case '|':
                    switch (direction) {
                        case RIGHT:
                        case LEFT:
                            checkPath(new Tuple(curr.x, curr.y - 1), Dir.UP);
                            checkPath(new Tuple(curr.x, curr.y + 1), Dir.DOWN);
                            return;
                    }
                    break;

            }
            curr.add(lookupTable.get(direction));
        }
        if (curr.x < 0) {
            visitedEdgeNodes.add(new Tuple(curr.x + 1, curr.y));
        } else if (curr.y < 0) {
            visitedEdgeNodes.add(new Tuple(curr.x, curr.y + 1));
        } else if (curr.x > mapLength - 1) {
            visitedEdgeNodes.add(new Tuple(curr.x - 1, curr.y));
        } else if (curr.y > mapHeigth - 1) {
            visitedEdgeNodes.add(new Tuple(curr.x, curr.y - 1));
        }
    }

    @Override
    public void puzzle1() {
        System.out.println("Puzzle 1:");
        fillMap();
        fillTable();

        visited = new HashSet<>();
        visitedEdgeNodes = new HashSet<>();

        checkPath(new Tuple(0, 0), Dir.RIGHT);
        HashSet<Tuple> result = new HashSet<>();

        for (Position pos : visited) {
            result.add(new Tuple(pos.x, pos.y));
        }

        System.out.println(result.size());
    }

    @Override
    public void puzzle2() {
        System.out.println("Puzzle 2:");
        int mostEnergized = 0;

        visitedEdgeNodes = new HashSet<>();
        for (int i = 0; i < mapLength; i++) {
            Tuple[] tempNodes = { new Tuple(i, 0), new Tuple(0, i), new Tuple(i, mapHeigth - 1),
                    new Tuple(mapLength - 1, i) };
            for (Tuple temp : tempNodes) {
                visited = new HashSet<>();
                if (!visitedEdgeNodes.contains(temp)) {
                    checkPath(temp, Dir.DOWN);
                    HashSet<Tuple> result = new HashSet<>();

                    for (Position pos : visited) {
                        result.add(new Tuple(pos.x, pos.y));
                    }
                    mostEnergized = Math.max(mostEnergized, result.size());
                }
            }

        }

        visited = new HashSet<>();

        checkPath(new Tuple(0, 0), Dir.RIGHT);
        HashSet<Tuple> result = new HashSet<>();

        for (Position pos : visited) {
            result.add(new Tuple(pos.x, pos.y));
        }
        mostEnergized = Math.max(mostEnergized, result.size());

        System.out.println(mostEnergized);

    }

}
