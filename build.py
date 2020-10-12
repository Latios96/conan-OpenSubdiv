import sys

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86_64"])
    builder.add_common_builds()
    builder.build_policy = "missing"
    builder.remove_build_if(
        lambda build: build.options["OpenSubdiv:shared"] == True and sys.platform == "win32")
    builder.run()
