import os
import sys

from conans import ConanFile, CMake, tools


class OpenSubdivConan(ConanFile):
    name = "OpenSubdiv"
    version = "3.4.3"
    license = "Apache-2.0"
    author = "Jan Honsbrok jan.honsbrok@gmail.com"
    url = "https://github.com/Latios96/conan-OpenSubdiv"
    description = "An Open-Source subdivision surface library"
    topics = ("cgi", "vfx", "subdivision surface")
    settings = "os", "compiler", "build_type", "arch"
    options = {"with_tbb": [True, False], "no_opengl": [True, False]}
    default_options = {"with_tbb": True,"no_opengl": False}
    generators = "cmake"

    requires = ()

    def requirements(self):
        if self.options.with_tbb:
            self.requires("tbb/2020.2")

    @property
    def version_with_underscore(self):
        return self.version.replace(".", "_")

    def source(self):
        tools.get(
            "https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v{}.zip".format(
                self.version_with_underscore
            )
        )

    def _configure_cmake(self):
        os.environ.update(
            {"TBB_LOCATION": self.deps_cpp_info["tbb"].rootpath,}
        )
        cmake = CMake(self)
        cmake.definitions["NO_TBB"] = not self.options.with_tbb
        cmake.definitions["NO_EXAMPLES"] = True
        cmake.definitions["NO_TUTORIALS"] = True
        cmake.definitions["NO_REGRESSION"] = True

        cmake.definitions["NO_TBB"] = True
        cmake.definitions["NO_OMP"] = True
        cmake.definitions["NO_CUDA"] = True
        cmake.definitions["NO_PTEX"] = True
        cmake.definitions["NO_DOC"] = True
        cmake.definitions["NO_CLEW"] = True
        cmake.definitions["NO_OPENCL"] = True
        cmake.definitions["NO_OPENGL"] = self.options.no_opengl

        cmake.configure(
            source_folder="OpenSubdiv-{}".format(self.version_with_underscore)
        )
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["osdCPU", "osdGPU"]

    def imports(self):
        self.copy("*.dll", "", "bin")
        self.copy("*.dylib", "", "lib")
