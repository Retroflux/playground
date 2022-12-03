#!/usr/bin/python3
import sys
import threading
import subprocess
from shutil import copyfile
import os.path

def thread(num,bufferSize,hostName,fileName):
	if not (os.path.exists("./data")):
		os.makedirs("./data")
	if (os.path.isfile("data/"+str(num)+".txt") == False):
		print("File not found")
		copyfile(fileName,"data/"+str(num)+".txt")
	print('Making call to server %s' % num)
	subprocess.run(["./client", hostName, "data/"+str(num)+".txt", bufferSize])


threads = []
if (len(sys.argv) == 4 or len(sys.argv) == 5):
	loopCounter = int(sys.argv[1])
	bufferSize = 2048
	hostName = sys.argv[2]
	fileName = sys.argv[3]
	if (len(sys.argv) == 5):
		bufferSize = sys.argv[4]
	for i in range(loopCounter):
		t = threading.Thread(target=thread, args=(i,bufferSize,hostName,fileName))
		threads.append(t)
		t.start()
else:
	print("Usage: python3 threadCall.py #ofThreads hostName:portNumber inputFileToSend sizeOfBuffer")
