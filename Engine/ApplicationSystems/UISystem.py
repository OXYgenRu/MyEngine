from typing import Optional

import numpy as np

from Engine.Nodes.CameraNode import CameraCleaner, CameraNode
from Engine.Nodes.UINodes.UIColliderNode import UIColliderNode
import shapely


class UISystem:
    def __init__(self, application):
        self.application = application
        self.flatten_ui_tree: list = []
        self.index: int = 0

    def update(self) -> None:
        index: int = 0
        for i in range(self.application.indexes[1]):
            if isinstance(self.application.flatten_update_tree[i], (UIColliderNode, CameraNode, CameraCleaner)):
                if index == len(self.flatten_ui_tree):
                    self.flatten_ui_tree.append(None)
                self.flatten_ui_tree[index] = self.application.flatten_update_tree[i]
                index += 1
        self.index = index

    def get_collider(self, x: float, y: float):
        pos: np.array = np.array([x, y], dtype=float)

        for i in range(self.index):
            if isinstance(self.flatten_ui_tree[i], UIColliderNode) and self.flatten_ui_tree[i].polygon.contains(
                    shapely.geometry.Point(pos)):
                return self.flatten_ui_tree[i]
            if isinstance(self.flatten_ui_tree[i], CameraCleaner):
                pos = np.array([x, y], dtype=float)
            if isinstance(self.flatten_ui_tree[i], CameraNode):
                pos = (np.array([x, y] - np.array([self.application.width // 2, self.application.height // 2]),
                                dtype=float))
                pos += (self.flatten_ui_tree[i].view_point - np.array(
                    [self.application.width // 2, self.application.height // 2])) * self.flatten_ui_tree[i].zoom
                pos /= self.flatten_ui_tree[i].zoom
                pos += np.array([self.application.width // 2, self.application.height // 2])
                print(pos)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        print(self.get_collider(x, y))

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int) -> None:
        pass
