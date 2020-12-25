"""Advent of code 2020, day22, part01
"""

MAGIC_NUMBER = 20201227


def read_input(input_str):
    with open(input_str, "r") as fobj:
        return [int(line.strip()) for line in fobj]

    
def compute_loop_size(subject_number, target):
    value = 1
    loop_size = 0
    while value != target:
        loop_size += 1
        value *= subject_number
        value %= MAGIC_NUMBER
    return loop_size


def loop(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= MAGIC_NUMBER
    return value


def decrypt(card, door):
    card_loop_size = compute_loop_size(7, card)
    door_loop_size = compute_loop_size(7, door)
    door_encryption_key = loop(door, card_loop_size)
    card_encryption_key = loop(card, door_loop_size)
    assert door_encryption_key == card_encryption_key
    return door_encryption_key


def run(input_str, expected_result=None):
    card, door = read_input(input_str)
    result = decrypt(card, door)
    print(
        "Encryption key{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 14897079)
    run("input")
