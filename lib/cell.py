from lib.exceptions import InvalidValueException, RefillWarning


class Cell:
    def __init__(self, row, column, box, value=None):
        self.row = row
        self.column = column
        self.box = box
        self.filled = False
        self.possible_values = list(range(1, 10))
        if value is not None:
            self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.row.value_array.remove(value)
            self.column.value_array.remove(value)
            self.box.value_array.remove(value)
            self.possible_values.remove(value)
        except ValueError:
            raise InvalidValueException(row=self.row._idx, column=self.column._idx, value=value)

        if not self.filled:
            self.filled = True
        else:
            raise RefillWarning(row=self.row._idx,
                                column=self.column._idx,
                                value=value,
                                old_value=self.value)
        self.__value = value
