import socket
import csv
import numpy as np
from numpy import genfromtxt

TCP_IP = '192.168.2.9'
TCP_PORT = 23
BUFFER_SIZE = 16
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#Read from socket and save values to numpy array and csv file
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames =['F1','F2','F3','Ax','Ay','Az']
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='h', quoting=csv.QUOTE_MINIMAL)
    while True:
        try:
            data = s.recv(BUFFER_SIZE)
            final = np.fromstring(data, sep=',')

        except Exception as e:
            print(e)
            s.close()

        print ("received message: ", data)
        writer.writerow([data])
