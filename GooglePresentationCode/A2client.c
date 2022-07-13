#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <netdb.h> 

struct sockaddr_in buildDest(char * ipArg);
long getBuffer(char * inBufferSize);
long getFileSize(char * fileName);
char * getHostIp(const char *host);

int main(int argc, char * argv[])
{
	struct sockaddr_in dest; 		//Struct for server connection information
	long bufferSize = 2048;
	int errCode = 0;
	memset(&dest, 0, sizeof(dest));	//Clean struct info

	if (argc == 3) // ./client ip:port fileName.txt
	{
		dest = buildDest(argv[1]);
	}
	else if (argc == 4) // ./client ip:port fileName.txt buffer
	{
		dest = buildDest(argv[1]);
		bufferSize = getBuffer(argv[3]);
	}
	else // ./client 
	{
		printf("Incorrect arguments. Please run the program with ./client <ip>:<port> <file> <optional buffer>\n");
		exit(EXIT_FAILURE);
	}

	if (strlen(argv[2]) > 20)
	{
		printf("Invalid file name. Expecting file name < 21 chars.\n");
		exit(EXIT_FAILURE);
	}

	printf("Beginning File Transfer ...\n");

	char * fileNameSend = calloc(21, sizeof(char));
	char * fileName = argv[2];
	strcat(fileNameSend,argv[2]);
	for (int i = strlen(argv[2]); i < 20; ++i)
	{
		fileNameSend[i] = ':';
	}
	fileNameSend[21] = '\0';

	FILE * fp = fopen(fileName, "r+");

	if (fp == NULL)
	{
		printf("Invalid file name \" %s \". Could not open file.\n", fileName);
		exit(-1);
	}

	int bytesRead = 0;
	char * buffer = calloc(bufferSize+1, sizeof(char));

	//Open the socket
	int mysocket = socket(AF_INET, SOCK_STREAM, 0);

	if (mysocket < 0)
	{
		printf("Error creatng socket on given port. Exiting.\n");
		exit(-1);
	}

	//Connect to the given server
	errCode = connect(mysocket, (struct sockaddr *)&dest, sizeof(struct sockaddr_in));
	
	if (errCode != 0)
	{
		printf("Server Connection Refused... Try Again Later. :(\n");
		exit(-1);
	}

	//send(mysocket, header, strlen(header), 0);
	long fileSize = getFileSize(fileName);

	printf("Sending %s (%ld bytes) to server in chunks of %ld.\n", fileName,fileSize, bufferSize);

	int len = 0;

	len = send(mysocket, &fileSize, sizeof(fileSize), 0);

	printf("FileSize Sent: %d\n", len);

	len = send(mysocket, &bufferSize, sizeof(bufferSize), 0);

    printf("BuffSize Sent: %d\n", len);

	len = send(mysocket, fileNameSend, 21, 0);

	printf("FileName Sent: %d\n", len);

	while ((bytesRead = fread(buffer, 1, bufferSize, fp)) > 0)
  	{
  		buffer[bytesRead] = '\0';
    	//printf("%lu | ~:%s:~\n", strlen(buffer), buffer);
    	send(mysocket, buffer, bufferSize, 0);
  	}

	printf("Transfer Complete! Exiting.\n");

  	fclose(fp);
  	free(fileNameSend);
  	close(mysocket);

  	return EXIT_SUCCESS;
}

struct sockaddr_in buildDest(char * ipArg)
{
	struct sockaddr_in dest;
	dest.sin_family = AF_INET;		// Use the IPv4 address family

	char * hostIp = calloc(strlen(ipArg), sizeof(char));
	int port = 0;

	sscanf(ipArg, "%[^:]:%d", hostIp, &port);

	//printf("Address: %s\nPort: %d", hostIp, port); 

