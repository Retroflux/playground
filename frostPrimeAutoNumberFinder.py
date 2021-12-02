#!/usr/local/bin/python3

import sys
import requests
from time import sleep
from random import randrange
from bs4 import BeautifulSoup 


def main():


	headers={"authority":'cpt-api.twentypoo.com',
	"method":'GET',
	"path":'/numberGuesses/0',
	"scheme":'https',
	"accept":'application/json, text/plain, */*',
	"accept-encoding":'gzip, deflate, br',
	"accept-language":'en-CA,en;q=0.9',
	"cache-control":'no-cache',
	"cookie":'SID=s:H-YW5T9a-cIa31fJlIMIBXzqz7h1SWa6.mNJ/J5qDtNVbbiOX1INGs1e6hpjoYo2EJ7n7OLFwF5c',
	"origin":'https://www.twentypoo.com',
	"pragma":'no-cache',
	"referer":'https://www.twentypoo.com/',
	"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

	foundNumbers = 0


	print("hello")
	session = requests.Session() #create a new session
	maxGuesses = input("Enter the number of numbers you want to find:") 
	while foundNumbers < int(maxGuesses):
		currentNumber = randrange(10,1000000)
		headers = updateHeaders(headers, currentNumber)
		response = getWebpage(session,"https://cpt-api.twentypoo.com/numberGuesses/"+str(currentNumber),headers)
		print(response.status_code) #currently getting 401 error; invalid auth creds.
		json_data = response.json()
		if (len(json_data) < 1):
			print(currentNumber)
			foundNumbers+=1
		sleep(1)

	print("goodbye")

def updateHeaders(headers, currentNumber):

	headers={"authority":'cpt-api.twentypoo.com',
	"method":'GET',
	"path":'/numberGuesses/'+str(currentNumber),
	"scheme":'https',
	"accept":'application/json, text/plain, */*',
	"accept-encoding":'gzip, deflate, br',
	"accept-language":'en-CA,en;q=0.9',
	"cache-control":'no-cache',
	"cookie":'SID=s%3Axq-V96wUJpIMW4wnAvgdfgWNy6GdMbyy.5shPGqVN2Hs7y8Nyw3Hmz7R1TnUkIQDUjZ%2BPnVtEmXU',
	"origin":'https://www.twentypoo.com',
	"pragma":'no-cache',
	"referer":'https://www.twentypoo.com/',
	"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

	return headers

def getWebpage(session, url, headers):
    """Uses sessions to get the web content from a given URL and with 
    appropriate headers. Returns the web content if the session is 
    successful within 10 attempts'; otherwise, an error is raised 
    because the connection is (likely) permanently closed.

    session - A session instance for the email
    url - the URL that should be accessed
    headers - A dictionary of header information to be sent along
        in the GET request.
    """

    retries = 10
    last_connection_exception = None
    while retries:
        try:
            return session.get(url, headers = headers)
        except Exception as e:
            retries -= 1
            last_connection_exception = e
    raise last_connection_exception

currentNumber = 800000


if __name__ == '__main__':
	main()