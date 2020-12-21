"""Advent of code 2020, day21, part02
"""

import re


def read_input(filepath):
    with open(filepath, "r") as fobj:
        possible_allergens = {}
        possible_ingredients = {}
        foods = []
        allergens = []
        for line in fobj:
            ap = re.compile(r"(?:\(contains )(\w+(\,\s\w+)*)")
            cur_allergens = ap.search(line).group(1).split(", ")
            allergens.append(cur_allergens)
            ip = re.compile(r"^(\w+\s*)*(\w+)")
            food = ip.search(line).group(0).split()
            foods.append(food)
            for ca in cur_allergens:
                old_ingredients = possible_ingredients.get(ca, [])
                possible_ingredients[ca] = set()
                for ingredient in food:
                    if len(old_ingredients) == 0 or ingredient in old_ingredients:
                        possible_ingredients[ca].add(ingredient)
                    if possible_allergens.get(ingredient) is not None:
                        possible_allergens[ingredient].add(ca)
                    else:
                        possible_allergens[ingredient] = {ca}
        for allergen, ingredients in possible_ingredients.items():
            if len(ingredients) == 1:
                possible_ingredients[allergen] = ingredients.pop()
        return possible_ingredients


def sort_ingredients(dubious_ingredients):
    key_ingredients = [
        ingredient for ingredient in dubious_ingredients.values() if type(ingredient) == str
    ]
    while any(type(p) == set for p in dubious_ingredients.values()):
        cur_ingredient = key_ingredients.pop(0)
        for allergen, ingredients in dubious_ingredients.items():
            if type(ingredients) == set:
                dubious_ingredients[allergen].discard(cur_ingredient)
                if len(dubious_ingredients[allergen]) == 1:
                    dubious_ingredients[allergen] = dubious_ingredients[allergen].pop()
                    key_ingredients.append(dubious_ingredients[allergen])
    res = ""
    for _, ingredient in sorted(dubious_ingredients.items()):
        res += "," + ingredient
    return res[1:]


def run(input_str, expected_result=None):
    possible_ingredients = read_input(input_str)
    result = sort_ingredients(possible_ingredients)
    print(
        "Number of ingredients without allergen{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", "mxmxvkd,sqjhc,fvjkl")
    run("input")
