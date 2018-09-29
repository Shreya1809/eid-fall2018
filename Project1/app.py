import sys   
import Adafruit_DHT
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog

from login import Ui_login
from myQT import Ui_Dialog
import numpy
import matplotlib.pyplot as plt

#import matplotlib
import time
hum_list = []
temp_list = []
time_list = []
avg_temp_list = []
avg_hum_list = []
num = 0
total_temp = 0
avg_t = 0
total_hum = 0
avg_h = 0
flag = 0
alarm_t = 0
alarm_h = 0
avg_humidity = 0
avg_temperature = 0

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.li = Ui_login()
        self.li.setupUi(self)
        self.li.ok.clicked.connect(self.Login)

        
    def Login(self):
        key = self.li.password.text()
        user = self.li.username.text()
        #print(key)
        if key == 'eid' and user == 'shreya' :
            print('Logged in')
            self.accept()
            print('closed')
        elif key == 'eid' and user != 'shreya':
            self.li.username.setText('Wrong Username')
        elif key != 'eid' and user == 'shreya':
            self.li.password.setText('Wrong Password')
        else:
            self.li.password.setText('Wrong Password')
            self.li.username.setText('Wrong Username')
            
class AppWindow(QDialog):
     def __init__(self):
        super(AppWindow,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)                
        humidity, temperature = Adafruit_DHT.read(22, 4)    
        if humidity is None and temperature is None:
            print('The sensor must be disconnected')
            self.ui.sensor_stat.setText('Sensor is disconnected')
        else:
            self.ui.sensor_stat.setText('Sensor is connected')
            temp = '{0:0.1f}'.format(temperature)
            hum = '{0:0.1f}%'.format(humidity)
            self.ui.temp_val.setText(temp)
            self.ui.hum_val.setText(hum)
            self.ui.avg_temp.setText(temp)
            self.ui.avg_hum.setText(hum)
            self.ui.temp_level.setValue(float(temperature))
            self.ui.hum_level.setValue(float(humidity))
        self.ui.time_req.setText(time.ctime())
        self.ui.refresh.clicked.connect(self.ui.time_req.clear)
        self.ui.refresh.clicked.connect(self.ui.temp_val.clear)
        self.ui.refresh.clicked.connect(self.ui.hum_val.clear)
        self.ui.cel_faran.clicked.connect(self.Cel_Faran)
        self.ui.pushButton_3.clicked.connect(self.Exit)
        self.ui.refresh.clicked.connect(self.SensorReadings)
        self.ui.alarm.setText('NO ALARM')
        self.ui.temp_alarm.valueChanged.connect(self.valuechange)
        self.ui.hum_alarm.valueChanged.connect(self.valuechange)
        self.ui.gen_graph.clicked.connect(self.Graph)
        
        
     def SensorReadings(self):
        global total_temp,num,total_hum,avg_humidity,avg_temperature,total_h
        #start = time.clock()
        humidity,temperature = Adafruit_DHT.read(22, 4)
        if temperature is None and humidity is None :
            print('sensor disconnect')
            self.ui.sensor_stat.setText('Sensor is disconnected')
            self.ui.temp_level.setValue(0)
            self.ui.hum_level.setValue(0)
            
            
        else:
            self.ui.sensor_stat.setText('Sensor is connected')
            temp = '{0:0.1f}'.format(temperature)
            hum = '{0:0.1f}%'.format(humidity)
            temp_list.append(temperature)
            hum_list.append(humidity)
            num = num+1
            total_temp = total_temp + temperature
            total_hum = total_hum + humidity
            avg_t = total_temp/num
            avg_temperature = '{0:0.1f}'.format(avg_t)
            avg_h = total_hum/num
            avg_hum_list.append(avg_h)
            avg_temp_list.append(avg_t)
            avg_humidity = '{0:0.1f}%'.format(avg_h)
            self.ui.temp_level.setValue(float(temperature))
            self.ui.hum_level.setValue(float(humidity))
            self.ui.avg_temp.setText(str(avg_temperature))
            self.ui.temp_val.setText(temp)
            self.ui.avg_hum.setText(str(avg_humidity))
            self.ui.hum_val.setText(hum)
            self.ui.time_req.setText(time.ctime())
            localtime = time.localtime(time.time())
            #https://www.tutorialspoint.com/python/python_date_time.htm
            time_list.append(localtime.tm_sec)
            self.ui.temp_alarm.valueChanged.connect(self.valuechange)
            self.ui.hum_alarm.valueChanged.connect(self.valuechange)
        
     def Cel_Faran(self):
        global flag
        humidity,temperature = Adafruit_DHT.read_retry(22, 4)
        if flag == 0:
            temperature = temperature * 9/5.0 + 32
            flag = 1
        temp = '{0:0.1f}'.format(temperature)
        self.ui.temp_val.setText(temp)
        
     def valuechange(self):
         global alarm_t,alarm_h
         humidity,temperature = Adafruit_DHT.read_retry(22, 4)
         alarm_t = self.ui.temp_alarm.value()
         print('Temp alarm set:' ,alarm_t)
         alarm_h = self.ui.hum_alarm.value()
         print('hum alarm set:' ,alarm_h)
         print(temperature)
         if alarm_t < temperature and alarm_h > humidity:
             print('alarm')
             self.ui.alarm.clear
             self.ui.alarm.setText('TEMP-ALARM')
         elif alarm_h < humidity and alarm_t > temperature:
             self.ui.alarm.clear
             self.ui.alarm.setText('HUM-ALARM')
         elif alarm_h < humidity and alarm_t < temperature:
             self.ui.alarm.clear
             self.ui.alarm.setText('TEMP & HUM ALARM')
         else:
             self.ui.alarm.clear
             self.ui.alarm.setText('NO ALARM')
         
     
     def Exit(self):
         sys.exit(app.exec_())
        
     def Graph(self):   #https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
        #print(avg_humidity)
        plt.plot(time_list,temp_list,'o-', label = "temperature")   
        plt.plot(time_list,hum_list, 'o-', label = "humidity")
        plt.plot(time_list,avg_hum_list, '--', label = "avg hum")
        plt.plot(time_list,avg_temp_list, '--', label = "avg hum")
        plt.xlabel('time axis') 
        plt.ylabel('temp/humidity') 
        plt.title('Temperature and humidty graph!')
        plt.legend() 
        plt.show()
           
     
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    log = LoginWindow()
    if log.exec_() == QtWidgets.QDialog.Accepted: #reference - vipraja
       w = AppWindow()
       a=w.show()
       sys.exit(app.exec_())