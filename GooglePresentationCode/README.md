Names: 
Course: 

Description: Multithreaded server that accepts input from any number of clients 

----------------------------
======Introduction==========
----------------------------

These source files will be used to create and run a TCP client and server. These can be placed locally or on a server.
A Makefile has been supplied for compilation with the required targets (all, clean), and the Python script used for sending
multiple connections has also been included.

----------------------------
========Execution===========
----------------------------
To compile the server and client, type 'make all' into the command line. This will create two executables: client and server.

To run the server, run the server executable and provide it with an optional port number parameter. The default port number is
the one provided on Moodle (12052). For example, 
	./server 12052

To run the client, supply the following arguments: <ip>:<port> <file> <optional buffer> . For example,
	./client 127.0.0.1:12052 smallTest.txt 2048

A Python3 script has also been supplied to spawn multiple clients simultaneously. To run this program, supply it with the following arguments:
	#ofThreads hostName:portNumber inputFileToSend optionalSizeOfBuffer
For example,
	python3 threadedCall.py 12 ginny.ca:12052 smallTest.txt 2048

----------------------
==Additional  Notes===
----------------------
1. The server was tested using two types of files: small files (several kilobytes) and larger files (~50Mb files). These files were sent one at a time, two at a time, four at a time, and 16 at a time. The server has been set up with sixteen threads to match the maximum number of connections that the server will accept at one time. Adding more clients only causes a large amount of wait time for those files, as they have to wait for connections to open.
2. Cisco anyConnect was used to VPN across to the server from an off campus location. This introduced a high amount of volatility in the connection and file transfer, however the file transfer was a success for all files sent. Sending 20 files of size 50mb took approximately 5 minutes to complete. 
3. File collissions were handled by appending the thread number to the end of the file name. This is a rudimentary fix to the file collision issue and is not meant to be a true fix to the problem. A proper file transfer server would create a hashed value and append it onto the files that are sent to the server in order to avoid any chance for file collisions. However, given the scope of this assignment, this was determined to be acceptable.
4. A soft exit and hard exit was implemented for this server. To test this, it is suggested that you send multiple large files using the Python script to the server and attempt both exit options.

