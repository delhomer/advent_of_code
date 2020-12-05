INPUT_FILEPATH = "2020/day05/input"


def read_input():
    with open(INPUT_FILEPATH, "r") as fobj:
        return fobj.readlines()


def convert_binary_sequence(seq, upper_value):
    return sum(2 ** (len(seq) - idx - 1) for idx, item in enumerate(seq) if item == upper_value)

def compute_seat_id(seat_code):
    assert len(seat_code) == 10
    row_code = seat_code[:7]
    column_code = seat_code[7:]
    row = convert_binary_sequence(row_code, "B")
    column = convert_binary_sequence(column_code, "R")
    return row * 8 + column


def find_missing_seat(seats):
    ordered_seats = sorted(seats)
    for idx, seat in enumerate(ordered_seats):
        if ordered_seats[idx - 1] != seat - 1 and idx > 0:
            return seat - 1
        
    
if __name__ == "__main__":

    lines = read_input()

    seat_ids = []
    for line in lines:
        line = line.strip()
        seat_id = compute_seat_id(line)
        seat_ids.append(seat_id)
    missing_seat_id = find_missing_seat(seat_ids)
    print("Missing seat ID: {}".format(missing_seat_id))
