import socket
import csv
import numpy as np
from numpy import genfromtxt

TCP_IP = '192.168.2.9'
TCP_PORT = 9999
BUFFER_SIZE = 16
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

#Read from socket and save values to numpy array and csv file
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames =['F1','F2','F3','Ax','Ay','Az']
    writer = csv.DictWriter(csvfile, delimiter=',',
                        quotechar='h', quoting=csv.QUOTE_MINIMAL,fieldnames=fieldnames)
    #writer.writerow(['F1 ','F2 ','F3 ','Ax ','Ay ','Az '])
    writer.writeheader()
    while True:
        try:
            data = sock.recv(128) # buffer size is 1024 bytes
            data = data.decode("utf-8")
            final = np.fromstring(data, sep=',')
            pass
        except Exception as e:
            print(e)

        print ("received message: ", final[0],final[1],final[2],final[3],final[4],final[5])
        writer.writerow({'F1':final[0],'F2':final[1],'F3':final[2],'Ax':final[3],'Ay':final[4],'Az':final[5],})
