
def main():
	#where your code exists
	listOfColumnTallies = initializeList()
	lineCounter = 0

	for line in file:
		listOfColumnTallies = separateAndSumColumns(line, listOfColumnTallies)
		lineCounter+=1
#TODO
	#Takeaways:
		#WRITE THINGS DOWN BEFORE YOU CODE
		#Functions are friends
			#CAVEAT: working functions are friends - please test your functions
		#Always ask: can I remove duplicate code
		#Always ask: Is there a better way to do this?
		#Always ask: Do I need help?
			#CAVEAT: Do I still want to learn more?

	#assume there's 1000 lines in the file
		#col1: 345
		#col2: 512
		#col3: 800
		#4:		523
		#5:		122
		#6:		950
		#7:		753
		#8:		642
		#9:		225
		#10:	695	
		#11:	735	
		#col12: 499
	gammmmmma = gammmmmma + '0'
	gammmmmma = gammmmmma + '1'
	
	#after all lines are read, don't need file anymore
	#next, 


def separateAndSumColumns(line, listOfColumnTallies):
	for i in range(0,len(line)):
		int(listOfColumnTallies[i]) += int(line[i])
	return listOfColumnTallies

def getMaxForColumns(listOfColumnTallies):
	#for each column in the list:
		#execute maxVal(closed box), returns results per columns
			#What you have:
			#-still have the list of tallies
			#-either a one or a zero per column
			# Is there a way to use typecasting to simplify the generation of gamma?
				#Hint: how many lines are in the data file?
				#Hint2: Do you have to work with just integers? What about strings? 
	#once you have maxVal, need to store is somewhere

def initializeList():
	tempList = list()

	for i in range(0,11) #make sure this is 12 things long
		tempList.append(0) #create 12 empty number holders

	return tempList





















if __name__ == '__main__':
	main()