# CMAKE-SCRIPT

## DESCRIPTION
Makes it easier to make a Cmake file by automating some of th tedious parts of writting one. Useful for smaller projects. Nothing fancy more functionality needs to be added.


## File Table

| File | Descripton |
| --------- | --------------------- |
| [main.py](main.py) | Basically where this simple program is written|
| [write_cmake.sh](write_cmake.sh) | runs the program from the current dir. So you can put this in your home bin and run it anywhere |


## How to run
I suggest putting the folder in your ~/bin file and then making an alias in you bashrc so you if you do want to use it you can run it from anywhere. If not just adjust the path in the .sh file since I assume it will be in your home directory and then have it call the python file. Could also call the python file directly and just passthe current directory you are working in or $PWD