	if (strlen(hostIp) < 1 || port < 1)
	{
		printf("Invalid Argument. Expecting IP:Port for argv[1].\n");
		free(hostIp);
		exit(EXIT_FAILURE);
	}
	else
	{
		//Set up hostIp & Port Num in the struct
		dest.sin_addr.s_addr = inet_addr(getHostIp(hostIp));
		dest.sin_port = htons(port);            
	}
	return dest;
}

long getBuffer(char * inBufferSize)
{
	long buffer = 0;
	sscanf(inBufferSize,"%ld",&buffer);

	if (buffer < 1)
	{
		printf("Invalid Argument. Expecting numeric buffer > 0 for argv[3].\n");
		exit(EXIT_FAILURE);
	}

	return buffer;
}

long getFileSize(char * fileName)
{
	FILE * fp = fopen(fileName, "r+");
	long fileSize = 0;
	while(fgetc(fp) != EOF)
	{
		fileSize++;
	}

	fclose(fp);

	return fileSize;
}

char * getHostIp(const char *host)
{
	struct addrinfo hints, *results, *looper;
	int errCode;
	int numIps = 0;
	char addrstr[2048];
	char * ipStr = NULL;
	void * ptr;

	memset (&hints, 0, sizeof (hints));
	hints.ai_family = PF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags |= AI_CANONNAME;

    //
	errCode = getaddrinfo(host, NULL, &hints, &results);
	
	if (errCode != 0)
	{
		printf("getaddrinfo failed: %s\n", gai_strerror(errCode));
		exit(-1);
	}

	looper = results;
	printf("IPs Found For Entered Location: \n");
	while(looper)
	{
		inet_ntop (looper->ai_family, looper->ai_addr->sa_data, addrstr, 2048);
		switch (looper->ai_family)
		{
			case AF_INET: //IP is type IPv4
			    ptr = &((struct sockaddr_in *) looper->ai_addr)->sin_addr;
			    break;
			case AF_INET6: //IP is type IPv6
			    ptr = &((struct sockaddr_in6 *) looper->ai_addr)->sin6_addr;
			    break;
        }

        inet_ntop (looper->ai_family, ptr, addrstr, 2048);

		if (looper->ai_family == PF_INET6)
        {
        	looper = looper->ai_next;
        	continue;
        }

        printf ("%d) IPv4 address: %s\n",numIps+1, addrstr);
        ipStr = calloc(strlen(addrstr), sizeof(char));
	    strcpy(ipStr, addrstr);
        numIps ++;
        looper = looper->ai_next;
    }

    if (numIps > 1)
    {
    	char * userInput = calloc(2048, sizeof(char));
    	printf("Please choose an IP Address: \n");
    	fgets(userInput,2047,stdin);
    	userInput[strlen(userInput)] = '\0';
    	//printf("User Choice: %d\n", atoi(userInput));
    	int choice = atoi(userInput);
    	if (choice < 1 || choice > numIps)
    	{
    		printf("Invalid user choice. Exiting.\n");
    		exit(-1);
    	}

    	for(int i = 0; i < choice; i++){
			inet_ntop (results->ai_family, results->ai_addr->sa_data, addrstr, 2048);
			switch (results->ai_family)
			{
				case AF_INET: //IP is type IPv4
				    ptr = &((struct sockaddr_in *) results->ai_addr)->sin_addr;
				    break;
				case AF_INET6: //IP is type IPv6
				    ptr = &((struct sockaddr_in6 *) results->ai_addr)->sin6_addr;
				    break;
	        }

			if (results->ai_family == PF_INET6)
	        {
	        	i --;
	        	continue;
	        }
	        else
	        {
	        	free(ipStr);
		        inet_ntop (results->ai_family, ptr, addrstr, 2048);
		        ipStr = calloc(strlen(addrstr), sizeof(char));
		        strcpy(ipStr, addrstr);
		    }
	        results = results->ai_next;
	    }

    	free(userInput);
    }

    printf("Selected Ip: %s\n", ipStr);
    return ipStr;
}
