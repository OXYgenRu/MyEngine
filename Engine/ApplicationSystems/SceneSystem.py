from collections import defaultdict


class SceneSystem:
    def __init__(self, application):
        self.scene_storage: defaultdict = defaultdict()
        self.loaded_scene_storage: defaultdict = defaultdict()
        self.active_scene = None
        self.application = application
        self.update_tree_flag: bool = False

    def register_scene(self, scene_class, scene_id) -> None:
        self.scene_storage[scene_id] = scene_class

    def set_new_scene(self, scene_id) -> None:
        self.active_scene = self.scene_storage[scene_id](self.application)
        self.loaded_scene_storage[scene_id] = self.active_scene
        self.update_tree_flag = True
        self.application.indexes = self.active_scene.get_tree(self.application.flatten_render_tree,
                                                              self.application.flatten_update_tree, True,
                                                              True, 0, 0)

    def set_loaded_scene(self, scene_id) -> None:
        self.active_scene = self.loaded_scene_storage[scene_id]
        self.update_tree_flag = True
        self.application.indexes = self.active_scene.get_tree(self.application.flatten_render_tree,
                                                              self.application.flatten_update_tree, True,
                                                              True, 0, 0)
