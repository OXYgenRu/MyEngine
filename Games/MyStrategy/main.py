import numpy
import numpy as np

from Engine.Application import Application
from Engine.GameScene import Scene
from Engine.Nodes.Node import Node
from Engine.Nodes.RenderNodes.Shapes import PolygonNode, CircleNode
from Engine.Nodes.RenderNodes.Text import TextNode


class Node1(Node):
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0):
        super().__init__(parent_node, render_priority)
        print("setup2")


class ShapesTest(Scene):
    def __init__(self, application: "Application"):
        super().__init__(application)
        print("setup")
        self.polygon = PolygonNode(self, numpy.array([[100, 100], [200, 100], [200, 200], [100, 200]]), 0)
        self.circle = CircleNode(self, np.array([700, 400]), radius=50, color=(0, 255, 0), width=2)
        self.text = TextNode(self, "скибиди доб доб ес ес", point=np.array([700, 100]))


if __name__ == "__main__":
    game = Application((1280, 720), __file__)
    game.scene_system.register_scene(ShapesTest, "1")
    game.scene_system.set_new_scene("1")
    game.run()
