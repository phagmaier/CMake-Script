#!/usr/bin/env python3

from pathlib import Path
import sys

def make_file(version, proj_name, c_version, files, exec, dir):
    file = "cmake_minimum_required(VERSION " + version + ")\n"
    file += "project(" + proj_name + ')\n'
    file += "set(CMAKE_CXX_STANDARD " + c_version + ')\n'
    file += "set(CMAKE_CXX_STANDARD_REQUIRED ON)\n"
    file += "set(SOURCES\n"
    for cpp in files:
        file += cpp + "\n"
    file += ")\n"
    file += "add_executable(" + exec + " ${SOURCES})\n"
    with open("CMakeLists.txt", 'w') as cmake:
        cmake.write(file)


def get_src(curr):
    print("If you have a source DIR please enter the relative path")
    src = input("If it's the current DIR just hit enter: ")
    if not src:
        return curr 
    else:
        src_path = Path(curr/src)
        if src_path.exists():
            return src_path
        else:
            print("Path does not exist")
            answer = input("Press enter if you made a typo OR press 1 then enter if you want to create that directory")
            if not answer:
                get_src(curr)
            else:
                src_path.mkdir(parents=True, exist_ok=True)
                return src_path

            
def get_cpp(a_path):
    files = a_path.glob("*.cpp")
    parent_name = str(a_path.parts[-1]) + "/"
    return [ parent_name + str(i.parts[-1]) for i in files] 


def main():
    if len(sys.argv) < 2:
        print("Some error occured didn't get current path")
        return
    curr_dir = Path(sys.argv[1])
    version = input("Enter a cmake version or press enter for the default (3.5): ")
    if not version:
        version = '3.5'
    proj_name = input("Please enter the name of your project (if none given defaults to Project): ")
    if not proj_name:
        proj_name = "Project"

    c_version = input("Please enter the c++ version you'd like to use (defualt is 14): ")
    if not c_version:
        c_version = '14'
    exec = input("Please enter the name of your executable (default is runme): ")
    if not exec:
        exec = 'runme'

    src = get_src(curr_dir)
    files = get_cpp(src)

    more = input("If you have any additional folders you need cpp files from press 1 else just press enter: ")
    if more:
        more = get_src(curr_dir)
    while more:
        more = get_src(curr_dir)
        names = get_cpp(more)
        files += names

    make_file(version, proj_name, c_version, files, exec, curr_dir)

if __name__ == '__main__':
    print("Welcome to the Simple Cmake Scrpt")
    print("This program assumes it was called at the base level directory of the project")
    main()
