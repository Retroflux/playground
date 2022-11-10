#!/usr/bin/python3


filePtr = open("input.txt","r")

previousNumber = -1
currentNumber = 0
greaterThanCounter = 0

for line in filePtr:
	currentNumber = int(line.strip())
	if (previousNumber < 0):
		print(f"{currentNumber} (N/A - no previous measurement)")
	else:
		if (currentNumber > previousNumber):
			print(f"{currentNumber} (increased)")
			greaterThanCounter += 1
		elif (currentNumber < previousNumber):
			print(f"{currentNumber} (decreased)")
		else:
			print(f"{currentNumber} (no change)")

	previousNumber = currentNumber

print(f"Larger measurements: {greaterThanCounter}")