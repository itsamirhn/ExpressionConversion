# Just for educational purposes, not used in the project
from models.operator import OperatorType
from models.stack import Stack


def infix_to_postfix(expression):
    """
    >>> infix_to_postfix('1 + 2')
    '1 2 +'
    >>> infix_to_postfix('1 + 2 * 3')
    '1 2 3 * +'
    >>> infix_to_postfix('1 * 2 + 3')
    '1 2 * 3 +'
    >>> infix_to_postfix('2 ^ 3 ^ 4')
    '2 3 4 ^ ^'
    >>> infix_to_postfix('( 2 ^ 3 ) ^ 4')
    '2 3 ^ 4 ^'
    >>> infix_to_postfix('2 ^ ( 3 ^ 4 )')
    '2 3 4 ^ ^'
    >>> infix_to_postfix('2 ^ 3 * 4')
    '2 3 ^ 4 *'
    >>> infix_to_postfix('2 * 3 ^ 4')
    '2 3 4 ^ *'
    """
    expression = expression.split()
    stack = Stack()
    postfix = []
    for ch in expression:
        if OperatorType.check(ch):
            if OperatorType.get(ch) == OperatorType.OPEN.value:
                stack.push(ch)
            elif OperatorType.get(ch) == OperatorType.CLOSE.value:
                while OperatorType.get(stack.top()) != OperatorType.OPEN.value:
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and \
                    ((OperatorType.get(stack.top()) != OperatorType.POW.value and OperatorType.get(stack.top()).priority >= OperatorType.get(ch).priority)
                     or
                     (OperatorType.get(stack.top()) == OperatorType.POW.value and OperatorType.get(stack.top()).priority > OperatorType.get(ch).priority)):
                    postfix.append(stack.pop())
                stack.push(ch)
        else:
            postfix.append(ch)
    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)


def postfix_to_infix(expression):
    """
    >>> postfix_to_infix('1 2 +')
    '(1 + 2)'
    >>> postfix_to_infix('1 2 3 * +')
    '(1 + (2 * 3))'
    >>> postfix_to_infix('1 2 * 3 +')
    '((1 * 2) + 3)'
    >>> postfix_to_infix('2 3 4 ^ ^')
    '(2 ^ (3 ^ 4))'
    >>> postfix_to_infix('2 3 ^ 4 ^')
    '((2 ^ 3) ^ 4)'
    """
    expression = expression.split()
    stack = Stack()
    for ch in expression:
        if OperatorType.check(ch):
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(f'({op1} {ch} {op2})')
        else:
            stack.push(ch)
    return stack.pop()


def infix_to_prefix(expression):
    """
    # >>> infix_to_prefix('1 + 2')
    # '+ 1 2'
    # >>> infix_to_prefix('1 + 2 * 3')
    # '+ 1 * 2 3'
    # >>> infix_to_prefix('1 * 2 + 3')
    # '+ * 1 2 3'
    >>> infix_to_prefix('2 ^ 3 ^ 4')
    '^ 2 ^ 3 4'
    >>> infix_to_prefix('( 2 ^ 3 ) ^ 4')
    '^ ^ 2 3 4'
    >>> infix_to_prefix('2 ^ ( 3 ^ 4 )')
    '^ 2 ^ 3 4'
    >>> infix_to_prefix('2 ^ 3 * 4')
    '* ^ 2 3 4'
    >>> infix_to_prefix('2 * 3 ^ 4')
    '* 2 ^ 3 4'
    """
    expression = expression.split()
    stack = Stack()
    prefix = []
    for ch in expression[::-1]:
        if OperatorType.check(ch):
            if OperatorType.get(ch) == OperatorType.CLOSE.value:
                stack.push(ch)
            elif OperatorType.get(ch) == OperatorType.OPEN.value:
                while OperatorType.get(stack.top()) != OperatorType.CLOSE.value:
                    prefix.append(stack.pop())
                stack.pop()
            else:
                while stack and \
                    ((OperatorType.get(stack.top()) != OperatorType.POW.value and OperatorType.get(stack.top()).priority > OperatorType.get(ch).priority)
                     or
                     (OperatorType.get(stack.top()) == OperatorType.POW.value and OperatorType.get(stack.top()).priority >= OperatorType.get(ch).priority)):
                    prefix.append(stack.pop())
                stack.push(ch)
        else:
            prefix.append(ch)
    while stack:
        prefix.append(stack.pop())
    return ' '.join(prefix[::-1])


def prefix_to_infix(expression):
    """
    >>> prefix_to_infix('+ 1 2')
    '(1 + 2)'
    >>> prefix_to_infix('+ 1 * 2 3')
    '(1 + (2 * 3))'
    >>> prefix_to_infix('+ * 1 2 3')
    '((1 * 2) + 3)'
    >>> prefix_to_infix('^ 2 ^ 3 4')
    '(2 ^ (3 ^ 4))'
    >>> prefix_to_infix('^ ^ 2 3 4')
    '((2 ^ 3) ^ 4)'
    """
    expression = expression.split()
    stack = Stack()
    for ch in expression[::-1]:
        if OperatorType.check(ch):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(f'({op1} {ch} {op2})')
        else:
            stack.push(ch)
    return stack.pop()


def postfix_to_prefix(expression):
    """
    >>> postfix_to_prefix('1 2 +')
    '+ 1 2'
    >>> postfix_to_prefix('1 2 3 * +')
    '+ 1 * 2 3'
    >>> postfix_to_prefix('1 2 * 3 +')
    '+ * 1 2 3'
    >>> postfix_to_prefix('2 3 4 ^ ^')
    '^ 2 ^ 3 4'
    >>> postfix_to_prefix('2 3 ^ 4 ^')
    '^ ^ 2 3 4'
    """
    expression = expression.split()
    stack = Stack()
    for ch in expression:
        if OperatorType.check(ch):
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(f'{ch} {op1} {op2}')
        else:
            stack.push(ch)
    return stack.pop()


def prefix_to_postfix(expression):
    """
    >>> prefix_to_postfix('+ 1 2')
    '1 2 +'
    >>> prefix_to_postfix('+ 1 * 2 3')
    '1 2 3 * +'
    >>> prefix_to_postfix('+ * 1 2 3')
    '1 2 * 3 +'
    >>> prefix_to_postfix('^ 2 ^ 3 4')
    '2 3 4 ^ ^'
    >>> prefix_to_postfix('^ ^ 2 3 4')
    '2 3 ^ 4 ^'
    """
    expression = expression.split()
    stack = Stack()
    for ch in expression[::-1]:
        if OperatorType.check(ch):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(f'{op1} {op2} {ch}')
        else:
            stack.push(ch)
    return stack.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()