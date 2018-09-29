# eid-fall2018
Repo for Fall 2018 Embedded Interface Design class
# Name: Shreya Chakraborty
For Project1
Referernces:
1.  https://www.tutorialspoint.com/python/python_date_time.htm 
2.  https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ 
3.  https://stackoverflow.com/questions/11812000/login-dialog-pyqt 
4.  https://pythonspot.com/pyqt5/ 
5.  Adafruit packages for the DHT-22  

# INSTALLATION INSTRUCTIONS:
Run this project on rpi using the following command on terminal :python3 ./app.py

# PROJECT WORK :
The project is my work alone. Any similarities with anyone else's work other than the ones specified in the references is purely
coincidental. The Project requires me to interface a temp/humidity sensor DHT-22 with RPI and design a UI to display the current
temperature, humidity, time of requesting, the status of the sensor and so on. There are 3 files in the project namely- app.py ,
login.py and myQT.py. The file myQT.py and login.py have been generated from the corresponding myQT.ui and login.ui using the command
: pyuic5 file.ui > file.py. The login.py is the file for the login screen which pops up initially as soon as the program is run. It 
asks for username and login. The username is 'shreya' and the password is 'eid'. Only when the username and password match the main
application window is diplayed on the screen. All the basic functionalities have been fulfilled in the project. The application window
called the Temperature and Sensor Analysis displayes sensor status whether conected or disconnected, current temperature, current humidity
avg temp, avg humidity, a slider to set temp and humidity alarm and an alarm notification doe the alarm set. It has a 'refresh' button
to display new temperature and humidity along with the time of the request. Each and everytime refresh is clicked the temp, hum, avg
temp and avg humidity values are stored in a list which is later used to generate a graph. The generate Graph push button pops up a 
graph generated using matplotlib.

# PROJECT ADDITIONS :
The following extra credit options have been attempted
1.  A login screen to secure the application.
2.  Retrieve temp/hum values on a timer and store n values for a graph.
3.  Calculate and display the average temp & hum on the graph.
4.  Make a graphic of a thermometer that shows current retrieved data.
5.  Allow user to set an alarm for an input high or low temperature or humidity value. 
6.  Celcius to Faranheit changing option.
