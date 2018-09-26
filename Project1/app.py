import sys
import Adafruit_DHT
from PyQt5.QtWidgets import QApplication, QDialog
from myQT import Ui_Dialog
import time
num_t = 0
total_temp = 0
avg_t = 0
num_h = 0
total_hum = 0
avg_h = 0
flag = 0
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        temp = '{0:0.1f}'.format(temperature)
        hum = '{0:0.1f}%'.format(humidity)
        #time.ctime() # 'Mon Oct 18 13:35:29 2010'
        self.ui.temp_val.setText(temp)
        self.ui.hum_val.setText(hum)
        self.ui.avg_temp.setText(temp)
        self.ui.avg_hum.setText(hum)
        self.ui.time_req_temp.setText(time.ctime())
        self.ui.time_req_hum.setText(time.ctime())
        self.ui.temp_refresh.clicked.connect(self.ui.time_req_temp.clear)
        self.ui.temp_refresh.clicked.connect(self.ui.temp_val.clear)
        self.ui.hum_refresh.clicked.connect(self.ui.time_req_hum.clear)
        self.ui.hum_refresh.clicked.connect(self.ui.hum_val.clear)
        self.ui.cel_faran.clicked.connect(self.Cel_Faran)
        self.ui.pushButton_3.clicked.connect(self.Exit)
        #time.sleep(2)
        self.ui.temp_refresh.clicked.connect(self.tempReadings)
        #self.ui.temp_refresh.clicked.connect(self.ui.temp_val.clear)
        self.ui.hum_refresh.clicked.connect(self.humReadings)
        #self.ui.hum_refresh.clicked.connect(self.ui.hum_val.clear)
        
        #self.ui.time_req_temp.clicked.connect(self.ui.hum_val.clear)
    def tempReadings(self):
        global num_t,total_temp
        humidity,temperature = Adafruit_DHT.read_retry(22, 4)
        temp = '{0:0.1f}'.format(temperature)
        num_t = num_t+1
        total_temp = total_temp + temperature
        avg_t = total_temp/num_t
        avg_temperature = '{0:0.1f}'.format(avg_t)
        print(avg_temperature)
        self.ui.avg_temp.setText(str(avg_temperature))
        self.ui.temp_val.setText(temp)
        self.ui.time_req_temp.setText(time.ctime())
        
    def Cel_Faran(self):
        global flag
        humidity,temperature = Adafruit_DHT.read_retry(22, 4)
        if flag == 0:
            temperature = temperature * 9/5.0 + 32
            flag = 1
        temp = '{0:0.1f}'.format(temperature)
        self.ui.temp_val.setText(temp)
        
    def humReadings(self):
        global num_h,total_hum
        humidity,temperature = Adafruit_DHT.read_retry(22, 4)
        hum = '{0:0.1f}%'.format(humidity)
        num_h = num_h+1
        total_hum = total_hum + humidity
        avg_h = total_hum/num_h
        avg_humidity = '{0:0.1f}%'.format(avg_h)
        self.ui.avg_hum.setText(str(avg_humidity))
        self.ui.hum_val.setText(hum)
        self.ui.time_req_hum.setText(time.ctime())
    def Exit(self):
        sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())