from Engine.Nodes.ContentNode import ContentNode
from Engine.Nodes.Node import Node


class ControlNode(ContentNode):
    def __init__(self, parent_node: "Node" = None):
        super().__init__(parent_node)

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, button: int, modifiers: int):
        pass

    def on_mouse_scroll(self, x: float, y: float, scroll_x: float, scroll_y: float):
        pass
