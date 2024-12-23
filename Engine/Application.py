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

        self.scene_system: SceneSystem = SceneSystem(self)

    def set_node_container_size(self, new_node_container_size: int) -> None:
        if new_node_container_size <= 0:
            raise ValueError(f"New node container size must be greater than 0, got {new_node_container_size}")
        self.node_container_size = new_node_container_size

    def on_draw(self) -> None:
        arcade.start_render()
        self.scene_system.active_scene.render()
        arcade.finish_render()
