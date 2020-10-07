for arg in "$@"
do
    case $arg in
        "source" )
           conan source . --source-folder=testing/source;;
        "install" )
           conan install . --install-folder=testing/build;;
        "build" )
           conan build . --source-folder=testing/source --build-folder=testing/build;;
        "package" )
          conan package . --source-folder=testing/source --build-folder=testing/build --package-folder=testing/package;;
        "export-pkg" )
          conan export-pkg . user/channel --source-folder=testing/source --build-folder=testing/build;;
        "test" )
          conan test test_package $2@user/channel;;
        "create" )
          conan create . user/channel;;
   esac
done