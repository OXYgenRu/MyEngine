import arcade
import numpy

from Engine.Nodes.ControlNodes.ControlNode import ControlNode
from Engine.Nodes.Node import Node


class CameraNode(Node):
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0):
        super().__init__(parent_node, render_priority)
        self.arcade_camera: arcade.Camera2D = arcade.Camera2D()

        self.camera_cleaner: CameraCleaner = CameraCleaner(self.application, self)

        self.view_point: numpy.array = numpy.array([self.application.width // 2, self.application.height // 2],
                                                   dtype=float)
        self.zoom: float = 1

        self.camera_control = ControlNode(self)
        self.camera_control.on_mouse_scroll = self.on_mouse_scroll
        self.camera_control.on_mouse_drag = self.on_mouse_drag

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, button: int, modifiers: int):
        if button != 2:
            return
        self.view_point += numpy.array([-dx, -dy], dtype=float) / self.zoom

    def on_mouse_scroll(self, x: float, y: float, scroll_x: float, scroll_y: float):
        if scroll_y < 0:
            self.zoom *= 0.75
            return
        self.zoom /= 0.75

    def render(self) -> None:
        self.arcade_camera.zoom = self.zoom
        self.arcade_camera.position = self.view_point
        self.arcade_camera.use()

    def get_tree(self, flatten_render_tree: list, flatten_update_tree: list, render_flag: bool,
                 update_flag: bool, render_index: int, update_index: int) -> (int, int):
        added_render_index: int = 0
        added_update_index: int = 0
        render_flag = render_flag & self.render_flag
        update_flag = update_flag & self.update_flag

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
            added_update_index += indexes[1]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                indexes: (int, int) = self.nodes[i][j].get_tree(flatten_render_tree, flatten_update_tree, render_flag,
                                                                update_flag,
                                                                render_index + added_render_index,
                                                                update_index + added_update_index)
                added_render_index += indexes[0]
                added_update_index += indexes[1]
        if render_flag:
            if len(flatten_render_tree) == render_index + added_render_index:
                flatten_render_tree.append(None)
            flatten_render_tree[render_index + added_render_index] = self.camera_cleaner
            added_render_index += 1
        if update_flag:
            if len(flatten_update_tree) == update_index + added_update_index:
                flatten_update_tree.append(None)
            flatten_update_tree[update_index + added_update_index] = self.camera_cleaner
            added_update_index += 1
        return added_render_index, added_update_index


class CameraCleaner:
    def __init__(self, application, parent: CameraNode):
        self.camera_cleaned: arcade.Camera2D = arcade.Camera2D()
        self.camera_cleaned.position = numpy.array([application.width // 2, application.height // 2], dtype=float)
        self.parent: CameraNode = parent

    def render(self) -> None:
        self.camera_cleaned.use()

    def update(self, delta_time: float) -> None:
        pass
