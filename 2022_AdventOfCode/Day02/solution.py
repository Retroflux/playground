
def main():

    totalScore = 0

    filePtr = open("input.txt", "r")

    for line in filePtr:

        line = line.strip()

        #break on empty final line
        if line != "":
            #split input line
            opponent = line.split(" ")[0] #A, B, or C
            # response = convert_response_to_opponent(line.split(" ")[1]) # converted to A, B, or C from X,Y,Z
            response = line.split(" ")[1] #X, Y, or Z

            #summates the points per round of RPC
            response = convert_to_win_loss_or_tie(opponent, response)
            totalScore += is_win_loss_or_tie(opponent, response)
            totalScore += convert_to_integer_for_RPC(response)
    print(totalScore)

    return totalScore

def convert_to_win_loss_or_tie(opponent, response):
    #check the opponent's value
    #check our response (is_win_loss_or_tie)

    if response == "X": #lose
        if(opponent == "A"):
            return "C"
        elif(opponent == "B"):
            return "A"
        else:
            return "B"
    if response == "Z": #win
        if(opponent == "A"):
            return "B"
        elif(opponent == "B"):
            return "C"
        else:
            return "A"
    return opponent # tie case





def convert_response_to_opponent(value):
    if (value == "X"):
        return "A"
    elif(value == "Y"):
        return "B"
    else:
        return "C"


def is_win_loss_or_tie(opponent, response):
    # tie
    if opponent == response:
        return 3

    #wins
    if opponent == "A" and response == "B":
        return 6
    elif opponent == "B" and response == "C":
        return 6
    elif opponent == "C" and response == "A":
        return 6

    return 0 #losses


def convert_to_integer_for_RPC(value):

    #Inputs: A, B, C
    #Outputs: 1, 2, 3

    if (value == "A"):
        return 1
    elif(value == "B"):
        return 2
    return 3



if __name__ == '__main__':
    main()