from Engine.Nodes.Node import Node


class PolygonNode(Node):
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0,):
        super().__init__(parent_node, render_priority)

