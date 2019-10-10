from lib.cell import Cell


class CellGroup:
    def __init__(self, idx: int):
        self._idx = idx
        self.value_array = list(range(1, 10))
        self.cell_array = []

    def assign_cell(self, cell: Cell):
        self.cell_array.append(cell)


class Row(CellGroup):
    def __init__(self, idx: int):
        super().__init__(idx)


class Column(CellGroup):
    def __init__(self, idx: int):
        super().__init__(idx)


class Box(CellGroup):
    def __init__(self, idx: int):
        super().__init__(idx)
