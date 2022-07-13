#include <stdio.h>
#include <errno.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <time.h>
#include <pthread.h>

#define DFULTREADSIZE 2048
#define DFULTPORTNUM 12052
#define NUM_THREADS 16

/*
 - Server Structs
*/

/* Used to pass the information into the thread from main */
typedef struct {
    int workerId;       // Equal to consocket value.
    int pThreadVal;     // Used to identify thread by number.
} ThreadArgs;

/*
 - Message List Structs
*/

/* SOME STUFF ABOUT List */
typedef struct {
    long totalFileSize;
    int totalReceived;
    int workerId;
    char nameOfFile[21];
} FileInfo;

/* SOME STUFF ABOUT List */
typedef struct ListNode {
    FileInfo msg;
    struct ListNode * next;
} FileTransferListNode;

/* List STUFF */
typedef struct {
    FileTransferListNode * head;
    FileTransferListNode * tail;
    pthread_mutex_t mutex;
    //Add a condition variable
    pthread_cond_t cond;
} FileTransferList;

/*
 - Server Functions
*/

//void intHandler(int num);             // Handles Sigint
int getPortNum(char * inBufferSize);    // Gets port number from buffer.
void * workerFunc(void * threadArg);    // Thread Work. Does single file transfer.

/*
 - Message List Functions
*/

void printList(FileTransferList * fileList);  // Prints List
FileTransferList* createFileTransferList(); //holds the list of all of the files, shared with all threads.
FileTransferListNode * createFileTransferListNode(float fileSize, int workerId, char * fileName);
void addFileToList(FileTransferList * inList, FileTransferListNode * toAdd);
void updateTransferListNodeReceived(FileTransferListNode * toUpdate, int totalReceived);
void removeFromFileList(FileTransferList * inList, FileTransferListNode * toRemove); //convert to removeFileFromList
void * uiFunct();

/*
 - GLOBAL VARIABLES :3
*/

FileTransferList * currentFileTransferList;   // List of all the threads.
int usedThreads[NUM_THREADS] = {0};           // Keep track of all thread's state.
pthread_t childThread[NUM_THREADS];           // Array of threads.
int softExit = 0;                             // Allow / Reject Connections

int main(int argc, char * argv[])
{
    int * consocketM = calloc(1, sizeof(int));
    int portNum = DFULTPORTNUM;

    if (argc != 2)
    {
        printf("Invalid Arguments. Expecting ./server <port number>\n");
        exit(-1);
    }

    //signal(SIGINT, intHandler);   //Catches ctrl+c

    currentFileTransferList = createFileTransferList();
    portNum = getPortNum(argv[1]);

    struct sockaddr_in dest;      //Socket info about the machine connecting to us
    struct sockaddr_in serv;      //Socket info about our server
    int mysocket;                 //Socket used to listen for incoming connections
    socklen_t socksize = sizeof(struct sockaddr_in);

    memset(&serv, 0, sizeof(serv));              //Zero the struct before filling the fields

    serv.sin_family = AF_INET;                   //Use the IPv4 address family
    serv.sin_addr.s_addr = htonl(INADDR_ANY);    //Set our address to any interface *CHANGE THIS TO AN ARGV THING
    serv.sin_port = htons(portNum);              //Set the server port number *CHANGE TO AN ARGV THING

    mysocket = socket(AF_INET, SOCK_STREAM, 0);  //Create the socket TCP & IPv4

    if (bind(mysocket, (struct sockaddr *)&serv, sizeof(struct sockaddr)) != 0)
    {
        printf("Unable to open TCP socket on localhost: %d\n", portNum);
        printf("%s\n", strerror(errno));
        close(mysocket);
        return 0;
    }

    pthread_t uiThread;
    pthread_create(&uiThread, NULL, uiFunct, NULL);

    printf("Listening on port %d\n", portNum);
    listen(mysocket, NUM_THREADS);  //Listen to socket with 1 pending connection allowed
    if (softExit == 0)
    {
        (*consocketM) = accept(mysocket, (struct sockaddr *)&dest, &socksize);
    }

    while(1)
    {
        //printf("=-= Incoming connection from %s \n", inet_ntoa(dest.sin_addr));

        /* Setup Thread information struct to send with thread on creation. */
        ThreadArgs * args = calloc(1, sizeof(ThreadArgs));
        args->workerId = (*consocketM);
        int foundThread = 0;
        
        //If more than NUM_THREADS is required, wait until a thread is finished.
        while(foundThread == 0)
        {
            for (int i = 0; i < NUM_THREADS; i++)
            {
                if(usedThreads[i] == 0)
                {
                    args->pThreadVal = i;
                    usedThreads[i] = 1;
                    foundThread = 1;
                    //printf("Thread %d is being created! :D\n", i);
                    pthread_create(&(childThread[i]), NULL, workerFunc, args);  
                    break;
                }
            }
        }
        /* New Thread deals with file transfer. Server continues to listen for new connections. */
        if (softExit == 0)
        {
            consocketM = calloc(1,sizeof(int));
            (*consocketM) = accept(mysocket, (struct sockaddr *)&dest, &socksize);
        }
    }
    return EXIT_SUCCESS; //Will never run. Added ctrl+c for cleanup
}

