#!/usr/bin/env python3

from pathlib import Path
import sys

def get_libs():
    print("\n\n")
    all_libs = []
    libs = input("If you want to include a external library enter it here: ")
    while libs:
        comps = input("If you want to just include a component type that here: ")
        if comps:
            libs += "::" + comps
        all_libs.append(libs)
        libs = input("If you want to inlude another library enter it here else hit ENTER: ")
    return all_libs

def make_file(version, proj_name, c_version, files, exec, data_files, libs):
    file = "cmake_minimum_required(VERSION " + version + ")\n"
    file += "project(" + proj_name + ')\n'
    file += "set(CMAKE_CXX_STANDARD " + c_version + ')\n'

    for i in libs:
        file += "find_package("
        x = 0
        while x < len(i) and i[x] != ':':
            file += i[x]
            x += 1
        file += " REQUIRED)\n"

    file += "set(CMAKE_CXX_STANDARD_REQUIRED ON)\n"
    file += "set(SOURCES\n"
    for cpp in files:
        file += cpp + "\n"
    file += ")\n"
    for i in data_files:
        file += "configure_file("
        file += i + " ${CMAKE_CURRENT_BINARY_DIR}/"
        file += i + " COPYONLY)\n"

    file += "add_executable(" + exec + " ${SOURCES})\n"
    if libs:
        file += "target_link_libraries(" + exec + " "
        for i in libs:
            if "::" not in i:
                file += i + " "
            else:
                file += "${" + i.upper() + "_LIBRARIES} "
        file = file[:-1]
        file += ")\n"

    with open("CMakeLists.txt", 'w') as cmake:
        cmake.write(file)
    print("\n\nYour CMakeList file should be in your home directory")


def get_src(curr):
    print("\n\n")
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
                return get_src(curr)
            else:
                src_path.mkdir(parents=True, exist_ok=True)
                return src_path

            
def get_cpp(a_path, og_dir):
    files = a_path.glob("*.cpp")
    if a_path == og_dir:
        return [str(i.parts[-1]) for i in files]
    parent_name = str(a_path.parts[-1]) + "/"
    return [ parent_name + str(i.parts[-1]) for i in files]


def copy_data():
    print("\n\n")
    names = []
    print("If you have a data file you want copied over to the directory")
    print("Where you will be making this project type the path relative to the home dir")
    files = input("else just hit enter: ")
    while files:
        names.append(files)
        files = input("If you have another file you'd like copied enter it here: ")
    return names


def main():
    if len(sys.argv) < 2:
        print("Some error occured didn't get current path")
        return
    curr_dir = Path(sys.argv[1])
    print("\n\n")
    version = input("Enter a cmake version or press enter for the default (3.5): ")
    if not version:
        version = '3.5'
    print("\n\n")
    proj_name = input("Please enter the name of your project (if none given defaults to Project): ")
    if not proj_name:
        proj_name = "Project"
    print("\n\n")
    c_version = input("Please enter the c++ version you'd like to use (defualt is 14): ")
    if not c_version:
        c_version = '14'
    print("\n\n")
    exec = input("Please enter the name of your executable (default is runme): ")
    if not exec:
        exec = 'runme'

    src = get_src(curr_dir)
    files = get_cpp(src, curr_dir)
    print("\n\n")
    more = input("If you have any additional folders you need cpp files from press 1 else just press enter: ")
    if more:
        more = get_src(curr_dir)
    while more:
        more = get_src(curr_dir)
        names = get_cpp(more, curr_dir)
        files += names
    data_files = copy_data() 
    libs = get_libs()

    make_file(version, proj_name, c_version, files, exec, data_files, libs)

if __name__ == '__main__':
    print("Welcome to the Simple Cmake Scrpt")
    print("This program assumes it was called at the base level directory of the project")
    main()
