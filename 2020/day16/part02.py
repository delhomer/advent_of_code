"""Advent of code 2020, day16, part02
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
            candidate_ticket = [int(v) for v in line.strip().split(",")]
            if scan_line(candidate_ticket, rules):
                nearby_tickets.append(candidate_ticket)
        return rules, personal_ticket, nearby_tickets


def convert_rule(rule_str):
    key, values = rule_str.split(": ")
    values = [[int(vv) for vv in v.split("-")] for v in values.split(" or ")]
    return key, values


def scan_line(ticket, rules):
    def predicat(t):
        return any(
            [
                any([interval[0] <= t <= interval[1] for interval in values])
                for values in rules.values()
            ]
        )
    return all(predicat(t) for t in ticket)


def ticket_check(ticket, rules):
        return {
            key: [
                not any([interval[0] <= t <= interval[1] for interval in values])
                for t in ticket
            ]
            for key, values in rules.items()
        }


def assign_positions(tickets, rules):
    candidate_ids = {k: set(range(len(rules))) for k in rules}
    final_ids = {}
    key_rules = set()
    for ticket in tickets:
        tcheck = ticket_check(ticket, rules)
        for rule in candidate_ids:
            for i in range(len(rules)):
                if tcheck[rule][i]:
                    candidate_ids[rule].remove(i)
                    if len(candidate_ids[rule]) == 1:
                        final_ids[rule] = candidate_ids[rule].pop()
                        key_rules.add(final_ids[rule])
    while(any(cids for cids in candidate_ids.values())):
        while(len(key_rules) > 0):
            key_rule = key_rules.pop()
            for rule in candidate_ids:
                candidate_ids[rule].discard(key_rule)
                if len(candidate_ids[rule]) == 1:
                    final_ids[rule] = candidate_ids[rule].pop()
                    key_rules.add(final_ids[rule])
    return final_ids


def solve(ticket, rule_ids):
    acc = 1
    for rule, rule_id in rule_ids.items():
        if rule.startswith("departure"):
            acc *= ticket[rule_id]
    return acc


def run(input_str, expected_result=None):
    rules, pt, nt = read_input(input_str)
    final_ids = assign_positions(nt, rules)
    print(
        "Assigned positions for rules{}: {}".format(
            "" if expected_result is None else " (test set)", final_ids
        )
    )
    if expected_result:
        assert final_ids == expected_result
    result = solve(pt, final_ids)
    print("Product of 'departure' field values: {}".format(result))


if __name__ == "__main__":

    run("test_input2", {"class": 1, "row": 0, "seat": 2})
    run("input")
