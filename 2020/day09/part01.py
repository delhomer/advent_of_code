"""Advent of code 2020, day09, part01
"""

def read_input(filepath, buffer_size):
    with open(filepath, "r") as fobj:
        buffered_numbers = []
        for line in fobj:
            candidate_number = int(line.strip())
            if len(buffered_numbers) < buffer_size:
                buffered_numbers.append(candidate_number)
                continue
            else:
                valid_candidate = False
                for idx1, b1 in enumerate(buffered_numbers):
                    for b2 in buffered_numbers[idx1:]:
                        if b1 + b2 == candidate_number:
                            buffered_numbers.append(candidate_number)
                            valid_candidate = True
                            break
                    if valid_candidate:
                        break
                if len(buffered_numbers) > buffer_size:
                    buffered_numbers.pop(0)
                else:
                    return candidate_number


def run(input_filepath, expected_result=None, buffer_size=None):
    unvalid_number = read_input(input_filepath, buffer_size)
    print(
        "First unvalid number regarding XMAS encoding{}: {}".format(
            "" if expected_result is None else " (test set)", unvalid_number
        )
    )
    if expected_result:
        assert unvalid_number == expected_result


if __name__ == "__main__":

    run("test_input", 127, buffer_size=5)
    run("input", buffer_size=25)
