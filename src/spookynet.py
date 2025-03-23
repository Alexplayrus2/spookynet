import urllib.request
import random
import os
import sys
import time
import logging
serverurl = "https://alexplayrus1.pythonanywhere.com/multiplayer/" # change if you want to use a custom server
pathlol = str(str(sys.executable).replace("spookynet.exe", "")) # replace exe name with urs or it will break if u rename
selfid = str(random.randrange(0,10000))
print("Welcome to SpookyNet! Your ID is " + selfid)
otherid = input("Enter the ID of the person you want to join: ")
delay = float(input("Enter request delay (recommended: 0 to 1) (float), if you dont see other players and get alot of request errors then raise it, however it will make you laggier, you can set it to 0 if ur using a custom server): "))
while True:
    file = open(pathlol + "p2data.ini", "w")
    try:
        contents = urllib.request.urlopen(serverurl + "get?name=SJM" + otherid).read()
        file.write(contents.decode('utf-8').replace("ENTERSPACE", "\n"))
        print("Get request success!")
    except Exception as e:
        print("Get request error! " + str(e) + ", see below for extra details")
        logging.exception("GetReqException")
    time.sleep(delay)
    file = open(pathlol + "p1data.ini", "r")
    fcontent = file.read()
    try:
        contents = urllib.request.urlopen(serverurl + "set?name=SJM" + selfid + "&val=" + fcontent.replace("\n", "ENTERSPACE")).read()
        print("Set request success!")
    except Exception as e:
        print("Set request error! " + str(e) + ", see below for extra details")
        logging.exception("SetReqException")
    
    time.sleep(delay)
