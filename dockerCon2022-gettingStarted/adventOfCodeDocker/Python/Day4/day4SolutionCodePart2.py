#!/usr/bin/python3
#each row is just a set of five of sequential numbers
#	ex. row1 = 0->4
#		row2 = 5->9
#		etc.
#each column is just the set of five numbers where y = 5x + i, where {i,x}={0,1,2,3,4}
#	ex. 
#		i=0     i=1     i=2     i=3     i=4
#	x=0 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i    
#	x=1 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  
#	x=2 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  
#	x=3 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  
#	x=4 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  


#>Boards are hardcoded in size, so each board will have ten possible win conditions that can be stored in two(?) lists.
#>When number is called, search the board strings for the number, identify its position number, and then find its row and col using math for each matching board
#	>replace the called index with an "X" and check that row and column (ex. row 2 and col 3) for all X's. 

#Can condense the 2x2 array into a 2n list
	# 0,0 = 0; 0,1 = 1; ... 2,1 = 11


	# 1  2  3  4  5
	# 6  7  8  9  10
	# 11 12 13 14 15
	# 16 17 18 19 20
	# 21 22 23 24 25

from classes.BingoCard import BingoCard

def main():

	listOfBingoCards = list()
	listOfWinningNumbers = list()
	firstLineFlag = 0
	checkRowsForBingo = 0
	checkColumnsForBingo = 0
	offsetTracker = 0
	i = 0
	j = 0
	x = 0
	bingoCardCounter = 0
	winningBingoCardNumber = 0
	penultimateWinningNumber = 0
	winningNumber = 0
	summationOfRemainingBingoNumbers = 0

	with open("input.txt","r") as fp:
		for line in fp:
			if firstLineFlag == 0:
				listOfWinningNumbers=list(line.strip().split(","))
				print(listOfWinningNumbers)
				firstLineFlag += 1
				next(fp)
			else:
				print("Making Bingo Card")
				print(line)
				bingoString = str()
				for i in range(0,5):
					bingoString += line.strip() + " "
					try:
						line = next(fp)
					except StopIteration as e:
						pass
				print(bingoString)
				listOfBingoCards.append(BingoCard(bingoString,bingoCardCounter))
				bingoCardCounter += 1

	for bingoCard in listOfBingoCards:
		bingoCard.BingoCardValues = bingoCard.BingoCardValues.split()
		print(bingoCard.BingoCardValues)

	while(len(listOfBingoCards) > 1):
		penultimateWinningNumber = findLosingBingoCard(listOfWinningNumbers,listOfBingoCards)
		# listOfBingoCards = fixBingoCardNumbers(listOfBingoCards)
	(winningBingoCardNumber,winningNumber) = findWinningBingoCard(listOfWinningNumbers,listOfBingoCards)
	
	if (penultimateWinningNumber == -1):
		print("Fatal Error: Ya dun' goofed")

	for number in listOfBingoCards[0].BingoCardValues:
		if (number == 'X'):
			pass
		else:
			print(number)
			summationOfRemainingBingoNumbers += int(number.strip())
	
	print(f"Summation of the remaining bingo numbers is {summationOfRemainingBingoNumbers}")
	finalValue = int(winningNumber) * summationOfRemainingBingoNumbers
	print(f"Final Value: {finalValue}")

	#Testing Print
	for bingoCard in listOfBingoCards:
		print("\n\n\n")
		for i in range(0,5):
			print(bingoCard.BingoCardValues[5*i:(5*i)+5])

def findLosingBingoCard(listOfWinningNumbers,listOfBingoCards):
	i = 0
	j = 0
	currMax = 0
	matchFound = 0
	boardsRemoved = 0
	for winningNumber in listOfWinningNumbers:
		j=0
		currMax = len(listOfBingoCards)
		while j < currMax:
			for i in range(0,len(listOfBingoCards[j].BingoCardValues)):
				if (listOfBingoCards[j].BingoCardValues[i] == winningNumber):
					listOfBingoCards[j].BingoCardValues[i] = 'X'
					checkRowsForBingo = checkRowsForCompletion(listOfBingoCards[j])
					checkColumnsForBingo = checkColumnsForCompletion(listOfBingoCards[j])
					if(checkRowsForBingo or checkColumnsForBingo):
						del listOfBingoCards[j]
						j-=1
						currMax-=1
						matchFound = 1
						break
			j+=1
		if(matchFound == 1):
			return winningNumber


def findWinningBingoCard(listOfWinningNumbers,listOfBingoCards):
	i = 0

	for winningNumber in listOfWinningNumbers:
		for bingoCard in listOfBingoCards:
			for i in range(0,len(bingoCard.BingoCardValues)):
				if (bingoCard.BingoCardValues[i] == winningNumber):
					# print(f"Found cell match of {bingoCard.BingoCardValues[i]} and {winningNumber}")
					bingoCard.BingoCardValues[i] = 'X'
					checkRowsForBingo = checkRowsForCompletion(bingoCard)
					checkColumnsForBingo = checkColumnsForCompletion(bingoCard)
					if(checkRowsForBingo or checkColumnsForBingo):
						print(f"Winning Bingo Found: Card Number {bingoCard.BingoCardNumber}")
						print(f"Winning Number:{winningNumber}")
						return (bingoCard.BingoCardNumber,int(winningNumber))
	return -1

def fixBingoCardNumbers(listOfBingoCards):
	i = 0

	for card in listOfBingoCards:
		card.BingoCardNumber = i
		i+=1
	return listOfBingoCards

def checkRowsForCompletion(bingoCard):
	i = 0 
	j = 0

	for i in range(0,25,5):
		counter = 0
		for j in range(i,i+5):
			if bingoCard.BingoCardValues[j] == 'X':
				counter += 1
		if counter == 5:
			return True
	return False	
	
def checkColumnsForCompletion(bingoCard):
	#y=5x+i

	for i in range(0,5):
		counter = 0
		for j in range(0,5):
			if(bingoCard.BingoCardValues[(5*j)+i] == 'X'):
				counter +=1
		if counter == 5:
			return True			
	return False	


if __name__ == '__main__':
	main()