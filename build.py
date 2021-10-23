import sys

from cpt.packager import ConanMultiPackager


def skip_if_windows(build):
    if sys.platform != "win32":
        return False
    return build.settings['build_type'] and build.settings[
        'compiler.runtime'].startswith("MT")


if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86_64"],visual_versions=[16], gcc_versions=[9], apple_clang_versions=[12.0])
    builder.add_common_builds()
    builder.build_policy = "missing"
    builder.remove_build_if(lambda build: skip_if_windows(build))
    builder.run()
