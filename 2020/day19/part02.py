"""Advent of code 2020, day19, part02
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
        rules["8"] = [["42"], ["42", "8"]]
        rules["11"] = [["42", "31"], ["42", "11", "31"]]
        messages = [line.strip() for line in fobj]
    return rules, messages


def compute_valid_messages(rules, key):
    rule_queue = deepcopy(rules[key])
    valid_messages = []
    counter = 0
    while len(rule_queue) > 0:
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
    return valid_messages


def accepted(message, rules):
    """Must contain at least two "42" rules and at least a "31" rule, and there are more beginning "42"
    than ending "31".

    - 0 leads to 8 + 11,
    - 8 leads to 42 or 42 + 8 (hence, at least one 42)
    - 11 leads to 42 + 31 or 42 + 11 + 31 (heace, at least one 42 + at least one 31, and as many 42 as 31)

    """
    strings_42 = compute_valid_messages(rules, "42")
    strings_31 = compute_valid_messages(rules, "31")
    counter_42 = counter_31 = 0
    while True:
        if any(message.startswith(s42) for s42 in strings_42):
            message = message[len(strings_42[0]):]
            counter_42 += 1
        elif counter_42 > 0:
            break
        else:
            return False
    while True:
        if any(message.startswith(s31) for s31 in strings_31):
            message = message[len(strings_31[0]):]
            counter_31 += 1
        elif counter_31 > 0 and message == "":
            break
        else:
            return False
    return counter_42 > counter_31


def run(input_str, expected_result=None):
    rules, messages = read_input(input_str)
    result = sum(accepted(m, rules) for m in messages)
    print(
        "Number of messages that match rule 0{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input2", 12)
    run("input")
