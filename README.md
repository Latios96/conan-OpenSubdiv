[ ![Download](https://api.bintray.com/packages/latios96/my_conan/OpenSubdiv:latios96/images/download.svg?version=3.4.3:stable) ](https://bintray.com/latios96/my_conan/OpenSubdiv:latios96/3.4.3:stable/link)

[![Build status](https://ci.appveyor.com/api/projects/status/nfb4724xnar0we1e?svg=true)](https://ci.appveyor.com/project/Latios96/conan-opensubdiv)
[![Build Status](https://travis-ci.com/Latios96/conan-OpenSubdiv.svg?branch=main)](https://travis-ci.com/Latios96/conan-OpenSubdiv)


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
