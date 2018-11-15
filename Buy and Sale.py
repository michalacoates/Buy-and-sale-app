print("Welcome to Buy & Sale")
# input ("Would you like to buy Ramen or Water"):

def collectInput(q):
    i = input(q)
    return i

answer = collectInput("Would you like to buy Ramen, Water, or Hot Pockets?")
answer2 = collectInput("How many do you need?")
answer3 = collectInput("How much are you willing to spend??")
answer4 = collectInput("So you would like " + answer + ", you need to have "+ answer2 + " and you're willing to spend " + answer3)
l = []
l.append(answer)
l.append(answer2)
l.append(answer3)
l.append(answer4)

print (l)
