"""Advent of code 2020, day23, part02
"""


class Cup():
    def __init__(self, label):
        self.value = label
        self.before = self.after = None

    def insert_after(self, cup):
        self.after = cup.after
        self.before = cup
        if cup.after is not None:
            cup.after.before = self
        cup.after = self

    def __repr__(self):
        before_value = str(self.before.value) if self.before else ""
        after_value = str(self.after.value) if self.after else ""
        return before_value + "<-" + str(self.value) + "->" + after_value


class CupCircle():
    def __init__(self, values):
        self.nb_cups = len(values)
        self.cache = {}
        self.first = Cup(values.pop(0))
        self.cache[self.first.value] = self.first
        self.last = None
        current = self.first
        for v in values:
            new_cup = Cup(v)
            new_cup.insert_after(current)
            self.cache[v] = new_cup
            current = new_cup
        self.last = current
        self.close_loop()

    def close_loop(self):
        self.first.before = self.last
        self.last.after = self.first

    def insert(self, value):
        new_cup = Cup(value)
        new_cup.before = self.last
        new_cup.after = self.first
        self.last.after = new_cup
        self.first.before = new_cup
        self.last = new_cup
        self.cache[value] = new_cup
        self.nb_cups += 1

    def mass_insert(self, values):
        for v in values:
            self.insert(v)

    def min(self):
        return min(self.cache)

    def max(self):
        return max(self.cache)

    def get(self, value):
        return self.cache[value]
        
    def focus_on(self, value):
        self.first = self.cache[value]

    def pop(self, value):
        current = self.cache.pop(value)
        current.before.after = current.after
        current.after.before = current.before
        current.before = current.after = None
        self.nb_cups -= 1
        return current

    def __repr__(self):
        res = str(self.first.value) + "->"
        current = self.first.after
        while current.value != self.first.value:
            res += str(current.value) + "->"
            current = current.after
        res += str(current.value)
        return res


def reorder_cups(draw, new_cup, drop_ref=False):
    resulting_draw = []
    for idx, item in enumerate(draw):
        if item != new_cup:
            resulting_draw += [item]
        else:
            start_idx = idx + 1 if drop_ref else idx
            resulting_draw = draw[start_idx:] + resulting_draw
            return resulting_draw


def play_game(cup_circle, iterations):

    min_cup = cup_circle.min()
    max_cup = cup_circle.max()
    for i in range(iterations):
        assert len(cup_circle.cache) == cup_circle.nb_cups
        if cup_circle.cache.get(9) is None:
            print(cup_circle.get(9))
            print("fail")
            import sys
            sys.exit(1)
        current_cup = cup_circle.first.value
        picked_cups = []
        for _ in range(3):
            picked_cups.append(cup_circle.pop(cup_circle.first.after.value))
        ccup = int(current_cup)
        while True:
            ccup -= 1
            if ccup < min_cup:
                ccup = max_cup + 1
                continue
            if ccup not in [pc.value for pc in picked_cups]:
                break
        destination_cup = cup_circle.get(ccup)
        for pc in reversed(picked_cups):
            pc.insert_after(destination_cup)
            cup_circle.cache[pc.value] = pc
            cup_circle.nb_cups += 1
        cup_circle.focus_on(cup_circle.first.after.value)
    cup_1 = cup_circle.get(1)
    return cup_1.after.value, cup_1.after.after.value


def run(input_str, expected_result=None):
    cup_values = [int(value) for value in input_str]
    cup_circle = CupCircle(cup_values)
    cup_circle.mass_insert(range(cup_circle.max() + 1, 1000001))
    result = play_game(cup_circle, 10_000_000)
    result = [result[0], result[1], result[0] * result[1]]
    print(
        "Harder crab cup game result{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    # run("389125467", [934001, 159792, 149245887792])
    run("963275481")
