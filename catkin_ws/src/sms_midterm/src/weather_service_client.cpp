#include "ros/ros.h"
#include "sms_midterm/Weather.h"

int main(int argc, char **argv)
{
    // Initialize the ROS node
    ros::init(argc, argv, "weather_client");

    // Create a handle to the ROS node
    ros::NodeHandle nh;

    // Create a client to call the weather service
    ros::ServiceClient client = nh.serviceClient<sms_midterm::Weather::Request, sms_midterm::Weather::Response>("get_weather");

    // Create a request message
    sms_midterm::Weather::Request req;
    req.latitude = 37.4563;
    req.longitude = 126.7052;
    //req.city = "Incheon";

    // Call the service and get the response
    sms_midterm::Weather::Response res;
    if (client.call(req, res))
    {
        // Print the response
        ROS_INFO("Temperature: %f, Description: %s", res.temperature, res.description.c_str());
    }
    else
    {
        ROS_ERROR("Failed to call service weather");
        return 1;
    }

    return 0;
}
