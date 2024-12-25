import os.path
from collections import defaultdict
from typing import Optional

import arcade

from Engine.ApplicationSystems.SceneSystem import SceneSystem


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

        # self.set_update_rate(2)

    def set_node_container_size(self, new_node_container_size: int) -> None:
        if new_node_container_size <= 0:
            raise ValueError(f"New node container size must be greater than 0, got {new_node_container_size}")
        self.node_container_size = new_node_container_size

    def on_draw(self) -> None:
        arcade.start_render()
        for i in range(self.indexes[0]):
            self.flatten_update_tree[i].render()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.indexes = self.scene_system.active_scene.get_tree(self.flatten_render_tree,
                                                               self.flatten_update_tree, True,
                                                               True, 0, 0)
        for i in range(self.indexes[1]):
            self.flatten_update_tree[i].update(delta_time)
