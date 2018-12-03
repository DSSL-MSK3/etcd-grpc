cmake_minimum_required (VERSION 3.1.3 FATAL_ERROR)
project (etcd-grpc)

set(LIBRARY_TYPE SHARED)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE RELEASE)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wpedantic -Werror")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

set(SRC_ROOT "${PROJECT_SOURCE_DIR}/src")

add_subdirectory(${SRC_ROOT})