/*
 - Server Functions
*/

int getPortNum(char * inBufferSize)
{
    int buffer = 0;
    sscanf(inBufferSize, "%d", &buffer);
    if (buffer < 1)
    {
        printf("Invalid Argument. Expecting numeric port > 0 for argv[2].\n");
        exit(EXIT_FAILURE);
    }
    return buffer;
}

// void intHandler(int num)
// {
//     close(consocket);
//     exit(0);
// }

void * uiFunct()
{
    char userInput = '\0';
    printf("Welcome to CIS 3210 File Transfer Server\n");
    printf("Input options:\n\t- d: List of current file transfers.\n\t- e: exit\nYour Input: ");
    while(scanf(" %c",&userInput) != 'e')
    {
        switch(userInput)
        {
            case 'd':
                printList(currentFileTransferList);
                break;
            case 'e':
                printf("Please select type of exit:\n\t- s: Soft Exit\n\t- h: Hard Exit\n");
                scanf(" %c",&userInput);
                while(userInput != 's' && userInput != 'h')
                {
                    scanf(" %c",&userInput);
                }

                if(userInput == 's')
                {
                    softExit = 1;
                    for (int i = 0; i < NUM_THREADS; i++)
                    {
                        if (usedThreads[i] == 1)
                        {
                            pthread_join(childThread[i], NULL);
                        }
                    }
                    exit(0);
                    return NULL;
                }
                else{
                    exit(0);
                }
                break;
            default:
                printf("\nInvalid Input. Please refere to the menu for commands.\n");
        }
        printf("Input options:\n\t- d: List of current file transfers.\n\t- e: exit\nYour Input: ");
    }
    return NULL;
}

void * workerFunc(void * threadArg)
{
    ThreadArgs * args = (ThreadArgs*)threadArg;
    int consocket = args->workerId;
    int len = 0;
        
    char * buffer = calloc(38, sizeof(char)); //Set Reciev Buffer
    while (len < 37)
    {
        //printf("PEEKING! %d *eyes* %d on %d\n", len, consocket, args->workerId);
        len = recv(consocket, buffer, 37, MSG_PEEK); //Look at first send, expecting header info w/ other content
        //fprintf(stderr, "recv: %s (%d)\n", strerror(errno), errno);
    }
    free(buffer);

    long totalFileSize = 0;
    long maxReceiveLength = DFULTREADSIZE;  //Default recieve size to 2048
    char * rawFileName = calloc(21, sizeof(char));
    char * fileName = calloc(28, sizeof(char));

    len = recv(consocket, &totalFileSize, sizeof(long), 0); //Get file size
    len = recv(consocket, &maxReceiveLength, sizeof(long), 0); //Get chunk size
    len = recv(consocket, rawFileName, 21, 0); //Get file name
    sscanf(rawFileName, "%[^:]", fileName);
    free(rawFileName);
    strcat(fileName, "_out");
    char idTOStr[3];
    sprintf(idTOStr,"%d",args->pThreadVal);
    strcat(fileName, idTOStr);
    fileName[strlen(fileName)] = '\0';
    //printf("File Name: %s | Packet Size: %ld | Total Size: %ld\n", fileName, maxReceiveLength, totalFileSize);

    int totalReceived = 0;
    buffer = calloc(maxReceiveLength + 1, sizeof(char));
    FILE * fp = fopen(fileName,"w+");
    
    if (fp == NULL)
    {
        printf("Unable to create file %s\n", fileName);
        close(args->workerId);
        exit(0);
    }

    FileTransferListNode * currListNode = createFileTransferListNode(totalFileSize, args->pThreadVal, fileName);
    addFileToList(currentFileTransferList, currListNode);

    while (totalReceived < totalFileSize)
    {
        len = recv(args->workerId, buffer, maxReceiveLength+1, 0);
        if (len > 0)
        {
            buffer[len] = '\0';
            // printf("Received:%s\n",buffer);
            fputs(buffer, fp);
            totalReceived += strlen(buffer);
            updateTransferListNodeReceived(currListNode, totalReceived);
            //printf("ConSocket: %d and Thread: %d ~~~ Total Received: %d TotalSize: %ld\n", args->workerId, args->pThreadVal, totalReceived, totalFileSize);
        }
    }
    //printf("Closing consocket %d\n",args->workerId);
    close(args->workerId);
    fclose(fp);
    removeFromFileList(currentFileTransferList, currListNode);
    usedThreads[args->pThreadVal] = 0;
    free(fileName);
    free((ThreadArgs*)threadArg);
    free(buffer);
    return NULL;
}

