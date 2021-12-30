# author: myc

import os
import importlib

from utils.file import get_files


class PluginLoader:
    def __init__(self, root_path, plugin_dir, plugin_ext=".py"):
        self.root_path = root_path
        self.plugin_dir = plugin_dir
        self.plugin_ext = plugin_ext

    def find_plugin(self):
        plugin_name = []
        path = os.path.normpath(self.get_plugin_dir())
        plugins = get_files(path)
        if plugins:
            for plugin in plugins:
                if plugin.endswith(self.plugin_ext) and "__" not in plugin:
                    name = self.plugin_dir + plugin[:-3].replace(path, "").replace("/", ".")
                    plugin_name.append(name)
        return plugin_name

    def load_plugin(self, keyword=""):
        module = []
        plugins = self.find_plugin()
        for plugin in plugins:
            if keyword in plugin:
                m = importlib.import_module(plugin)
                module.append(m)
        return module

    def get_plugin_dir(self):
        return os.path.join(self.root_path, self.plugin_dir)
