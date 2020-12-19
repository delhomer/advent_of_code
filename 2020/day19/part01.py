"""Advent of code 2020, day19, part01
"""

from copy import deepcopy


def read_input(filepath):
    with open(filepath, "r") as fobj:
        rules = {}
        for line in fobj:
            if line.strip() == "":
                break
            rule_id, rule_content = line.strip().split(": ")
            if "\"" in rule_content:
                rule_content = rule_content[1]
            else:
                rule_content = [
                    [r for r in rc.split()] for rc in rule_content.split(" | ")
                ]
            rules[rule_id] = rule_content
        messages = [line.strip() for line in fobj]
    return rules, messages
    

def compute_valid_messages(rules):
    rule_queue = deepcopy(rules["0"])
    valid_messages = []
    counter = 0
    while len(rule_queue) > 0:
        if counter % 100000 == 0:
            print("counter:", counter, "len(rule queue):", len(rule_queue), "len(valid_messages):", len(valid_messages))
        cur_rule = rule_queue.pop()
        digits_in_rule = [item.isdigit() for item in cur_rule]
        if True not in digits_in_rule:
            valid_messages.append("".join(cur_rule))
            continue
        first_digit = digits_in_rule.index(True)
        for rule in rules.get(cur_rule[first_digit], []):
            candidate_rule = deepcopy(cur_rule)
            candidate_rule.pop(first_digit)
            for r in reversed(rule):
                candidate_rule.insert(first_digit, r)
            rule_queue.append(candidate_rule)
        counter += 1
    return valid_messages


def run(input_str, expected_result=None):
    rules, messages = read_input(input_str)
    valid_messages = compute_valid_messages(rules)
    result = sum(m in valid_messages for m in messages)
    print(
        "Number of messages that match rule 0{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 2)
    run("input")
