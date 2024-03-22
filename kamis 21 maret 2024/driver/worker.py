from PyQt5.QtCore import QObject, QThread, pyqtSignal
import serial
import serial.tools.list_ports

class Worker(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(str)
    port =None
    
    def get_port(self):
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element.device)
        lst = connected

        for com in lst:
            try:
                ser = serial.Serial(com, 9600, timeout=1.5).read()
                if ser:
                    print(com)
                    self.port = com
                    break
                    # if (ser.readline()):
                    #     port = com
                    #     print("masuk")
            except Exception as e:
                
                print(e)

    def run(self):
        self.get_port()
        self.ser = serial.Serial(self.port, 9600, timeout=1) 
        while True:                
            try:
                 
                # Reading all bytes available bytes till EOL 
                line = self.ser.readline() 
                if line:
                    # Converting Byte Strings into unicode strings
                    string = line.decode()
                    string = string.strip()
                    self.progress.emit(string) 

            except Exception as e:
                #print(e)
                self.progress.emit("not connect")
                comlist = serial.tools.list_ports.comports()
                
                connected = []
                for element in comlist:
                    connected.append(element.device)
                lst = connected
                #lst.reverse()
                #self.port = lst[0]
                
                print(lst)
                for com in lst:
                    try:
                        print('a')
                        ser = serial.Serial(com, 9600, timeout=1.5)
                        if (ser.readline()):
                            self.port = com
                            self.ser = serial.Serial(self.port, 9600, timeout=1) 
                    except Exception as e:
                        pass             
              
        self.finished.emit()

    def send_data(self, value):
        self.ser.write(value.encode('utf-8'))   