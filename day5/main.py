import math

boarding_passes = tuple(open('input', 'r'))

count_rows = 128
count_columns = 8

PLACE_TAKEN = 'X'
PLACE_UNTAKEN = ''
grid = [PLACE_UNTAKEN] * ((count_rows - 1) * 8 + (count_columns - 1))


def boarding_pass_to_seat_id(boarding_pass):
    # print(boarding_pass)
    current_rows = [0, count_rows - 1]
    current_columns = [0, count_columns - 1]
    boarding_pass = boarding_pass.strip()

    for letter in boarding_pass:
        if letter == 'F':
            current_rows[1] -= math.ceil((current_rows[1] - current_rows[0]) / 2)
        elif letter == 'B':
            current_rows[0] += math.ceil((current_rows[1] - current_rows[0]) / 2)
        elif letter == 'L':
            current_columns[1] -= math.ceil((current_columns[1] - current_columns[0]) / 2)
        elif letter == 'R':
            current_columns[0] += math.ceil((current_columns[1] - current_columns[0]) / 2)
        else:
            raise ValueError(f"Unsupported letter '{letter}' in boarding pass {boarding_pass}")

    if current_rows[0] == current_rows[1]:
        row = current_rows[0]
    else:
        raise ValueError(f'Could not find row seat for {boarding_pass}. '
                         f'Current range = {current_rows[0]}-{current_rows[1]}')

    if current_columns[0] == current_columns[1]:
        column = current_columns[0]
    else:
        raise ValueError(f'Could not find column seat for {boarding_pass}. '
                         f'Current range = {current_columns[0]}-{current_columns[1]}')
    seat_id = row * 8 + column
    grid[seat_id] = PLACE_TAKEN
    return seat_id


seat_ids = list(map(boarding_pass_to_seat_id, boarding_passes))
print(f'Maximum seat id : {max(seat_ids)}')
for idx, _ in enumerate(grid):
    if 0 < idx < len(grid):
        found = grid[idx - 1] == 'X' and grid[idx + 1] == 'X' and grid[idx] == ''
        if found:
            print(f'Seat {idx} between {idx - 1} and {idx + 1} is not taken.')
