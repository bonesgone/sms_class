* Clone a git repository inside the src folder of your workspace folder.
```
git clone https://github.com/online-courses-materials/sms-project5.git
```

* Inside the root of workspace folder, build the project once for early build.
```
~/catkin_ws$ catkin_make
```

* Change your .cpp files into .py files with rospy functions(any IDE)
```
~/catkin_ws$/src gedit rpm_pub.cpp speed_calc.cpp odd_even_service_client.cpp odd_even_service_server.cpp 
```

* Save your modified files with .py extension. After that, rebuild the project inside the root of the workspace folder.
```
~/catkin_ws$ catkin_make
```

* Update your environment whenever you build a new package. It adds several environment variables that ROS needs in order to work. Run this command in every new terminal tab.
```
~/catkin_ws$ source devel/setup.bash
```

* Run the nodes and check the result.
```
~/catkin_ws$ rosrun project5 rpm_pub.py
```

