#client example
import socket
import sys
import numpy as np
import cv2
import copy

def play_videoFile(filePath):
    
    video = cv2.VideoCapture(filePath)
    frames_counter = 1

    while True:
        frames_counter = frames_counter + 1
        check, frame = video.read()
        if check:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Capturing", gray)
            key = cv2.waitKey(1)
        else:
            break

    video.release()
    cv2.destroyAllWindows()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))
msg=input('tki ?')
client_socket.send(msg.encode())

while 1:
    data = client_socket.recv(512)
    string = str(data).split(' ')
    if ( data == 'q' or data == 'Q'):
        client_socket.close()

    if (string[0] == "video"):
        print("RECIEVED VIDEO:" + string[1])
        play_videoFile(string[1])

    else:
        print("RECIEVED  " + string[0])

