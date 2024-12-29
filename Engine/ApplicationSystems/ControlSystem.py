from Engine.Nodes.ControlNodes.ControlNode import ControlNode


class ControlSystem:
    def __init__(self, application):
        self.application = application
        self.flatten_control_tree: list = []
        self.index: int = 0

    def update(self):
        index: int = 0
        for i in range(self.application.indexes[1]):
            if isinstance(self.application.flatten_update_tree[i], ControlNode):
                if index == len(self.flatten_control_tree):
                    self.flatten_control_tree.append(None)
                self.flatten_control_tree[index] = self.application.flatten_update_tree[i]
                index += 1

    def on_key_press(self, symbol: int, modifiers: int):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_key_release(symbol, modifiers)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, button: int, modifiers: int):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_mouse_drag(x, y, dx, dy, button, modifiers)

    def on_mouse_scroll(self, x: float, y: float, scroll_x: float, scroll_y: float):
        for i in range(len(self.flatten_control_tree)):
            self.flatten_control_tree[i].on_mouse_scroll(x, y, scroll_x, scroll_y)
