def main():

   filePtr = open("input.txt", "r")

   rollingCounter = 0

   for line in filePtr:
      line=line.strip()
      
      leftSide = line.split(",")[0] #ex format: 1-2
      rightSide = line.split(",")[1] #ex format: 1-2

      if leftSide == rightSide:
         continue

      if (leftSide.split("-")[0] >= rightSide.split("-")[0]): #left MAY be within right side
         if(leftSide.split("-")[1] <= rightSide.split("-")[1]): #left IS inside right side
            rollingCounter += 1
      elif(rightSide.split("-")[0] >= leftSide.split("-")[0]): #right MAY be within left side
         if(rightSide.split("-")[1] <= leftSide.split("-")[1]): #right IS inside left side
            rollingCounter += 1
   print(rollingCounter)

   return




if __name__ == "__main__":
   main()












