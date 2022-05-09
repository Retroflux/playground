#!/usr/bin/python3

from classes.bitClass import Bit
import copy

def main():

	listOfBits = list()
	fileInList = list()
	totalNumberOfRows = 0
	positionCounter = 0
	gammaBitString = ""
	epsilonBitString = ""
	gammaInDecimal = 0
	epsilonInDecimal = 0
	powerConsumptionValue = 0

	#Part 2 Specific Variables
	lifeSupportRatingList = list()
	lifeSupportMetricValue = ""
	lifeSupportRatingValue = 0
	oxygenInDecimal = 0
	carbonDioxideInDecimal = 0

	with open("input.txt","r") as fp:
		for line in fp:
			line = line.strip()
			positionCounter = 0
			for i in range(0,len(line)):
				colExists = CheckIfColExists(listOfBits,positionCounter)
				if (colExists == False):
					listOfBits.append(generateNewColumn(positionCounter))
				if(int(line[i]) == 1):
					listOfBits = addToBitColumnCounter(listOfBits,positionCounter)
				positionCounter += 1
			totalNumberOfRows += 1
			fileInList.append(line)
	
	#Now have a list of counts for all 1's in each column. Should be in column order, but will sort for sanity's sake
	sortedListOfBits = sorted(listOfBits,key=lambda Bit: Bit.bitColumn)

	gammaBitString = createGammaString(sortedListOfBits,totalNumberOfRows)
	epsilonBitString = invertGammaBitStringForEpsilonString(gammaBitString)

	gammaInDecimal = convertBitStringToDecimal(gammaBitString)
	epsilonInDecimal = convertBitStringToDecimal(epsilonBitString)

	print(f"gammaBitString: {gammaBitString}, output from decimal calculation is {gammaInDecimal}")
	print(f"epsilonBitString: {epsilonBitString}, output from decimal calculation is {epsilonInDecimal}")

	print(f"E+G bit strings will XOR into a string of all 1's, so the sum of their decimal conversions should one less than (2^",len(sortedListOfBits),f")-1: Their sum is: {gammaInDecimal + epsilonInDecimal}")


	powerConsumptionValue = gammaInDecimal * epsilonInDecimal

	print(f"The Power Consumption found in the submarine's diagnostic report is {powerConsumptionValue}")

	#Oxygen and CO2 scrubbing begins

	print("\n\nNow Measuring Oxygen and Carbon Dioxide\n")
	lifeSupportRatingList = copy.deepcopy(fileInList)
	for i in range(0,len(sortedListOfBits)):
		print(f"Current column:{i}, len of inputList:" + str(len(lifeSupportRatingList)))
		if (len(lifeSupportRatingList) == 1):
			print("\tResult found, exiting loop")
			break
		tempListCountOfOnes = 0
		for line in lifeSupportRatingList:
			if (line[i] == '1'):
				tempListCountOfOnes+=1
		if tempListCountOfOnes >= (len(lifeSupportRatingList)/2):
			print("\tOnes >= Zeroes, removing zero case")
			lifeSupportRatingList = removeLeastPopularBit(lifeSupportRatingList,0,i)

		else:
			print("\tZeroes > Ones, removing ones case")
			lifeSupportRatingList = removeLeastPopularBit(lifeSupportRatingList,1,i)

	lifeSupportMetricValue=lifeSupportRatingList[0]
	oxygenInDecimal = convertBitStringToDecimal(lifeSupportMetricValue)
	print(f"Oxygen Result in binary:{lifeSupportMetricValue}, in decimal: {oxygenInDecimal}\n")

	lifeSupportRatingList = copy.deepcopy(fileInList)
	for i in range(0,len(sortedListOfBits)):
		print(f"Current column:{i}, len of inputList:" + str(len(lifeSupportRatingList)))
		if (len(lifeSupportRatingList) == 1):
			print("\tResult found, exiting loop")
			break
		tempListCountOfOnes = 0
		for line in lifeSupportRatingList:
			if (line[i] == '1'):
				tempListCountOfOnes+=1
		if tempListCountOfOnes < (len(lifeSupportRatingList)/2):
			print("\tOnes < Zeroes, removing zeroes case")
			lifeSupportRatingList = removeLeastPopularBit(lifeSupportRatingList,0,i)

		else:
			print("\tZeroes <= Ones, removing ones case")
			lifeSupportRatingList = removeLeastPopularBit(lifeSupportRatingList,1,i)
	
	lifeSupportMetricValue=lifeSupportRatingList[0]
	carbonDioxideInDecimal = convertBitStringToDecimal(lifeSupportMetricValue)
	print(f"Carbon Dioxide Result in binary:{lifeSupportMetricValue}, in decimal: {carbonDioxideInDecimal}\n")

	lifeSupportRatingValue = carbonDioxideInDecimal * oxygenInDecimal
	print(f"Calculation Complete: Life Support Rating: {lifeSupportRatingValue}")


def generateNewColumn(colValue):
	return Bit(colValue,0)


def CheckIfColExists(listOfBits, colValue):
	for bitObject in listOfBits:
		if(bitObject.bitColumn == colValue):
			return True
	return False


def addToBitColumnCounter(listOfBits,colValue):
	for i in range(0,len(listOfBits)):
		if (listOfBits[i].bitColumn == colValue):
			listOfBits[i].count+=1
			return listOfBits
	print(f"Error Occurred - Iterated through entire list and could not find match to bitColumn: {colValue}")
	return(listOfBits)

def createGammaString(sortedListOfBits,totalNumberOfRows):
	gammaBitString = ""
	for column in sortedListOfBits:
		if (column.count > totalNumberOfRows - column.count):
			print(f"For column {column.bitColumn} there are more 1's than 0's ({column.count} vs {totalNumberOfRows - column.count})")
			gammaBitString = gammaBitString + "1"
		else:
			print(f"For column {column.bitColumn} there are more 0's than 1's ({column.count} vs {totalNumberOfRows - column.count})")
			gammaBitString = gammaBitString + "0"
	return gammaBitString

def invertGammaBitStringForEpsilonString(gammaBitString):
	epsilonBitString = ""
	for i in range(0,len(gammaBitString)):
		if(gammaBitString[i] == '1'):
			epsilonBitString = epsilonBitString + "0"
		else:
			epsilonBitString = epsilonBitString + "1"
	return epsilonBitString		

def convertBitStringToDecimal(bitString):
	convertedDecimalValue = 0
	exponentialFactor = 0

	for i in range(len(bitString)-1,-1,-1):
		convertedDecimalValue += int(bitString[i])*(2**exponentialFactor)
		exponentialFactor+=1
	return convertedDecimalValue

def removeLeastPopularBit(inputList,bitValueToRemove,colValue):
	i = 0
	while(i < len(inputList)):
		if(inputList[i][colValue] == str(bitValueToRemove)):
			del inputList[i]
			i-=1
		i+=1
	return inputList


if __name__ == '__main__':
	main()