import arcade
import numpy as np

from Engine.Nodes.ContentNode import ContentNode
# import Engine.Nodes.ContentNode
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
        self.text_object = arcade.Text(self.text, point[0], point[1], self.color, self.font_size, anchor_x=anchor_x,
                                       anchor_y=anchor_y)

    def render(self) -> None:
        self.text_object.text = self.text
        self.text_object.x = self.point[0]
        self.text_object.y = self.point[1]
        self.text_object.color = self.color
        self.text_object.font_size = self.font_size
        self.text_object.anchor_x = self.anchor_x
        self.text_object.anchor_y = self.anchor_y
        self.text_object.draw()
