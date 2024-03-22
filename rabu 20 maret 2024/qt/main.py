from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, QTimer
import sys


from driver.time_ import get_date, get_jam



class Dashboard:

    def __init__(self):
        
        app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.load("main.qml")
        if not self.engine.rootObjects():
            sys.exit(-1)
        
        # button = self.engine.rootObjects()[0].findChild(QObject, "button1") 
       
        # self.text = self.engine.rootObjects()[0].findChild(QObject, "text1")
        # self.gambar = self.engine.rootObjects()[0].findChild(QObject, "gambar")
        # self.rpm = self.engine.rootObjects()[0].findChild(QObject, "rpm")
        # self.tanggal = self.engine.rootObjects()[0].findChild(QObject, "tanggal")
        # self.jam = self.engine.rootObjects()[0].findChild(QObject, "jam")
        
        # self.nilai =0
        # self.rpm_value = 0
        # self.clockwise = True

        # self.gambar.setProperty("visible",False) 
        # button.clicked.connect(self.function)

        # self.tanggal.setProperty("text", str(get_date()))

        # self.timer_rpm = QTimer(interval=100)
        # self.timer_rpm.timeout.connect(self.speed)
     

        # self.timer_jam = QTimer(interval=500)
        # self.timer_jam.timeout.connect(self.update_jam)

        
       
    
        # self.indicator = True
        
        # self.increment = 0

        # paling bawah
        sys.exit(app.exec_())
    
    # def update_jam(self):
    #     self.jam.setProperty('text', str(get_jam()))
    #     self.indicator = not self.indicator
    #     self.gambar.setProperty('visible',self.indicator)
    
    
    # def speed(self):
    #     if (self.rpm_value<150 and self.clockwise):
    #         self.rpm_value +=1
    #         if (self.rpm_value==150):
    #             self.clockwise=False
    #     elif (self.clockwise ==False):
    #         self.rpm_value -=1
    #         if (self.rpm_value<0):
    #             self.clockwise=True
    #     self.rpm.setProperty("value",str(self.rpm_value))
    #     self.text.setProperty('text',str(self.rpm_value))

        

    # def function(self):
    #     print("button di tekan")
    #     self.increment +=1
    #     if self.increment%2==0:
    #         self.timer_rpm.stop()
    #         self.rpm.setProperty('value',0)
    #         self.text.setProperty('text','RPM')
    #     else:
    #         self.timer_rpm.start()
     
                 


if __name__ == "__main__":
    Dash = Dashboard()
        



  


