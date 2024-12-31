import numpy

from Engine.Nodes.ContentNode import ContentNode
from Engine.Nodes.Node import Node
import shapely


class UIColliderNode(ContentNode):
    def __init__(self, parent_node: "Node" = None, points: numpy.array = numpy.array([])):
        super().__init__(parent_node)
        self.points: numpy.array = points
        self.polygon = shapely.geometry.Polygon(self.points)

    def on_mouse_press(self, button: int, modifiers: int):
        pass

    def on_mouse_release(self, button: int, modifiers: int):
        pass
