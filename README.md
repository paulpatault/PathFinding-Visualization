# Pathfinding Visualizer
A [Pygame](https://www.pygame.org/) GUI visualization of the Dijkstra or A* path finding algorithm. It allows you to pick your start and end node in the table and view the process of finding the shortest path.

# Preview


| ![Preview GIF](assets/preview/astar.gif) | ![Preview GIF](assets/preview/dij.gif) |
| :--------------------------------------: | :------------------------------------: |
|           **Astar algorithm**            |         **Dijkstra algorithm**         |


# Dependencies and run commands

Here are the commands to install all dependencies and run the program : 

*Simple Version*
```
$ pip3 install -r requirements.txt
$ python3 src/main.py
```
or *Advanced Version*
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python src/main.py
```

# Options

**This field must be updated**

You can add :
+ `--N=x`, where `x` is the lenght of the board
+ `--C=strong | smooth`, change colors style
+ `--algo=astar | (dij | dijkstra)`, choice of the algorithm used
+ `--nd=True | False`, "No Diagonals" : authorize or not diagonal search

# License
[MIT](https://choosealicense.com/licenses/mit/) License
