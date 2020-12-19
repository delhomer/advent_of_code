"""Advent of code 2020, day18, part02
"""

import re


def read_input(filepath):
    with open(filepath, "r") as fobj:
        for line in fobj:
            yield line.strip()


def evaluate_without_parenthesis(expression):
    figures = list(map(int, re.findall("\d+", expression)))
    ops = list(re.findall("[\+\*]", expression))
    assert len(figures) == len(ops) + 1
    while sum([op == "+" for op in ops]) > 0:
        idx = ops.index("+")
        a = figures.pop(idx + 1)
        b = figures.pop(idx)
        figures.insert(idx, a + b)
        ops.pop(idx)
    res = 1
    for f in figures:
        res *= f
    return res


def evaluate(expression):
    counter = 0
    expr = expression
    cpar_idx = -1
    opar_ids = [expr.find("(")]
    while opar_ids[-1] > -1:
        cpar_idx = expr.find(")", opar_ids[-1] + 1)
        opar_ids.append(expr.find("(", opar_ids[-1] + 1))
        if cpar_idx < opar_ids[-1] or opar_ids[-1] == -1:
            sub_expression = expr[opar_ids[0]:cpar_idx+1]
            res = evaluate_without_parenthesis(sub_expression[1:-1])
            expr = expr.replace(sub_expression, str(res))
            opar_ids = [expr.find("(")]
        else:
            sub_expression = expr[opar_ids[-1]:cpar_idx+1]
            res = evaluate_without_parenthesis(sub_expression[1:-1])
            expr = expr.replace(sub_expression, str(res))
            opar_ids = [expr.find("(")]
    return evaluate_without_parenthesis(expr)


def run(input_str, expected_result=None):
    if type(input_str) != list:
        expressions = read_input(input_str)
    else:
        expressions = input_str
    result = sum(evaluate(expr) for expr in expressions)
    print(
        "Sum of resulting values{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run(["1 + 2 * 3 + 4 * 5 + 6"], 231)
    run(["1 + (2 * 3) + (4 * (5 + 6))"], 51)
    run(["2 * 3 + (4 * 5)"], 46)
    run(["5 + (8 * 3 + 9 + 3 * 4 * 3)"], 1445)
    run("input")
