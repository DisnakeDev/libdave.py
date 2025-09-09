cmake_minimum_required(VERSION 3.10)

# this is probably not the proper way to do this
set(CMAKE_TOOLCHAIN_FILE libdave/cpp/vcpkg/scripts/buildsystems/vcpkg.cmake CACHE STRING "")
set(VCPKG_MANIFEST_DIR libdave/cpp/vcpkg-alts/boringssl CACHE STRING "")

project(HelloWorld)

add_subdirectory(libdave/cpp)
# find_package(libdave CONFIG REQUIRED)

add_executable(HelloWorld helloworld.cpp)

target_link_libraries(HelloWorld PRIVATE libdave)
