# pylint: disable=missing-docstring


def sudoku_validator(grid):
    expected = set(range(1,10))

    for row in grid:
        if set(row) != expected:
            return False

    for col_index in range(9):
        column = []
        for row_index in range(9):
            column.append(grid[row_index][col_index])

        if set(column) != expected:
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []

            for row_index in range(box_row, box_row + 3):
                for col_index in range(box_col, box_col +3):
                    box.append(grid[row_index][col_index])

            if set(box) != expected:
                return False

    return True
