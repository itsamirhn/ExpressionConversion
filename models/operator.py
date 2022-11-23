from enum import Enum


class Operator:
    def __init__(self, value, priority, apply_func):
        self.value = value
        self.priority = priority
        self.apply_func = apply_func


class OperatorType(Enum):
    ADD = Operator('+', 1, lambda x, y: x + y)
    SUB = Operator('-', 1, lambda x, y: x - y)
    MUL = Operator('*', 2, lambda x, y: x * y)
    DIV = Operator('/', 2, lambda x, y: x / y)
    POW = Operator('^', 3, lambda x, y: x ** y)
    OPEN = Operator('(', 0, None)
    CLOSE = Operator(')', 0, None)

    @classmethod
    def check(cls, value):
        for op in cls:
            if op.value.value == value:
                return True
        return False

    @classmethod
    def get(cls, value):
        for op in cls:
            if op.value.value == value:
                return op.value
        raise ValueError('Invalid operator')
