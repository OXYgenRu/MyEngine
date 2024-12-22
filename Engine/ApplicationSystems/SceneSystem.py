from collections import defaultdict


class SceneSystem:
    def __init__(self):
        self.scene_storage: defaultdict = defaultdict()
        self.loaded_scene_storage: defaultdict = defaultdict()
        self.active_scene = None

    def register_scene(self, scene_class, scene_id):
        self.scene_storage[scene_id] = scene_class

    def set_new_scene(self, scene_id) -> None:
        self.active_scene = self.scene_storage[scene_id](self)
        self.loaded_scene_storage[scene_id] = self.active_scene

    def set_loaded_scene(self, scene_id) -> None:
        self.active_scene = self.loaded_scene_storage[scene_id]
