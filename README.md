# Conan recipe for OpenSubdiv

[OpenSubdiv](https://github.com/PixarAnimationStudios/OpenSubdiv) is a library for subdivision surfaces. 

The and prebuild binaries can be found on [Bintray](https://bintray.com/beta/#/latios96/my_conan/OpenSubdiv:latios96?tab=overview).

## How to use
You need to add my Bintray repo to conan:
```shell
conan remote add my_bintray https://api.bintray.com/conan/latios96/my_conan
```
Now you can install the package:
```shell
conan install OpenSubdiv/3.4.3@latios96/stable
```
