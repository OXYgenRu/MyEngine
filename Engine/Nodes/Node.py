from collections import defaultdict
import numpy as np
from typing import Optional

from Engine.Application import Application


class Node:
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0):
        self.nodes: list = []
        self.content: list = []
        self.render_priority: int = render_priority
        self.application: Optional["Application", None] = None

        if parent_node is not None:
            self.application = parent_node.application
            parent_node.add_node(self)
            self.nodes = [[] for _ in range(self.application.node_container_size)]

    def add_node(self, other: "Node") -> None:
        self.nodes[other.render_priority].append(other)

    def add_content(self, other) -> None:
        self.content.append(other)

    def render(self) -> None:
        pass

    def update(self, delta_time: float):
        pass
        print("Node")

    def get_tree(self, flatten_render_tree: list, flatten_update_tree: list, render_flag: bool,
                 update_flag: bool, render_index: int, update_index: int) -> (int, int):
        added_render_index: int = 0
        added_update_index: int = 0

        if render_flag:
            if len(flatten_render_tree) == render_index + added_render_index:
                flatten_render_tree.append(None)
            flatten_render_tree[render_index + added_render_index] = self
            added_render_index += 1
        if update_flag:
            if len(flatten_update_tree) == update_index + added_update_index:
                flatten_update_tree.append(None)
            flatten_update_tree[update_index + added_update_index] = self
            added_update_index += 1

        for i in range(len(self.content)):
            indexes: (int, int) = self.content[i].get_tree(flatten_render_tree, flatten_update_tree, render_flag,
                                                           update_flag,
                                                           render_index + added_render_index,
                                                           update_index + added_update_index)
            added_render_index += indexes[0]
            added_update_index += indexes[0]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                indexes: (int, int) = self.nodes[i][j].get_tree(flatten_render_tree, flatten_update_tree, render_flag,
                                                                update_flag,
                                                                render_index + added_render_index,
                                                                update_index + added_update_index)
                added_render_index += indexes[0]
                added_update_index += indexes[0]
        return added_render_index, added_update_index
