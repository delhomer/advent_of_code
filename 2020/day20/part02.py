"""Advent of code 2020, day20, part02
"""

import copy
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
    return {
        "north": tile[0],
        "east": [line[-1] for line in tile],
        "south": tile[-1],
        "west": [line[0] for line in tile],
    }


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
    for idx1, b1 in borders(tile1).items():
        for idx2, b2 in borders(tile2).items():
            if b1 == b2:
                return True, idx1, idx2, False
            if b1 == [item for item in reversed(b2)]:
                return True, idx1, idx2, True
    return False, None, None, None


def find_neighbors(puzzle):
    neighbors = {}
    for key1, tile1 in puzzle.items():
        neighbors[key1] = []
        for key2, tile2 in puzzle.items():
            if key1 == key2:
                continue
            tile_fit, idx1, idx2, reverse = fit(tile1, tile2)
            if tile_fit:
                neighbors[key1].append((key2, idx1, idx2, reverse))
        if len(neighbors[key1]) < 2 or len(neighbors[key1]) > 4:
            raise ValueError("Something is wrong in the neighbor detection...")
    return neighbors


def neighbor_grid(puzzle_dim):
    grid = []
    for i in range(puzzle_dim):
        line = []
        for j in range(puzzle_dim):
            neighbors = []
            if i > 0:
                neighbors.append([i - 1, j])
            if i < puzzle_dim - 1:
                neighbors.append([i + 1, j])
            if j > 0:
                neighbors.append([i, j - 1])
            if j < puzzle_dim - 1:
                neighbors.append([i, j + 1])
            line.append(neighbors)
        grid.append(line)
    return grid


def cut_tile(tile):
    new_tile = []
    for i in range(1, len(tile) - 1):
        new_line = []
        for j in range(1, len(tile) - 1):
            new_line.append(tile[i][j])
        new_tile.append(new_line)
    return new_tile


def order_puzzle(puzzle):
    ordered_puzzle_dim = int(math.sqrt(len(puzzle)))
    ordered_puzzle = [[-1 for _ in range(ordered_puzzle_dim)] for _ in range(ordered_puzzle_dim)]
    neighborhood = neighbor_grid(ordered_puzzle_dim)
    neighbors = find_neighbors(puzzle)
    search_queue = []
    # Look for the top-left corner to initialize the puzzle building
    for key, neighbor_keys in neighbors.items():
        if (
                len(neighbor_keys) == 2 and
                (neighbor_keys[0][1] == "south" or neighbor_keys[0][1] == "east") and
                (neighbor_keys[1][1] == "south" or neighbor_keys[1][1] == "east")
        ):
            ordered_puzzle[0][0] = key
            search_queue.append((0, 0, key))
            break
    counter = 0
    while len(search_queue) > 0:
        x, y, key = search_queue.pop(0)
        do_horizontal_flip = do_vertical_flip = do_rotation = False
        # update neighborhood
        adjacent_positions = neighborhood[x][y]
        neighborhood[x][y] = []
        # update neighbors
        key_neighbors = neighbors[key]
        neighbors[key] = []
        for nkey, idx, nidx, reverse in key_neighbors:
            neighbors[nkey].remove((key, nidx, idx, reverse))
        # assign positions to found neighbors
        for ax, ay in adjacent_positions:
            neighborhood[ax][ay].remove([x, y])
            ref_border = "east" if ay > y else "south"
            for nkey, idx, nidx, reverse in key_neighbors:
                if len(neighborhood[ax][ay]) == len(neighbors[nkey]):
                    transformed_tile = transform(puzzle[nkey], puzzle[key], ref_border)
                    if transformed_tile is None:
                        continue
                    puzzle[nkey] = transformed_tile
                    search_queue.append((ax, ay, nkey))
                    key_neighbors.remove((nkey, idx, nidx, reverse))
                    break
        ordered_puzzle[x][y] = key
    return puzzle, ordered_puzzle


TRANSFORMATION_SEQUENCE = [
    vertical_flip,
    horizontal_flip,
    vertical_flip,
    rotate,
    vertical_flip,
    horizontal_flip,
    vertical_flip,
]


