from Engine.Application import Application
from Engine.GameScene import Scene
from Engine.Nodes.Node import Node


class Node1(Node):
    def __init__(self, parent_node: "Node" = None, render_priority: int = 0):
        super().__init__(parent_node, render_priority)
        print("setup2")


class MainScene(Scene):
    def __init__(self, application: "Application"):
        super().__init__(application)
        print("setup")
        self.node1 = Node1(self, 0)
        print(self.nodes)


if __name__ == "__main__":
    game = Application((1280, 720), __file__)
    game.register_scene(MainScene, "1")
    game.set_new_scene('1')
    game.run()
