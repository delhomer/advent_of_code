"""Advent of code 2020, day07, part02
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        rules = {}
        for line in fobj:
            out_bag, in_bags = line.split(" contain ")
            out_bag = out_bag.split(" bags")[0]
            if "no other bags" in in_bags:
                in_bags = dict()
            else:
                in_bags = in_bags.split(",")
                in_bags = {
                    " ".join(b.strip(" .\n").split()[1:3]): int(b.strip(" .\n").split()[0]) for b in in_bags
                }
            rules[out_bag] = in_bags
        return rules


def must_contain(bag, rules):
    bags_to_buy = 1
    for in_bag, multiplier in rules[bag].items():
        content = must_contain(in_bag, rules)
        bags_to_buy += multiplier * must_contain(in_bag, rules)
    return bags_to_buy


def run(input_filepath, expected_result=None):
    rules = read_input(input_filepath)
    bag_count = must_contain("shiny gold", rules) - 1
    print(
        "Number of bags that must contain a 'shiny gold' bag{}: {}".format(
            "" if expected_result is None else " (test set)", bag_count
        )
    )
    if expected_result:
        assert bag_count == expected_result


if __name__ == "__main__":

    run("test_input", 32)
    run("test_input_2", 126)
    run("input")
