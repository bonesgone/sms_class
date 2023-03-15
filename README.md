* Create a workspace folder for various projects' workspaces.
```
mkdir catkin_ws
```

* Inside the folder, create src folder for projects' source code.
```
cd catkin_ws && mkdir src
```

* To build the workspace, run this command to generate executables, libraries, and interfaces.
```
~/catkin_ws$ catkin_make
```

* Update your environment whenever you build a new package. It adds several environment variables that ROS needs in order to work. Run this command in every new terminal tab.
```
~/catkin_ws$ source devel/setup.bash
```

* Inside the src folder, create a project folder with a source folder.
```
~/catkin_ws/src$ mkdir projectw3 && cd projectw3 && mkdir src
```

* Inside the catkin_ws, or base folder of all workspaces, build the package again for the project configuration as well.
```
~/catkin_ws$ catkin_make
```
