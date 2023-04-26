#include "ros/ros.h"
#include "sms_midterm/Weather.h"
#include "cpprest/http_client.h"
#include "cpprest/filestream.h"
#include "cpprest/json.h"

using namespace web;
using namespace web::http;
using namespace web::http::client;
using namespace web::json;

bool handle_get_weather(sms_midterm::Weather::Request& req, sms_midterm::Weather::Response& res)
{
    utility::string_t api_key = "4de2e4bc50f0a3f9ccf833202ba575e6";

   //make a request to the OpenWeatherMap API to get the current weather for the requested location
    utility::string_t url = U("http://api.openweathermap.org/data/2.5/weather?lat=") + std::to_string(req.latitude) +
                            U("&lon=") + std::to_string(req.longitude) + U("&units=metric&appid=") + api_key;
    
    
    // utility::string_t city = uri::encode_data_string(req.city);
    //  utility::string_t url = U("http://api.openweathermap.org/data/2.5/weather?q=") + req.city +
    //                         U("&units=metric&appid=") + api_key;

    // uri_builder builder(U("http://api.openweathermap.org/data/2.5/weather")); TODO
    // builder.append_query(U("q"), city);
    // builder.append_query(U("units"), U("metric"));
    // builder.append_query(U("appid"), api_key);

    //http_client client(url);
    http_client client(url);
    http_response response = client.request(methods::GET).get();

    // parse the response as JSON and extract the temperature and weather description fields
    json::value json_response = response.extract_json().get();
    if (json_response[U("main")][U("temp")].is_number())
    {
        float temperature = json_response[U("main")][U("temp")].as_double();
        res.temperature = temperature;
    }
    else
    {
        ROS_ERROR("Temperature field is not a number");
        return false;
    }

    utility::string_t description = json_response[U("weather")][0][U("description")].as_string();
    res.description = std::string(description.begin(), description.end());

    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "weather_server");
    ros::NodeHandle nh;

    // create a service server that takes latitude and longitude as arguments and returns temperature and description
    ros::ServiceServer weather_service = nh.advertiseService<sms_midterm::Weather::Request, sms_midterm::Weather::Response>(
        "get_weather", handle_get_weather);

    ROS_INFO("Weather service server is ready.");

    ros::spin();

    return 0;
}
