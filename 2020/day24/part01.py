"""Advent of code 2020, day24, part01
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


def populate(moves):
    tile_cache = {}
    nb_black_tiles = 0
    for move in moves:
        x, y = walk(move)
        if tile_cache.get((x, y)) is not None:
            tile_cache[(x, y)] += 1
            nb_black_tiles = nb_black_tiles + 1 if tile_cache[(x, y)] % 2 == 1 else nb_black_tiles - 1                
        else:
            tile_cache[(x, y)] = 1
            nb_black_tiles += 1
    return nb_black_tiles


def run(input_str, expected_result=None):
    moves = read_input(input_str)
    result = populate(moves)
    print(
        "Number of black tiles on the floor{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 10)
    run("input")
