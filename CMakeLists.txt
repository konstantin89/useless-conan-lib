cmake_minimum_required(VERSION 3.1.2)

project("UselessLib")

set(LIBRARY_NAME "useless_lib")

set(USELESS_LIB_INCLUDE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(USELESS_LIB_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/src/UselessClass.cpp)

message("Useless library include path: " ${USELESS_LIB_INCLUDE_PATH})

add_library(${LIBRARY_NAME} SHARED ${USELESS_LIB_SOURCES}) 

target_include_directories(${LIBRARY_NAME} PUBLIC ${USELESS_LIB_INCLUDE_PATH}) 

add_subdirectory(tests)