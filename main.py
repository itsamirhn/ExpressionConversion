from models.parser import AutoParser
from models.operator import OperatorType


def normalize_expression(expression):
    for operator in OperatorType:
        value = operator.value.value
        expression = expression.replace(value, f' {value} ')
    expression = ' '.join(expression.split())
    return expression.split()


def main():
    expression = input("Enter an expression: ")
    expression = normalize_expression(expression)

    try:
        tree = AutoParser.parse(expression)
        print("Infix: {}".format(tree.infix()))
        print("Prefix: {}".format(tree.prefix()))
        print("Postfix: {}".format(tree.postfix()))
        try:
            print("Eval: {}".format(tree.eval()))
        except ValueError:
            print("Not evaluable")
        tree.show()
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
