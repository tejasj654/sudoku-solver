# from lib.solver import Row, Column

ERROR_CODES = {
    'SHAPE_ERROR': "Invalid shape for the input values. Input shape should be (9X9)",
    'VALUE_ERROR': "Conflicting values found in the problem",
    'SOLVE_ERROR': "Encountered an error while solving. The problem might be incorrect",
    'OVERFLOW_ERROR': "Exceeded maximum steps required to solve the problem"
}


class SolverException(Exception):
    def __init__(self):
        raise Exception


class InvalidShapeException(SolverException):
    def __init__(self):
        print(ERROR_CODES['SHAPE_ERROR'])
        raise SolverException


class InvalidValueException(SolverException):
    def __init__(self, row: int, column: int, value: None):
        print(f'{ERROR_CODES["VALUE_ERROR"]} at {row} row and {column} column with ',
              f'value {value}')
        raise SolverException


class RefillWarning(SolverException):
    def __init__(self, row: int, column: int, value: None, old_value: None):
        print(f'Refill for value at {row} row and {column} column with ',
              f'value {value} and old_value {old_value}')
        pass