# Smart Mobility Service Midterm Project

* Create a package sms_midterm with its required dependent packages.
```
catkin_make sms_midterm message_generation roscpp std_msgs rospy
```

* Inside the folder, create a src folder for nodes.
```
~/sms_midterm$ mkdir src folder.
```

* Build the package inside the root of the workspace for configuration.
```
~/catkin_ws$/catkin_make
```

## First Task

* Create a srv file inside a srv folder for a request and response data. Copy the contents to the file.
```
~/sms_midterm$ mkdir srv && gedit Weather.srv
```

```
* Create a service client and service server nodes.
~/sms_midterm/src gedit weather_service_client.cpp weather_service_server.cpp
```

* Modify a CMakeLists.txt for configuration of all files, including the nodes executables and service files.
```
~/sms_midterm$ gedit CMakeLists.txt
```

* Copy the contents of the service client and the service server. The client node sends GPS location of the vehicle, while the server node sends the current weather status there. API calls are implemented using OpenWeatherMap API.

* Create a launch folder and create a launch file inside the folder to run both nodes at once. Copy the contents to it.
```
~/sms_midterm$ mkdir launch && gedit weather_status.launch 
```

* Build the package inside the root of the workspace.
```
~/catkin_ws$ catkin_make
```

* Source new configurations for each new terminal tab.
```
~/catkin_ws$ source devel/setup.bash
```

* Run the launch file to see both nodes running simultaneously. The client sends a request to the server by sending fixed latitude and longitude of Incheon City and the server sends a one time response with the current temperature and weather description.
```
~/catkin_ws$ roslaunch sms_midterm weather_status.launch
```
### Output
![image](https://user-images.githubusercontent.com/64888324/234596597-d5cd90ee-9687-41c4-809d-3e9f130f1147.png)

## Second Task
* With current package configurations, create a publisher node to send a speed of the autonomous vehicle to a topic. Also, a subcriber node is subscribed to the speed publisher and echo the plate number and whether the vehicle violates the speed limit or not. Copy the contents to both nodes. The subscriber must get the parameter as a speed limit. The paramer will be set in the launch file.
```
~/sms_midterm/src$ gedit plate_subcriber.py speed_publisher.py 
```

* Create a launch file to run both nodes and set the parameter as a speed limit. Copy the contents to it.
```
~/sms_midterm$ gedit speed_monitor.launch
```

* Build the package again.
```
~/catkin_ws$ catkin_make
```

* Source new configurations for each new terminal tab.
```
~/catkin_ws$ source devel/setup.bash
```

* Run the launch file to see if the vehicle violates the speed limit or not.
```
~/catkin_ws$ roslaunch sms_midterm speed_monitor.launch
```

### Output
![image](https://user-images.githubusercontent.com/64888324/234601195-8363a2fa-7323-471b-a06d-1b6bb699a52f.png)

