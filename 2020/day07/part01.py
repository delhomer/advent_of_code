"""Advent of code 2020, day07, part01
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        rules = {}
        for line in fobj:
            out_bag, in_bags = line.split(" contain ")
            out_bag = out_bag.split(" bags")[0]
            if "no other bags" in in_bags:
                in_bags = []
            else:
                in_bags = [
                    " ".join(b.strip(" .\n").split()[1:3]) for b in in_bags.split(",")
                ]
            rules[out_bag] = in_bags
        return rules


def is_contained(bag, rules):
    containers = set()
    bag_to_check = {bag}
    while(bag_to_check):
        current_bag = bag_to_check.pop()
        for outbag, inbags in rules.items():
            if current_bag in inbags:
                bag_to_check.add(outbag)
                containers.add(outbag)
    return containers


def run(input_filepath, expected_result=None):
    rules = read_input(input_filepath)
    bag_count = len(is_contained("shiny gold", rules))
    print(
        "Number of bags that can contain a 'shiny gold' bag{}: {}".format(
            "" if expected_result is None else " (test set)", bag_count
        )
    )
    if expected_result:
        assert bag_count == expected_result

if __name__ == "__main__":

    run("test_input", 4)
    run("input")
