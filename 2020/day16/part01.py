"""Advent of code 2020, day16, part01
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        rules = {}
        while True:
            line = fobj.readline()
            if line.strip() == "":
                break
            key, values = convert_rule(line)
            rules[key] = values
        fobj.readline()  # your ticket:
        personal_ticket = [int(v) for v in fobj.readline().strip().split(",")]
        fobj.readline()  # empty line
        fobj.readline()  # nearby tickets:
        nearby_tickets = []
        while True:
            line = fobj.readline()
            if line.strip() == "":
                break
            nearby_tickets.append([int(v) for v in line.strip().split(",")])
        return rules, personal_ticket, nearby_tickets


def convert_rule(rule_str):
    key, values = rule_str.split(": ")
    values = [[int(vv) for vv in v.split("-")] for v in values.split(" or ")]
    return key, values


def scan_line(ticket, rules):
    def predicat(t):
        return not any(
            [
                any([interval[0] <= t <= interval[1] for interval in values])
                for values in rules.values()
            ]
        )
    return sum(t for t in ticket if predicat(t))


def run(input_str, expected_result=None):
    rules, pt, nt = read_input(input_str)
    result = sum(scan_line(ticket, rules) for ticket in nt)
    print(
        "Ticket scanning error rate (sum of unvalid information){}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 71)
    run("input")
