from lib.solver import Validator


cell_array = [
    [0, 0, 0, 1, 0, 0, 2, 0, 0],
    [0, 0, 0, 2, 0, 0, 3, 0, 0],
    [0, 0, 0, 3, 0, 0, 4, 0, 0],
    [0, 0, 0, 4, 0, 0, 5, 0, 0],
    [0, 0, 0, 5, 0, 0, 6, 0, 0],
    [0, 0, 0, 6, 0, 0, 7, 0, 0],
    [0, 0, 0, 7, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 0, 0, 9, 0, 0],
    [0, 0, 0, 9, 0, 0, 1, 0, 0]
]

actual_cell_array = []

for row in cell_array:
    actual_cell_array.append([x if x != 0 else None for x in row])

Validator(actual_cell_array)
