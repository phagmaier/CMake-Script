# CMAKE-SCRIPT

## DESCRIPTION
Makes it easier to make a Cmake file by automating some of the tedious parts of writting one. 
Useful for smaller projects. currently set the minimum cmake requirments. Create a project name. 
Set the c++ version. Include packages and specify the module of the package. Includes all cpp
files for you. Can copy data files to your bin if they aren't there already. Creates executable.
and links the libraries. 


## File Table

| File | Descripton |
| --------- | --------------------- |
| [main.py](main.py) | Basically where this simple program is written|
| [write_cmake.sh](write_cmake.sh) | runs the program from the current dir. So you can put this in your home bin and run it anywhere |


## How to run
Included a little script that will automatically pass the current directory to the path of the 
python file. So you can call that by doing ./write_cmake.sh as long as you change the file permissions
to allow you to run it. If you do this make sure to add the directory of the .py and .sh files
to your path so you can call this script from anywhere. 

