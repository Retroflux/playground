
def main():
   
   filePtr = open("input.txt", 'r')

   rollingSum = 0

   fileList = list()

   for line in filePtr:
      fileList.append(line.strip())

   #part 1
   for line in fileList:

      halfArray = int(len(line)/2)
      leftSide = line[halfArray:]
      rightSide = line[:halfArray]

      foundDuplicates = list()
      for character in leftSide:
         if character in rightSide:
            if character not in foundDuplicates:
               rollingSum += convert_character_to_score(character)
               foundDuplicates.append(character)
   print(rollingSum)

   #part 2
   rollingSum = 0
   for i in range(0,len(fileList)-1,3):
      firstLine = fileList[i]
      secondLine = fileList[i+1]
      thirdLine = fileList[i+2]

      for character in firstLine:
         if character in secondLine:
            if character in thirdLine:
               rollingSum += convert_character_to_score(character)
               break
            else:
               continue
         else:
            continue
               
   print(rollingSum)
   return


def convert_character_to_score(character):

   if (character.isupper()):
      return ord(character) - 38
   return ord(character) - 96






if __name__ == '__main__':
    main()