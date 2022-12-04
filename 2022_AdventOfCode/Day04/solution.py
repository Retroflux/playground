def main():

   filePtr = open("input.txt", "r")

   rollingCounter = 0 #part 1 counter
   secondCounter = 0 #part 2 counter

   for line in filePtr:
      
      #format and split input
      line=line.strip()
      leftSide = line.split(",")[0] #ex format: 1-2
      rightSide = line.split(",")[1] #ex format: 1-2

      #typecast to int
      left_min = int(leftSide.split("-")[0]) 
      left_max = int(leftSide.split("-")[1])
      right_min = int(rightSide.split("-")[0]) 
      right_max = int(rightSide.split("-")[1])


      #part 1
      if(left_min <= right_min and left_max >= right_max):
         rollingCounter+=1
      elif(right_min <= left_min and right_max >= left_max):
         rollingCounter+=1

      #part 2 - use negations to confirm no overlap
      if(left_min > right_max or right_min > left_max):
         continue
      elif(right_max < left_min or left_max < right_min):
         continue
      else:
         secondCounter+=1

   print(rollingCounter)
   print(secondCounter)

   return




if __name__ == "__main__":
   main()












