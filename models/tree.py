import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

from models.operator import OperatorType


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def is_operator(self) -> bool:
        return OperatorType.check(self.value)

    def infix(self) -> str:
        if self.is_operator:
            return f'({self.left.infix()} {self.value} {self.right.infix()})'
        return self.value

    def postfix(self) -> str:
        if self.is_operator:
            return f'{self.left.postfix()} {self.right.postfix()} {self.value}'
        return self.value

    def prefix(self) -> str:
        if self.is_operator:
            return f'{self.value} {self.left.prefix()} {self.right.prefix()}'
        return self.value

    def get_networkx_graph(self):
        G = nx.Graph()
        G.add_node(self.__hash__(), value=self.value)
        if self.left:
            left_graph = self.left.get_networkx_graph()
            G = nx.compose(G, left_graph)
            G.add_edge(self.__hash__(), self.left.__hash__())
        if self.right:
            right_graph = self.right.get_networkx_graph()
            G = nx.compose(G, right_graph)
            G.add_edge(self.__hash__(), self.right.__hash__())
        return G

    def show(self):
        G = self.get_networkx_graph()
        pos = graphviz_layout(G, prog="dot")
        labels = nx.get_node_attributes(G, 'value')
        nx.draw(G, pos, labels=labels, with_labels=True)
        plt.show()

    def eval(self) -> int:
        if self.is_operator:
            return OperatorType.get(self.value).apply_func(self.left.eval(), self.right.eval())
        try:
            return int(self.value)
        except ValueError:
            raise ValueError('Not evaluable')
