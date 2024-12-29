import arcade
import numpy as np

from Engine.Nodes.ContentNode import ContentNode
from Engine.Nodes.Node import Node


class TextNode(ContentNode):
    def __init__(self, parent_node: "Node" = None, text: str = "", point: np.array = np.array([]),
                 color: tuple = (255, 255, 255),
                 font_size=24, anchor_x="center", anchor_y="center"):
        super().__init__(parent_node)
        self.text: str = text
        self.point: np.array = point.astype(float)
        self.color: tuple = color
        self.font_size: int = font_size
        self.anchor_x: str = anchor_x
        self.anchor_y: str = anchor_y

    def render(self) -> None:
        arcade.draw_text(self.text, self.point[0], self.point[1], self.color, self.font_size, 0, anchor_x=self.anchor_x,
                         anchor_y=self.anchor_y)
