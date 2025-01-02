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
from Engine.Nodes.UINodes.UIColliderNode import UIColliderNode


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
        self.map_collider = UIColliderNode(self.camera, self.polygon.points)
        self.map_polygon = PolygonNode(self, numpy.array(
            [[100 + 700, 100], [200 + 700, 100], [200 + 700, 200], [100 + 700, 200]]), 0, color=(255, 255, 0))
        self.ui_collider = UIColliderNode(self, self.map_polygon.points)
        self.ui_collider.on_mouse_release = self.ui_collider_method
        self.map_collider.on_mouse_release = self.map_collider_method

    def map_collider_method(self, button, modifiers):
        print("map")

    def ui_collider_method(self, button, modifiers):
        print("ui")

    def update(self, delta_time: float):
        # print(1 / delta_time)
        pass


class UITest(Scene):
    def __init__(self, application: "Application"):
        super().__init__(application)
        self.ui_node = Node(self, 1)
        self.ui_polygon = PolygonNode(self.ui_node, numpy.array([[0, 0], [0, 200], [200, 200], [200, 0]]), 0)
        self.ui_text = TextNode(self.ui_node, "ui_polygon", np.array([100, 100]), color=(125, 255, 0))
        self.ui_collider = UIColliderNode(self.ui_node, points=self.ui_polygon.points)
        self.ui_collider.on_mouse_release = self.click_ui

        self.camera = CameraNode(self)
        self.map_polygon = PolygonNode(self.camera, np.array([[300, 300], [300, 700], [800, 700], [800, 300]]),
                                       color=(0, 255, 255))
        self.map_text = TextNode(self.camera, "map_polygon", np.array([550, 500]), color=(0, 0, 0))
        self.map_collider = UIColliderNode(self.camera, points=self.map_polygon.points)
        self.map_collider.on_mouse_release = self.click_map

    def click_map(self, button, modifiers):
        print("you clicked map")

    def click_ui(self, button, modifiers):
        print("you clicked ui")


if __name__ == "__main__":
    game = Application((1280, 720), __file__)
    game.scene_system.register_scene(ShapesTest, "1")
    game.scene_system.register_scene(ControlTest, "2")
    game.scene_system.register_scene(UITest, "3")
    game.scene_system.set_new_scene("3")
    print(game.game_folder)
    game.run()
