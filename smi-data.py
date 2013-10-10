#!/usr/bin/python

# True (False) if you wnat to show (not show) the corresponding value
# Almost one of the two must be True
show_send = True
show_received = True

# open file in which are stored total data send and received
lines = open("/proc/net/dev", "r").readlines()

columnLine = lines[1]
_, receiveCols , transmitCols = columnLine.split("|")
receiveCols = map(lambda a:"recv_"+a, receiveCols.split())
transmitCols = map(lambda a:"trans_"+a, transmitCols.split())

cols = receiveCols+transmitCols

# define arrow up and arrow down char from unicode
import locale
locale.setlocale(locale.LC_ALL,"")
code = locale.getpreferredencoding()
ARROW_UP = u'\u2191'.encode(code)
ARROW_DOWN = u'\u2193'.encode(code)

send = 0
rec = 0
unitup = "Mb" # default unit is Megabyte
unitdown = "Mb"
for line in lines[3:]:
    if line.find(":") < 0: continue
    face, data = line.split(":")
    tempData = data.split()
    rec += (float(tempData[0]))/(1024.*1024.) # convert byte in Megabyte
    send += (float(tempData[8]))/(1024.*1024.) # convert byte in Megabyte
    if rec>999.99: # convert Megabyte in Gigabyte
        rec = rec/1024.
        unitdown = "Gb"
    if send>999.99: # convert Megabyte in Gigabyte
        send = send/1024.
        unitup = "Gb"

if (show_send & show_received):
	print "%s %.2f %s  |  %s %.2f %s" % (ARROW_UP,send,unitup,ARROW_DOWN,rec,unitdown)
else:
	if show_received:
		print "%s %.2f %s" % (ARROW_DOWN,rec,unitdown)
	else:
		print "%s %.2f %s" % (ARROW_UP,send,unitup)
