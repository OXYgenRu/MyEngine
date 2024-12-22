from Engine.Application import Application
from Engine.Nodes.Node import Node


class Scene(Node):
    def __init__(self, application: "Application"):
        super().__init__()
        self.application = application
        self.nodes = [[] for _ in range(application.node_container_size)]
