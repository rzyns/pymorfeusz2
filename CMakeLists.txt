cmake_minimum_required(VERSION 3.27)
project(pymorfeusz2 VERSION "0.1.0")

set(CMAKE_CXX_STANDARD 20)

include(litgen_cmake/litgen_cmake.cmake)

litgen_find_pybind11()

set(python_module_sources
    src/pymorfeusz2/module.cpp
    src/pymorfeusz2/pybind_Morfeusz2.cpp
)

pybind11_add_module(_morfeusz2 ${python_module_sources})
litgen_setup_module(
    morfeusz2
    _morfeusz2
    morfeusz2
    ${CMAKE_CURRENT_LIST_DIR}/src/pymorfeusz2
)
