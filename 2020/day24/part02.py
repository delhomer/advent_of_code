"""Advent of code 2020, day24, part02
"""


MOVES = {
    "se": (1, -1),
    "sw": (-1, -1),
    "e": (2, 0),
    "w": (-2, 0),
    "ne": (1, 1),
    "nw": (-1, 1),
}


def read_input(filepath):
    with open(filepath, "r") as fobj:
        tiles = [line.strip() for line in fobj]
        moves = []
        for t in tiles:
            idx = 0
            tile_moves = []
            while idx < len(t):
                if t[idx] == "s" or t[idx] == "n":
                    tile_moves.append(t[idx:idx+2])
                    idx += 2
                else:
                    tile_moves.append(t[idx])
                    idx += 1
            moves.append(tile_moves)
    return moves


def walk(move):
    out_x, out_y = 0, 0
    for m in move:
        out_x += MOVES[m][0]
        out_y += MOVES[m][1]
    return out_x, out_y


class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 0

    def switch(self):
        self.state = 0 if self.is_black() else 1

    def is_black(self):
        return bool(self.state)

    def __repr__(self):
        return "(" + str(self.x) + ";" + str(self.y) + ";" + ("black" if self.is_black() else "white") + ")"


class Floor():
    def __init__(self, x, y, moves):
        self.tiles = {(x, y): Tile(x, y)}
        self.populate(moves)

    def get_nb_black_tiles(self):
        return sum(t.state for t in self.tiles.values())

    def tile_exist(self, x, y):
        return True if self.tiles.get((x, y)) else None

    def add_tile(self, x, y):
        self.tiles[(x, y)] = Tile(x, y)

    def get_nb_tiles(self):
        return len(self.tiles)

    def populate(self, moves):
        for move in moves:
            x, y = walk(move)
            if not self.tile_exist(x, y):
                self.add_tile(x, y)
            self.tiles[(x, y)].switch()

    def expand_neighbors(self, x, y):
        if not self.tile_exist(x, y):
            return
        for move in MOVES.values():
            newx, newy = x + move[0], y + move[1]
            if not self.tile_exist(newx, newy):
                self.tiles[(newx, newy)] = Tile(newx, newy)

    def count_black_neighbors(self, tile):
        black_neighbor_counter = 0
        for move in MOVES.values():
            newx, newy = tile.x + move[0], tile.y + move[1]
            if self.tile_exist(newx, newy):
                black_neighbor_counter += self.tiles[(newx, newy)].is_black()
        return black_neighbor_counter

    def update(self):
        # First expand the floor grid to consider unknown white tiles on the border
        tile_list = list(self.tiles.values()).copy()
        for tile in tile_list:
            self.expand_neighbors(tile.x, tile.y)
        # Then, find which tiles must be switched
        tiles_to_switch = []
        for tile in self.tiles.values():
            nb_black_neighbors = self.count_black_neighbors(tile)
            if tile.is_black() and (nb_black_neighbors != 1 and nb_black_neighbors != 2):
                tiles_to_switch.append(tile)
            elif not tile.is_black() and self.count_black_neighbors(tile) == 2:
                tiles_to_switch.append(tile)
        # Last, effectively switch the tiles
        for tile in tiles_to_switch:
            tile.switch()

    def min_x(self):
        return min(t.x for t in self.tiles.values())

    def max_x(self):
        return max(t.x for t in self.tiles.values())

    def min_y(self):
        return min(t.y for t in self.tiles.values())

    def max_y(self):
        return max(t.y for t in self.tiles.values())

    def __repr__(self):
        res = ""
        for y in range(self.max_y(), self.min_y() - 1, -1):
            line = ""
            for x in range(self.min_x(), self.max_x() + 1):
                if not self.tile_exist(x, y):
                    line += "."
                elif self.tiles[(x, y)].is_black():
                    line += "B"
                else:
                    line += "W"
            res += line + "\n"
        return res


def run(input_str, expected_result=None):
    moves = read_input(input_str)
    floor = Floor(0, 0, moves)
    for i in range(1, 101):
        floor.update()
    result = floor.get_nb_black_tiles()
    print(
        "Number of black tiles on the floor{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 2208)
    run("input")
