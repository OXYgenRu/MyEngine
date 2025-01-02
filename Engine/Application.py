import os.path
from collections import defaultdict
from typing import Optional

import arcade

from Engine.ApplicationSystems.ControlSystem import ControlSystem
from Engine.ApplicationSystems.SceneSystem import SceneSystem
from Engine.ApplicationSystems.UISystem import UISystem


class Application(arcade.Window):
    def __init__(self, window_size: tuple, init_file: str):
        super().__init__(window_size[0], window_size[1], "Mygame")
        self.game_folder: str = os.path.dirname(init_file)
        self.window_size: tuple = window_size
        self.node_container_size: int = 10

        self.flatten_render_tree: list = []
        self.flatten_update_tree: list = []
        self.indexes: (int, int) = (0, 0)
        self.scene_system: SceneSystem = SceneSystem(self)
        self.control_system: ControlSystem = ControlSystem(self)
        self.ui_system: UISystem = UISystem(self)

        self.set_update_rate(0.006)

    def set_node_container_size(self, new_node_container_size: int) -> None:
        if new_node_container_size <= 0:
            raise ValueError(f"New node container size must be greater than 0, got {new_node_container_size}")
        self.node_container_size = new_node_container_size

    def on_draw(self) -> None:
        self.clear()
        for i in range(self.indexes[0]):
            self.flatten_render_tree[i].render()

    def on_update(self, delta_time: float) -> None:
        self.indexes = self.scene_system.active_scene.get_tree(self.flatten_render_tree,
                                                               self.flatten_update_tree, True,
                                                               True, 0, 0)
        self.control_system.update()
        self.ui_system.update()

        for i in range(self.indexes[1]):
            self.flatten_update_tree[i].update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.control_system.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.control_system.on_key_release(symbol, modifiers)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        self.control_system.on_mouse_press(x, y, button, modifiers)
        self.ui_system.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> None:
        self.control_system.on_mouse_release(x, y, button, modifiers)
        self.ui_system.on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        self.control_system.on_mouse_motion(x, y, dx, dy)
        self.ui_system.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, button: int, modifiers: int) -> None:
        self.control_system.on_mouse_drag(x, y, dx, dy, button, modifiers)

    def on_mouse_scroll(self, x: float, y: float, scroll_x: float, scroll_y: float) -> None:
        self.control_system.on_mouse_scroll(x, y, scroll_x, scroll_y)
