this is still very barebones, please be prepared to be frustrated and dislike cmake even more.

## First setup

```sh
$ git clone --recurse-submodules https://github.com/DisnakeDev/libdave.py.git
```

#### Windows

```sh
$ cd libdave.py/libdave/cpp/vcpkg/.bootstrap-vcpkg.bat
```

#### Linux and MacOS

```sh
$ cd libdave.py/libdave/cpp/vcpkg/.bootstrap-vcpkg.sh
```

## How to build
```sh
$ cmake -B build
$ cmake --build build --parallel $(nproc)
```
