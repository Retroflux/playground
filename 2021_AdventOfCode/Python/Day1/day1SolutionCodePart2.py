#!/usr/bin/python3


filePtr = open("input.txt","r")

previousNumber = -1
previousSummation = 0
currentNumber = 0
greaterThanCounter = 0
currentSummation = 0
oldestNumber = 0
initialLoop = 0
for line in filePtr:
	currentNumber = int(line.strip())
	if (initialLoop < 2):
		print("We made it to case 1")
		currentSummation += currentNumber
		initialLoop+=1
	else:
		if(previousSummation < 1):
			print(f"{currentSummation + currentNumber} (N/A - no previous sum)")
		elif (currentSummation + currentNumber > previousSummation):
			print(f"{currentSummation + currentNumber} (increased)")
			greaterThanCounter += 1
		elif (currentSummation + currentNumber < previousSummation):
			print(f"{currentSummation + currentNumber} (decreased)")
		else:
			print(f"{currentSummation + currentNumber} (no change)")
		oldestNumber = currentSummation - previousNumber
		currentSummation = previousNumber + currentNumber
		previousSummation = currentSummation + oldestNumber
	previousNumber = currentNumber

print(f"Larger measurements: {greaterThanCounter}")