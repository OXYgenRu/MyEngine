from typing import Optional

from Engine.Application import Application
from Engine.Nodes.Node import Node


class ContentNode:
    def __init__(self, parent_node: "Node" = None):
        self.application: Optional["Application", None] = None

        if parent_node is not None:
            self.application = parent_node.application
            parent_node.add_content(self)

    def render(self):
        pass
