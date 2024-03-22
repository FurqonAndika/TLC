from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, QTimer
import sys

from driver.time_ import get_date
from driver.time_ import get_jam
from driver.worker import Worker

class dashboard:
    def __init__(self):
        app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.load("main.qml")
        if not self.engine.rootObjects():
            sys.exit(-1)

        self.button = self.engine.rootObjects()[0].findChild(QObject, "button_1")
        self.text_kecepatan = self.engine.rootObjects()[0].findChild(QObject, "text_kecepatan")
        self.headLamp = self.engine.rootObjects()[0].findChild(QObject, "headLamp")
        self.parkingBrake = self.engine.rootObjects()[0].findChild(QObject,"parkingBrake")
        self.kecepatan = self.engine.rootObjects()[0].findChild(QObject,"kecepatan")
        self.Tanggal = self.engine.rootObjects()[0].findChild(QObject,"Tanggal")
        self.Jam = self.engine.rootObjects()[0].findChild(QObject,"Jam")

        # self.nilai = 0
        # self.kecepatan_value = 0
        # self.clockwise = True
        self.increament = 0

        self.button.clicked.connect(self.send_to_arduino)
        # self.text.setProperty("text", "TLC")
        # self.TurnSignalKanan.setProperty("visible", False)
        self.Tanggal.setProperty("text", str(get_date()))

        self.timer_parkingBrake_value = False
        self.timer_parkingBrake = QTimer(interval=450)
        self.timer_parkingBrake.timeout.connect(self.blink_parkingBrake)

        self.flag = False
        


        timerJam = QTimer(interval=1000)
        timerJam.timeout.connect(self.update_jam)
        timerJam.start()

        # self.timerTurnSignalKanan = QTimer(interval=1000)
        # self.timerTurnSignalKanan.timeout.connect(self.function)

        # self.indicator = True
            
        # set serial worker
        self.worker = Worker()
        self.worker.start()
        self.worker.progress.connect(self.show)

        sys.exit(app.exec_())

    def show(self, data):
        data = data.split(',')
        print(data)
        self.kecepatan.setProperty('value', data[0])
        self.text_kecepatan.setProperty('text', data[0])
        if data[3]=='0':
            self.headLamp.setProperty('visible', False)
        else:
            self.headLamp.setProperty('visible', True)

        if data[2]=='0'and self.flag==False:
            self.timer_parkingBrake.stop()
            self.parkingBrake.setProperty('visible', False)
            self.flag=True     
        elif data[2]=='1' and self.flag==True:
            self.timer_parkingBrake.start()
            self.flag=False

    def blink_parkingBrake(self):
        self.timer_parkingBrake_value = not self.timer_parkingBrake_value
        self.parkingBrake.setProperty('visible', self.timer_parkingBrake_value)

    



    # def speed(self):
    #     if(self.kecepatan_value<150 and self.clockwise):
    #         self.kecepatan_value +=1
    #         if(self.kecepatan_value==150):
    #             self.clockwise=False
    #     elif(self.clockwise == False):
    #         self.kecepatan_value -=1
    #         if(self.kecepatan_value<0):
    #             self.clockwise=True
    #     self.kecepatan.setProperty("value", str(self.kecepatan_value))
    #     self.text.setProperty("text", self.kecepatan_value)

        

    def update_jam(self):
        self.Jam.setProperty("text", str(get_jam()))
        self.Tanggal.setProperty("text", str(get_date()))
    #     self.indicator = not self.indicator       
    #     self.TurnSignalKanan.setProperty("visible", self.indicator)
        

    def send_to_arduino(self):
        self.increament+=1
        if self.increament%2==0:
            self.worker.send_data("on")
            self.button.setProperty('text', "on")
            
           
        else :
            self.worker.send_data("off")
            self.button.setProperty('text', "off")
           
            

    #     self.increament+=1
    #     if self.increament%2==0:
    #         self.timer.stop()
    #         self.kecepatan.setProperty("value",0)
    #         self.text.setProperty("text", "TOYOTA")
            
    #     else:
    #         self.timer.start()
    
       


if __name__ == "__main__":
    Dash = dashboard()