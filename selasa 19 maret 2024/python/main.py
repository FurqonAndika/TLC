import serial
import serial.tools.list_ports   

# print(type(serial))
# print(type(serial.tools.list_ports))

# mendapatkan list port yang terhubung dengan komputer
ports = serial.tools.list_ports.comports()

for port in ports:
    print('port :',port.device)


try:
    for port in ports:
        ser = serial.Serial(port.device, 9600, timeout=1)
        data = ser.readline()
        if data:
            print('ada data')
            break
    

except Exception as e:
    print("error ser", e)


while (True):
    try:
        line = ser.readline()
        line = line.decode()
        # print data dari arduino
        print(line)

        # parsing data
        data_raw = line.split(",")
        speed = data_raw[0]
        rpm = data_raw[1]
        engine_temp = data_raw[2]
        temp = data_raw[3]
        current = data_raw[4]
        voltage = data_raw[5]
        print(speed, rpm, engine_temp, temp, current, voltage)
        
        # kirim data
        ser.write(bytes("data", 'utf-8')) 
        
    except Exception as e:
        print("error while", e)

        try:
            ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

        except Exception as e:
            print("error ser", e)




# speed, rpm, suhu engine, suhu ruangan, arus, tegangan,
#100,10,27,50,10,220

# Serial.println("100,10,27,50,10,220")
