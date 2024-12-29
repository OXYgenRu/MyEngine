from Engine.Nodes.ContentNode import ContentNode
from Engine.Nodes.Node import Node
import numpy as np
import arcade


class PolygonNode(ContentNode):
    def __init__(self, parent_node: "Node" = None, points: np.array = np.array([]),
                 width: int = 0, color: tuple = (255, 255, 255)):
        super().__init__(parent_node)
        self.points: np.array = points.astype(float)
        self.width: int = width
        self.color: tuple = color

    def render(self) -> None:
        if self.width == 0:
            arcade.draw_polygon_filled(self.points.tolist(), self.color)
        else:
            arcade.draw_polygon_outline(self.points.tolist(), self.color, self.width)


class CircleNode(ContentNode):
    def __init__(self, parent_node: "Node" = None, point: np.array = np.array([]), radius: int = 0, width: int = 0,
                 color: tuple = (255, 255, 255)):
        super().__init__(parent_node)
        self.point: np.array = point.astype(float)
        self.radius: int = radius
        self.width: int = width
        self.color: tuple = color

    def render(self) -> None:
        if self.width == 0:
            arcade.draw_circle_filled(self.point[0], self.point[1], self.radius, self.color)
        else:
            arcade.draw_circle_outline(self.point[0], self.point[1], self.radius, self.color, self.width)
