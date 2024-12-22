from collections import defaultdict
import numpy as np
from typing import Optional

from Engine.Application import Application


class Node:
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0):
        self.nodes: list = []
        self.content: list = []
        self.render_priority: int = render_priority
        self.application: Optional["Application", None] = None

        if parent_node is not None:
            self.application = parent_node.application
            parent_node.add_node(self)
            self.nodes = [] * self.application.node_container_size

    def add_node(self, other: "Node") -> None:
        self.nodes[other.render_priority].append(other)

    def add_content(self, other) -> None:
        self.content.append(other)

    def render(self) -> None:
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                self.nodes[i][j].render()
