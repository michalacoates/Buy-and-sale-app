print("Welcome to Buy & Sale")
# input ("Would you like to buy Ramen or Water"):

def collectInput(q):
    i = input(q)
    return i

answer = collectInput("Would you like to buy Water, Snacks, Supplies, or Ramen?")
answer2 = collectInput("How many do you need?")
answer3 = collectInput("How much are you willing to spend??")
answer4 = collectInput("So you would like " + answer + ", you need to have "+ answer2 + " and you're willing to spend " + answer3)

l = []
l.append(answer)
l.append(answer2)
l.append(answer3)
l.append(answer4)

print (l)


items = {
    "Water" : {"Poland Spring" : [4.39, 24+"pack"], "Fiji" : [15.99, 4+"pack"], "Smart Water" : [14.99, 12+"pack"]},
    "Snacks" : {"Oreos" : [3, 36+"cookies"],
        "Spicy Nacho Cheese Doritos" : [4.29, 1+"bag"],
        "Cool Ranch Doritos" :[4.29, 1+"bag"],
        "M&M Variety Pack" : [19.79, 18+"pack"]},
    "supplies" : {},
    "Ramen" : {}
}

water = items["water"]
poland = water["Poland Spring"]

print(items["water"]["Poland Spring"][0])

# Rce cakes ($2.69), lucky charms ($3.49), Instant Coffee (3.87), Lipton Tea (7.04), Hummus ($13.99), Pita Chips ($14.69)
<html>
  <head>
    <title>Buy and Sell!</title>
  </head>
  <body>
    <h1>Buy and Sell!!</h1>
    This is it!
  </body>
</html>
<html>
  <head>
    <title>My first page!</title>
  </head>
  <body>
    <h1>Tim's page!!</h1>
    This is it!
    <br>
    What part of your body do you want to focus on?
    <br>
    <input type="text" name="bodypart" >
    <br>
    <button name="send">Submit</button>
    
  </body>
</html> 
<html>
  <head>
    <title>My first page!</title>
  </head>
  <body>
    <h1>Tim's page!!</h1>
    This is it!
  </body>
</html>
