"""Advent of code 2020, day20, part01
"""

import math
import re


def read_input(filepath):
    with open(filepath, "r") as fobj:
        puzzle = {}
        tiles = fobj.read().split("\n\n")
        pattern = re.compile(r"\d+")
        for t in tiles:
            tlines = t.split("\n")
            key = pattern.findall(tlines[0])[0]
            tile = [list(titem) for titem in tlines[1:]]
            puzzle[int(key)] = tile
        return puzzle


def borders(tile):
    return [tile[0], [line[-1] for line in tile], tile[-1], [line[0] for line in tile]]


def rotate(tile, rho=90):
    size = len(tile)
    new_tile = [[-1 for _ in range(size)] for _ in range(size)]
    ref_tile = [[tile[x][y] for y in range(size)] for x in range(size)]
    for _ in range(rho // 90):
        for x in range(size):
            for y in range(size):
                new_tile[x][y] = ref_tile[size - 1 - y][x]
        ref_tile = [[new_tile[x][y] for y in range(size)] for x in range(size)]
    return new_tile


def horizontal_flip(tile):
    new_tile = []
    for line in tile:
        new_line = []
        for item in reversed(line):
            new_line.append(item)
        new_tile.append(new_line)
    return new_tile


def vertical_flip(tile):
    new_tile = []
    for line in reversed(tile):
        new_tile.append(line)
    return new_tile


def fit(tile1, tile2):
    b1 = borders(tile1)
    b2 = borders(tile2)
    for b1 in borders(tile1):
        for b2 in borders(tile2):
            if b1 == b2 or b1 == [item for item in reversed(b2)]:
                return True
    return False


def find_corners(puzzle):
    corner_ids = []
    for key1, tile1 in puzzle.items():
        neighbor_counter = 0
        for key2, tile2 in puzzle.items():
            if key1 == key2:
                continue
            neighbor_counter += fit(tile1, tile2)
        if neighbor_counter == 2:
            corner_ids.append(key1)
            continue
        if len(corner_ids) == 4:
            break
        if neighbor_counter != 3 and neighbor_counter != 4:
            raise ValueError("Something is wrong in the corner detection...")
    if len(corner_ids) < 4:
        raise ValueError("Not enough corners!")
    return corner_ids

    
def run(input_str, expected_result=None):
    puzzle = read_input(input_str)
    result = 1
    for cid in find_corners(puzzle):
        result *= cid
    print(
        "Multiplication of corner tile IDs{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 20899048083289)
    run("input")
