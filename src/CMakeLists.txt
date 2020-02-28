set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(SOURCES ${SRC_ROOT}/auth.pb.cc
		${SRC_ROOT}/kv.pb.cc
		${SRC_ROOT}/rpc.pb.cc
		${SRC_ROOT}/rpc.grpc.pb.cc)

add_library(${PROJECT_NAME} ${LIBRARY_TYPE} ${SOURCES})

set(deps "")

if (${BUILD_FROM_CONAN})
	list(APPEND deps CONAN_PKG::protobuf CONAN_PKG::grpc)	
else()
	list(APPEND deps protobuf grpc grpc++)
endif()

target_link_libraries(${PROJECT_NAME} ${deps})

install(TARGETS ${PROJECT_NAME} DESTINATION lib)

install(FILES ${SRC_ROOT}/auth.pb.h
		${SRC_ROOT}/etcdserver.pb.h
		${SRC_ROOT}/kv.pb.h
		${SRC_ROOT}/rpc.grpc.pb.h
		${SRC_ROOT}/rpc.pb.h
	       DESTINATION include/etcd/etcd-grpc)

