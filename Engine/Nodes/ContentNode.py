from typing import Optional

from Engine.Application import Application
from Engine.Nodes.Node import Node


class ContentNode:
    def __init__(self, parent_node: "Node" = None):
        self.application: Optional["Application", None] = None

        if parent_node is not None:
            self.application = parent_node.application
            parent_node.add_content(self)

    def render(self):
        pass

    def update(self, delta_time: float):
        pass
        print("ContentNode")

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
        return added_render_index, added_update_index
