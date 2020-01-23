import threading
from pythonping import ping
import csv

numpings = int(0)

#######################################
# this will be our primary menu
#######################################

def recordit():
    t = threading.Timer(1.0, recordit)  # would be nice to be able to change the speed.
    t.start()
    myData = []
    pingr = ping('8.8.8.8', count=1)  # need to change 8.8.8.8 to user input variable
    if pingr.rtt_avg_ms == 2000:
        pingr = 0
    else:
        pingr = pingr.rtt_avg_ms
    myData.append(pingr)
    myFile = open('output.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows([myData])
    print(myData)
    t.cancel()



#######################################
# recordit menu
#######################################

def recordmenu():
    ip = input("What IP?")
    numpings = input("How many pings?")

#######################################
# this will be our primary menu
#######################################

def mainmenu():

    print("------------------------------------------------")
    print("Select one of this options")
    print("1. Ping")
    print("0. Exit ")
    print("------------------------------------------------")


mainmenu()


choice = int(input("Please enter: "))
print(choice)
if choice == 1:
    recordmenu()
else:
    print("not pinged")
