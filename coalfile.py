from coal import CoalFile
from util import cp, git_clone, cd, patch
from os import path

class ImguiFile(CoalFile):
    url = "https://github.com/ocornut/imgui.git"
    exports = ["include", "src"]

    def prepare(self):
        git_clone(self.url, 'master', 'repo')
        if "patch" in self.options:
            with cd('repo/'):
                patch(self.options["patch"])
    def package(self):
        cp('repo/*.h', 'include/')
        cp('repo/*.cpp', 'src/')
    def info(self, generator):
        generator.add_include_dir('include/')
        generator.add_source_files('src/imgui.cpp', 'src/imgui_draw.cpp')
