from Engine.Nodes.ContentNode import ContentNode
from Engine.Nodes.Node import Node
import numpy as np
import arcade


class PolygonNode(ContentNode):
    def __init__(self, parent_node: "Node" = None, points: np.array = np.array([]),
                 width: int = 0, color: tuple = (255, 255, 255)):
        super().__init__(parent_node)
        self.points: np.array = points
        self.width: int = width
        self.color: tuple = color

    def render(self):
        if self.width == 0:
            arcade.draw_polygon_filled(self.points.tolist(), self.color)
        else:
            arcade.draw_polygon_outline(self.points.tolist(), self.color, self.width)
