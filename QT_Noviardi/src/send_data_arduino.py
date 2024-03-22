import serial

ser = serial.Serial("COM5", 9600, timeout=1)

while(True):
    data_send = input("masukkan perintah: ")
    print(data_send)
    ser.write(data_send.encode('utf-8'))