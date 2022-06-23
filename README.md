# Pathfinding Algorithm Visualizer
This application is my second take on Pathfinding Algorithm Visualizer. It visualizes and demonstrates internal work of various path finding algorithms.

![Dijkstra Found](https://user-images.githubusercontent.com/7826894/175387101-363a1058-b923-441c-8df1-d1d5a6b2d23f.png)



**Tech characteristics:**
* Implemented game using OOP design principles:
    * Encapsulation
    * Formal Interface
* Implemented two algorithms:
    * Depth-first Search Algorithm - unweighted, does not guarantee shortest path
    * Dijkstra Algorithm - weighted, does guarantee shortest path
* Easy extensibility
* GUI via Pygame
* Fonts work on different operation systems

**GUI Interface:**
- You can select and deselect start and target nodes by left/right mouse click
- You can build and deselect walls by right/left mouse click on unvisited node
- Select algorithm of your choice by using numbers on your keyboard
- Press "R" on your keyboard to reset canvas


**ToDO:** (in the order of importance and interest):
* Add A* algorithm
* Add option to generate mazes (e.g. with Kruskal's Algorithm)
* Add notification when algorithm did not find any path
* Solve an issue when running algorithm letters become a little blurry


![Dijkstra 1](https://user-images.githubusercontent.com/7826894/175387207-e422efc5-bcea-4316-afd7-cf19e58c08c7.png)

Dijkstra Algorithm is searching for the target node [picture above]

![Dijkstra 2](https://user-images.githubusercontent.com/7826894/175387218-d26b184e-79a2-4784-a993-8d25686a662c.png)

Dijkstra Algorithm is searching for the target node [picture above]

![Dijkstra Found](https://user-images.githubusercontent.com/7826894/175387226-9b59ea50-6b77-4392-a1b4-692671187de6.png)

Dikstra found the shortest path [picture above]

![DFS 1](https://user-images.githubusercontent.com/7826894/175387242-f2d434b4-fc74-4875-b682-cc038bb1d452.png)

Right before running Depth-first Search Algorithm [picture above]

![DFS 2](https://user-images.githubusercontent.com/7826894/175387257-ea3d454e-7013-4868-9bdb-b943faaea141.png)

Depth-first Search is looking for the target node [picture above]

![DFS 3](https://user-images.githubusercontent.com/7826894/175387262-8233124b-904f-4c82-be3d-30c7c6c6e43f.png)

Depth-first Search is looking for the target node [picture above]

![DFS Found](https://user-images.githubusercontent.com/7826894/175387269-3ea6ebb5-ddc2-4b9d-8b57-1fc893f92c10.png)

Depth-first Search found the path between two nodes(it does not guarantee the path is the shortest) [picture above]