def transform(tile, ref_tile, ref_border="east"):
    tile = copy.deepcopy(tile)
    if borders(tile)["west" if ref_border == "east" else "north"] == borders(ref_tile)[ref_border]:
        return tile
    for t in TRANSFORMATION_SEQUENCE:
        tile = t(tile)
        if borders(tile)["west" if ref_border == "east" else "north"] == borders(ref_tile)[ref_border]:
            return tile
    for t in TRANSFORMATION_SEQUENCE:
        tile = t(tile)
        if borders(tile)["west" if ref_border == "east" else "north"] == borders(ref_tile)[ref_border]:
            return tile
    return None


def assemble_puzzle(puzzle, ordered_puzzle):
    assembled_puzzle = []
    for x in range(len(ordered_puzzle)):
        assembled_lines = cut_tile(puzzle[ordered_puzzle[x][0]])
        for y in range(1, len(ordered_puzzle)):
            ordered_tile = cut_tile(puzzle[ordered_puzzle[x][y]])
            for i in range(len(assembled_lines)):
                assembled_lines[i] += ordered_tile[i]
        assembled_puzzle += ["".join(ai) for ai in assembled_lines]
    return assembled_puzzle


def count_monster(puzzle):
    """Look at the monster!
                      #
    #    ##    ##    ###
     #  #  #  #  #  #
     ^
     |
     |
    character of reference
    """
    monster_counter = 0
    for i in range(2, len(puzzle)):
        for j in range(1, len(puzzle[0]) - 19):
            monster_counter += (
                puzzle[i][j] == "#" and
                puzzle[i][j+3] == "#" and
                puzzle[i][j+6] == "#" and
                puzzle[i][j+9] == "#" and
                puzzle[i][j+12] == "#" and
                puzzle[i][j+15] == "#" and
                puzzle[i-1][j-1] == "#" and
                puzzle[i-1][j+4] == "#" and
                puzzle[i-1][j+5] == "#" and
                puzzle[i-1][j+10] == "#" and
                puzzle[i-1][j+11] == "#" and
                puzzle[i-1][j+16] == "#" and
                puzzle[i-1][j+17] == "#" and
                puzzle[i-1][j+18] == "#" and
                puzzle[i-2][j+17] == "#"
            )
    return monster_counter


def compute_water_roughness(image):
    nb_characters = sum(sum(c == "#" for c in line) for line in image)
    counter = 0
    checked_direction = 0
    while counter == 0 and checked_direction < 2:
        counter = count_monster(image)
        if counter > 0:
            break
        image_horiz_flip = horizontal_flip(image)
        counter = count_monster(image_horiz_flip)
        if counter > 0:
            break
        image_vert_flip = vertical_flip(image)
        counter = count_monster(image_vert_flip)
        if counter > 0:
            break
        image_horvert_flip = vertical_flip(image_horiz_flip)
        counter = count_monster(image_horvert_flip)
        if counter > 0:
            break
        image = rotate(image)
        checked_direction += 1
    assert counter > 0
    return nb_characters - 15 * counter


def test_assembled_puzzle(assembled_puzzle):
    with open("test_image") as fobj:
        expected_puzzle = [line.strip() for line in fobj]
    if not all(exp == res for exp, res in zip(expected_puzzle, assembled_puzzle)):
        res_puzzle = copy.deepcopy(assembled_puzzle)
        for t in TRANSFORMATION_SEQUENCE:
            res_puzzle = t(res_puzzle)
            if all(exp == res for exp, res in zip(expected_puzzle, res_puzzle)):
                return
        else:
            raise ValueError("The assembled puzzle does not equal to the expected one.")

def run(input_str, expected_result=None):
    puzzle = read_input(input_str)
    puzzle, ordered_puzzle = order_puzzle(puzzle)
    assembled_puzzle = assemble_puzzle(puzzle, ordered_puzzle)
    if expected_result is not None:
        test_assembled_puzzle(assembled_puzzle)
    result = compute_water_roughness(assembled_puzzle)
    print(
        "Habitat's water roughness{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 273)
    run("input")
