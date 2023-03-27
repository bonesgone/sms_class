* Create a new project folder.
```
~/catkin_ws/src$ mkdir project_ws4 && cd project_ws4 && mkdir src
```

* Inside the root of the workspace(in my case, catkin_ws), build the package.
```
~/catkin_ws$ catkin_make
```

* Inside the src folder, firstly, create a communication over a topic with a publisher and subscriber nodes. Create two cpp files and copy the code from my cpp files. In this case, the publisher node sends a message "Hello" to the topic and the other node is subscribed and listens to the publisher.
```
~/catkin_ws/src/ gedit publisher_node.cpp  subscriber_node.cpp
```

* Secondly, another communication to be created is a service-based communication. Services allow nodes to send a request and receive a response. Copy to your source as well.
```
~/catkin_ws/src/ gedit addition_service_node.cpp
```

* The service node, or in my case only the service server, returns a response to the request from the user input prompted in the command line. It returns a sum of two integers. 

* After finishing source files, change accordingly configuration files and package dependencies. 
```
~/catkin_ws/src/ gedit CMakeLists.txt package.xml
```

*Lastly, build your package inside the root of the workspace.
```
~/catkin_ws$ catkin_make
```

###Output
![image](https://user-images.githubusercontent.com/64888324/227823308-c407774b-15f0-42e3-a980-8060ad592e55.png)
![image](https://user-images.githubusercontent.com/64888324/227823826-bafaded9-ab3e-40ca-894b-0e956c6c7893.png)
![image](https://user-images.githubusercontent.com/64888324/227823525-99ecbc78-7797-4413-ae4d-234cc243a664.png)



 






