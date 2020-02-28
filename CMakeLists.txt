cmake_minimum_required (VERSION 3.1.3 FATAL_ERROR)
project (etcd-grpc)

if (EXISTS "${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake")
	message("Using conan installation for dependencies")
	set(BUILD_FROM_CONAN True)
	include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
else() 
	message("Using system instalaltion for dependencies")
	set(BUILD_FROM_CONAN False)	
endif()

set(LIB_TYPE SHARED)
if (${BUILD_FROM_CONAN} AND NOT DEFINED CONAN_BUILD_SHARED_LIBS)
	set(LIB_TYPE STATIC)
endif()
set(LIBRARY_TYPE ${LIB_TYPE})

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE RELEASE)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wpedantic -Werror")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

set(SRC_ROOT "${PROJECT_SOURCE_DIR}/src")

add_subdirectory(${SRC_ROOT})
