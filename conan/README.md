## Usage

#### Install Conan

First, you will need Conan installed. See [the upstream Conan docs](https://docs.conan.io/2/installation.html) for installation instructions.

You will know you have conan available when you can check the version of conan:

For example, on Linux:

```
$ conan --version
Conan version 2.3.0
```

Make sure you are using at least version 2 of Conan.

#### Clone the repo

```
git clone https://github.com/beman-project/beman.git
```

#### Add the beman repo as a remote

```
conan remote add bemanrepo ./beman/conan/ --allowed-packages="*"
```

#### List available packages

Exact packages and versions in the beman project will vary over time, but you should see some, especially a package called `beman`.

```
$ conan list "*" --remote=bemanrepo "*"
bemanrepo
  beman
    beman/20240520.0
  example
    example/v0.0.0.1
  scn
    scn/v2.0.2
```

#### Make a build directory

In any directory:

```
mkdir build && cd build
```

To install one or more libraries from The Beman Project, you can use the `conan install` command using the versions listed in the `conan list` command. If you want the latest versions of all libraries, you can use this command:

```
$ conan install --requires="beman/[*]" --remote=bemanrepo --build=missing --generator=CMakeToolchain build
```

If everything goes well, you will see a lot of logs print to your screen building all of the requested libraries.


#### Using the installed libraries

Now you can build with your preferred CMake workflow.

For instance, from the command line in Linux:

```
cmake \
  -B build \
  -S beman \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake
```

And to run tests:

```
ctest --test-dir build
```


## References

* https://docs.conan.io/2/installation.html
* https://blog.conan.io/2024/04/23/Introducing-local-recipes-index-remote.html
* https://docs.conan.io/2/tutorial/consuming_packages.html
