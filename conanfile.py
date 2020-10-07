from conans import ConanFile, CMake, tools


class OpenSubdivConan(ConanFile):
    name = "OpenSubdiv"
    version = "3.4.3"
    license = "<Put the package license here>"
    author = "Jan Honsbrok jan.honsbrok@gmail.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "An Open-Source subdivision surface library"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    requires = (
    )

    @property
    def version_with_underscore(self):
        return self.version.replace(".", "_")

    def source(self):
        tools.get("https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v{}.zip".format(self.version_with_underscore))

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="OpenSubdiv-{}".format(self.version_with_underscore))
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [
            "osdCPU",
            "osdGPU"]

    def imports(self):
        self.copy("*.dll", "", "bin")
        self.copy("*.dylib", "", "lib")
