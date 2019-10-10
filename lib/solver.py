from lib.exceptions import InvalidShapeException
from lib.cell_group import Row, Column, Box
from lib.cell import Cell


class Validator:
    def __init__(self, cell_array):
        self.row_array = []
        self.column_array = []
        self.box_array = []

        # Shape validation. Accept only proper array
        if len(cell_array) != 9:
            raise InvalidShapeException()
        for row in cell_array:
            if len(row) != 9:
                raise InvalidShapeException()

        # Create CellGroups first. Assign them to cell later
        for i in range(0, 9):
            self.row_array.append(Row(i))
            self.column_array.append(Column(i))
            self.box_array.append(Box(i))

        # Assign CellGroup to Cell and store for retrieval
        idx = 0
        for row in cell_array:
            col_idx = 0
            for cell in row:
                box_idx = (col_idx % 3) + 3 * (idx % 3)
                cell = Cell(
                    row=self.row_array[idx],
                    column=self.column_array[col_idx],
                    box=self.box_array[box_idx],
                    value=cell
                )
                self.row_array[idx].assign_cell(cell)
                self.column_array[col_idx].assign_cell(cell)
                self.box_array[box_idx].assign_cell(cell)
                col_idx += 1
            idx += 1
