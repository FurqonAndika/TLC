from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, QTimer, QThread
import sys
import warnings

from driver.time_ import get_date, get_jam
from driver.worker import Worker

import os


class Dashboard:

    def __init__(self):
      
        app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.load("main.qml")
        if not self.engine.rootObjects():
            sys.exit(-1)

        self.button = self.engine.rootObjects()[0].findChild(QObject, "button") 
        self.gambar_utama = self.engine.rootObjects()[0].findChild(QObject, "gambar_utama") 
       
        # self.text = self.engine.rootObjects()[0].findChild(QObject, "text1")
        self.belt = self.engine.rootObjects()[0].findChild(QObject, "belt")
        self.hazard = self.engine.rootObjects()[0].findChild(QObject, "hazard")
        self.speed = self.engine.rootObjects()[0].findChild(QObject, "speed")
        self.tanggal = self.engine.rootObjects()[0].findChild(QObject, "tanggal")
        self.jam = self.engine.rootObjects()[0].findChild(QObject, "jam")
        self.logo = self.engine.rootObjects()[0].findChild(QObject, "logo")


        self.belt.setProperty('visible',False)
        self.hazard.setProperty('visible',False)
        self.speed.setProperty('visible',False)
        self.tanggal.setProperty('visible',False)
        self.jam.setProperty('visible',False)
        
        # self.nilai =0
        # self.rpm_value = 0
        # self.clockwise = True

        # self.gambar.setProperty("visible",False) 
        self.button.clicked.connect(self.send_to_micro)

        self.timer_logo = QTimer(interval=1000)
        self.timer_logo.timeout.connect(self.show_dashboard)
        self.timer_logo.start()

        # self.timer_rpm = QTimer(interval=100)
        # self.timer_rpm.timeout.connect(self.speed)
     

        self.timer_jam = QTimer(interval=500)
        self.timer_jam.timeout.connect(self.update_jam)
        self.timer_jam.start()

        self.hazard_value=False
        self.timer_hazard = QTimer(interval=500)
        self.timer_hazard.timeout.connect(self.blink_hazard)
    
        # self.indicator = True
        
        # self.increment = 0

        self.flag = False
        self.flag_button = False
            
        # set serial worker
        self.worker = Worker()
        self.worker.start()
        self.worker.progress.connect(self.show)

        # paling bawah
        sys.exit(app.exec_())

    def show_dashboard(self):
        self.logo.setProperty('visible',False)
        self.belt.setProperty('visible',True)
        self.hazard.setProperty('visible',True)
        self.speed.setProperty('visible',True)
        self.tanggal.setProperty('visible',True)
        self.jam.setProperty('visible',True)
        self.timer_logo.stop()
        

    def send_to_micro(self):
        try:
            if self.flag_button==False:
                # self.worker.send_data("on")
                self.flag_button=True
                self.button.setProperty('text', 'ON')
                
              
            elif self.flag_button==True:
                # self.worker.send_data("off")
                self.flag_button=False
                self.button.setProperty('text', 'OFF')

        except Exception as e:
            print(e)
    


    def show(self, data):
        print(data)
        try:
            data = data.split(',')
            speed = data[0]
            rpm = data[1]
            belt = data[2]
            hazard =data[3]
            self.speed.setProperty('value', speed)
            if belt=='1':
                self.belt.setProperty('visible',True)
            else:
                self.belt.setProperty('visible',False)

            if hazard=='1' and self.flag==False:
                self.timer_hazard.start()
                self.flag =True
            elif hazard ==0 and self.flag==True:
                self.timer_hazard.stop()
                self.flag=False
        except Exception as e:
            print(e)

        
    
    def update_jam(self):
        self.jam.setProperty('text', str(get_jam()))
        self.tanggal.setProperty("text", str(get_date()))
        # self.indicator = not self.indicator
        # self.gambar.setProperty('visible',self.indicator)
    
    def blink_hazard(self):
        self.hazard_value = not self.hazard_value
        self.hazard.setProperty('visible',self.hazard_value)

        


if __name__ == "__main__":
    os.environ["XDG_SESSION_TYPE"] = "xcb"
    warnings.filterwarnings('ignore')
    Dash = Dashboard()
        



  


