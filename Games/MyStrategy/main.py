import arcade
import numpy
import numpy as np

from Engine.Application import Application
from Engine.GameScene import Scene
from Engine.Nodes.CameraNode import CameraNode
from Engine.Nodes.ControlNodes.ControlNode import ControlNode
from Engine.Nodes.Node import Node
from Engine.Nodes.RenderNodes.Shapes import PolygonNode, CircleNode
from Engine.Nodes.RenderNodes.Text import TextNode


class Node1(Node):
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0):
        super().__init__(parent_node, render_priority)
        print("setup2")


class ControlTest(Scene):
    def __init__(self, application: "Application"):
        super().__init__(application)
        self.control_node = ControlNode(self)
        self.polygon = PolygonNode(self, numpy.array([[100, 100], [200, 100], [200, 200], [100, 200]]), 0)
        self.control_node.on_key_release = self.on_key_release
        self.control_node.on_mouse_drag = self.on_mouse_drag

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.polygon.points += numpy.array([100, 0])

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, button: int, modifiers: int):
        print(f"drag mouse from {x} {y} on {dx} {dy}, button {button}")


class ShapesTest(Scene):
    def __init__(self, application: "Application"):
        super().__init__(application)
        print("setup")
        self.camera = CameraNode(self)
        self.camera_control = ControlNode(self)
        self.polygon = PolygonNode(self.camera, numpy.array([[100, 100], [200, 100], [200, 200], [100, 200]]), 0)
        self.node1 = Node(self.camera)
        self.circle = CircleNode(self.node1, np.array([700, 400]), radius=50, color=(0, 255, 0), width=2)
        self.node2 = Node(self.camera)
        self.text = TextNode(self.node2, "скибиди доб доб ес ес", point=np.array([700, 100]))
        self.node3 = Node(self, render_priority=1)
        self.text_ui = TextNode(self.node3, "скибиди доб доб ес ес", point=np.array([200, 100]), color=(255, 125, 125))

    def update(self, delta_time: float):
        # print(1 / delta_time)
        pass

if __name__ == "__main__":
    game = Application((1280, 720), __file__)
    game.scene_system.register_scene(ShapesTest, "1")
    game.scene_system.register_scene(ControlTest, "2")
    game.scene_system.set_new_scene("1")
    print(game.game_folder)
    game.run()
