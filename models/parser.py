from models.operator import OperatorType
from models.stack import Stack
from models.tree import Node
from abc import ABC, abstractmethod


class Parser(ABC):
    @classmethod
    @abstractmethod
    def can_parse(cls, expression) -> bool:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def parse(cls, expression) -> Node:
        raise NotImplementedError


class PostfixParser(Parser):
    @classmethod
    def can_parse(cls, expression) -> bool:
        if OperatorType.check(expression[0]):
            return False
        return OperatorType.check(expression[-1]) and OperatorType.get(expression[-1]).priority != 0

    @classmethod
    def parse(cls, expression) -> Node:
        if not cls.can_parse(expression):
            raise ValueError('Invalid expression')
        stack = Stack()
        for ch in expression:
            if OperatorType.check(ch):
                right = stack.pop()
                left = stack.pop()
                stack.push(Node(ch, left, right))
            else:
                stack.push(Node(ch))
        root = stack.pop()
        if stack:
            raise ValueError('Invalid expression')
        return root


class PrefixParser(Parser):
    @classmethod
    def can_parse(cls, expression) -> bool:
        if OperatorType.check(expression[-1]):
            return False
        return OperatorType.check(expression[0]) and OperatorType.get(expression[0]).priority != 0

    @classmethod
    def parse(cls, expression) -> Node:
        if not cls.can_parse(expression):
            raise ValueError('Invalid expression')
        stack = Stack()
        for ch in reversed(expression):
            if OperatorType.check(ch):
                left = stack.pop()
                right = stack.pop()
                stack.push(Node(ch, left, right))
            else:
                stack.push(Node(ch))
        root = stack.pop()
        if stack:
            raise ValueError('Invalid expression')
        return root


class InfixParser(Parser):
    @classmethod
    def can_parse(cls, expression) -> bool:
        if (OperatorType.check(expression[0]) and OperatorType.get(expression[0]).priority != 0) or \
                (OperatorType.check(expression[-1]) and OperatorType.get(expression[-1]).priority != 0):
            return False
        return True

    @classmethod
    def parse(cls, expression) -> Node:
        if not cls.can_parse(expression):
            raise ValueError('Invalid expression')
        char_stack = Stack()
        node_stack = Stack()
        for ch in expression:
            if OperatorType.check(ch):
                if OperatorType.get(ch) == OperatorType.OPEN.value:
                    char_stack.push(ch)
                elif OperatorType.get(ch) == OperatorType.CLOSE.value:
                    while char_stack and OperatorType.get(char_stack.top()) != OperatorType.OPEN.value:
                        right = node_stack.pop()
                        left = node_stack.pop()
                        node_stack.push(Node(char_stack.pop(), left, right))
                    char_stack.pop()
                else:
                    while char_stack and OperatorType.get(char_stack.top()) != OperatorType.OPEN and \
                            ((OperatorType.get(char_stack.top()) != OperatorType.POW.value and OperatorType.get(
                                ch).priority <= OperatorType.get(char_stack.top()).priority)
                             or
                             (OperatorType.get(char_stack.top()) == OperatorType.POW.value and OperatorType.get(
                                 ch).priority < OperatorType.get(char_stack.top()).priority)
                            ):
                        right = node_stack.pop()
                        left = node_stack.pop()
                        node_stack.push(Node(char_stack.pop(), left, right))
                    char_stack.push(ch)
            else:
                node_stack.push(Node(ch))
        while char_stack:
            right = node_stack.pop()
            left = node_stack.pop()
            node_stack.push(Node(char_stack.pop(), left, right))
        root = node_stack.pop()
        if node_stack:
            raise ValueError('Invalid expression')
        return root


class AutoParser:
    ALL_PARSERS = [PostfixParser, PrefixParser, InfixParser]

    @classmethod
    def parse(cls, expression) -> Node:
        for parser in cls.ALL_PARSERS:
            if parser.can_parse(expression):
                try:
                    result = parser.parse(expression)
                    return result
                except Exception:
                    continue
        raise ValueError('Invalid expression')
