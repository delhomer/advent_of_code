"""Advent of code 2020, day21, part01
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

        dubious_ingredients = set()
        for ca, ingredients in possible_ingredients.items():
            for ingredient in ingredients:
                dubious_ingredients.add(ingredient)

        safe_ingredients = 0
        for food in foods:
            safe_ingredients += sum(ingredient not in dubious_ingredients for ingredient in food)
        return safe_ingredients


def run(input_str, expected_result=None):
    result = read_input(input_str)
    print(
        "Number of ingredients without allergen{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 5)
    run("input")
