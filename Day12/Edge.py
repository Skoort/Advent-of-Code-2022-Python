from Day12.Node import Node


class Edge:
    def __init__(self, node_from: Node, node_to: Node, cost: int):
        self.node_from = node_from
        self.node_to = node_to
        self.cost = cost