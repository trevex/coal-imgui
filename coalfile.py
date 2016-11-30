from coal import CoalFile
from util import cp, git_clone, cd, patch
from os import path

class ImguiFile(CoalFile):
    repo = "https://github.com/ocornut/imgui.git"
    url = "https://github.com/ocornut/imgui/archive/v%s.zip"
    zipfile = "imgui.zip"
    exports = ["include", "src"]
    def prepare(self):
        if "version" in self.settings:
            version = self.settings["version"]
            download(self.url % version, self.zipfile)
            unzip(self.zipfile, 'temp')
        else:
            git_clone(self.repo, 'master', 'repo')
        if "patch" in self.settings:
            with cd('repo/'):
                patch(self.settings["patch"])
    def package(self):
        cp('repo/*.h', 'include/')
        cp('repo/*.cpp', 'src/')
        cp('temp/imgui/*.h', 'include/')
        cp('temp/imgui/*.cpp', 'src/')
    def info(self, generator):
        generator.add_include_dir('include/')
        generator.add_source_files('src/imgui.cpp', 'src/imgui_draw.cpp')
