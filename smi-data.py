#!/usr/bin/python

lines = open("/proc/net/dev", "r").readlines()

columnLine = lines[1]
_, receiveCols , transmitCols = columnLine.split("|")
receiveCols = map(lambda a:"recv_"+a, receiveCols.split())
transmitCols = map(lambda a:"trans_"+a, transmitCols.split())

cols = receiveCols+transmitCols

import locale
locale.setlocale(locale.LC_ALL,"")
code = locale.getpreferredencoding()
ARROW_UP = u'\u2191'.encode(code)
ARROW_DOWN = u'\u2193'.encode(code)

send = 0
rec = 0
faces = {}
unitup = "Mb"
unitdown = "Mb"
for line in lines[3:]:
    if line.find(":") < 0: continue
    face, data = line.split(":")
    tempData = data.split()
    rec += (float(tempData[0]))/(1024.*1024.)
    send += (float(tempData[8]))/(1024.*1024.)
    if rec>999.99:
        rec = rec/1024.
        unitdown = "Gb"
    if send>999.99:
        send = send/1024.
        unitup = "Gb"

# both send and received
#print "%s %.2f %s  |  %s %.2f %s" % (ARROW_UP,send,unitup,ARROW_DOWN,rec,unitdown)

# received
print "%s %.2f %s" % (ARROW_DOWN,rec,unitdown)

# send
#print "%s %.2f %s" % (ARROW_UP,send,unitup)