/*
 - Message List Functions
*/

void printList(FileTransferList * inList)
{
    pthread_mutex_lock(&inList->mutex);
    FileTransferListNode * tempPtr = inList->head;
    printf("+----------+--------------------------------+------------------+-------------------------+\n");
    printf("| Thread # |            File Name           |    File Size     |      Bytes Received     |\n");
    printf("+----------+--------------------------------+------------------+-------------------------+\n");
    
    if (tempPtr == NULL)
    {
            printf("|          |                                |                  |                         |\n");
    }

    while (tempPtr != NULL){
        int transferProgress = ((float)tempPtr->msg.totalReceived/(float)tempPtr->msg.totalFileSize)*100;
        printf("| %8d | %30s | %16ld | %16d (%3d%%) |\n",tempPtr->msg.workerId, tempPtr->msg.nameOfFile, tempPtr->msg.totalFileSize, tempPtr->msg.totalReceived, transferProgress);
        tempPtr = tempPtr->next;
    }
    printf("+----------+--------------------------------+------------------+-------------------------+\n");
    pthread_cond_signal(&inList->cond);
    pthread_mutex_unlock(&inList->mutex);
    return;
}

//Create a List and initilize its mutex and condition variable
FileTransferList * createFileTransferList()
{
    FileTransferList * newList = calloc(1, sizeof(FileTransferList));
    newList->head = NULL;
    newList->tail = NULL;
    pthread_mutex_init(&newList->mutex, NULL);
    pthread_cond_init(&newList->cond, NULL);
    return newList;
}

FileTransferListNode * createFileTransferListNode(float fileSize, int workerId, char * fileName)
{
    FileTransferListNode * newListNode = calloc(1, sizeof(FileTransferListNode));
    newListNode->msg.totalFileSize = fileSize;
    newListNode->msg.totalReceived = 0;
    newListNode->msg.workerId = workerId;
    strcpy(newListNode->msg.nameOfFile, fileName);
    newListNode->next = NULL;
    return newListNode;
}

//"Send" a message - append it onto the List
void addFileToList(FileTransferList * inList, FileTransferListNode * toAdd)
{
    pthread_mutex_lock(&inList->mutex);

    toAdd->next = NULL;

    if (inList->head == NULL)
    {
        inList->head = toAdd;
    }
    else
    {
        inList->tail->next = toAdd;
    }
    
    inList->tail = toAdd;

    //Signal the consumer thread waiting on this condition variable
    pthread_cond_signal(&inList->cond);
    pthread_mutex_unlock(&inList->mutex);

    return;
}

void updateTransferListNodeReceived(FileTransferListNode * toUpdate, int totalReceived)
{
    if (toUpdate != NULL)
    {
        toUpdate->msg.totalReceived = totalReceived;
    }
    return;
}

void removeFromFileList(FileTransferList * inList, FileTransferListNode * toRemove)
{
    FileTransferListNode * currNode = inList->head;
    
    //Case where first node is item.
    if (currNode->msg.workerId == toRemove->msg.workerId)
    {
        inList->head = currNode->next;
        return;
    }

    FileTransferListNode * prevNode = NULL;
    //Iterate through the list to find the file
    while (currNode != NULL)
    {
        prevNode = currNode;
        currNode = currNode->next;
        if (currNode->msg.workerId == toRemove->msg.workerId)
        {
            pthread_mutex_lock(&inList->mutex);

            prevNode->next = currNode->next;
            currNode->next = NULL;

            //Signal the consumer thread waiting on this condition variable
            pthread_cond_signal(&inList->cond);
            pthread_mutex_unlock(&inList->mutex);

            return;
        }
    }
    return;
}