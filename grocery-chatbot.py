import time
# list of stuff
fruits = ["apples", "oranges", "pears", "watermelon", "bananas", "pomegranate", "peach", "kiwi", "melon", "pumpkin", "honeydew", "starfruit", "dragonfruit", "apricot", "tangerines", "strawberries", "blueberries", "blackberries", "pineapple", "jicama", "cucumbers", "mandarins", "grapes", "green grapes", "lemon", "limes", "orange", "strawberry", "mango", "mangos", "tamarind", "tamarindo", "papaya", "mangoes", "cherries", "cherry"]

vegetables = ["broccoli", "cabbage", "tomatoes", "spinach", "cauliflower", "carrots", "corn", "peas", "potatoes", "little gems", "onion", "red onion", "radish", "celery", "beet", "sweet potato", "avocado", "eggplant", "asparagus", "artichokes", "pickle", "brussel sprouts"]

householdItems = ["soap", "aluminum foil", "aluminium foil", "plastic wrap", "saran wrap", "paper towels", "paper plates", "disposable plates", "foam plates", "dish soap", "mr. clean"]

pet = ["dog food", "cat food", "cat toys", "dog toys", "bird feeders"]

baby = ["baby formula", "baby bottles", "baby toys", "diapers", "baby food" "baby wipes"]

dry = ["beans", "lentils", "pasta", "rice", "black beans", "brown beans"]
# end of lists

#price and other variables
fruitPrice = 0.99
vegetablePrice = 0.79
householdPrice = 1.50
petPrice = 3.50
babyPrice = 4.75
dryPrice = 0.80
currentCart = []
currentPrice = []
cartTotal = []

def addProduct():
  print("Would you like to add this product to your cart?")
  answer = input().lower()
  if answer == "yes" or "y":
    currentCart.append(product)
    currentPrice.append(fruitPrice)
  print("Anything else?")
  product = input().lower()
# intro
print('''Hello my name is Itemizer! 
I am your interactive map and will help you find the products you need!
I am also able to add the products to your virtual cart to calculate the price of your trip.
When you are done, please respond with "done".
What are you currently looking for?''')

#start of process
product = input().lower()
while product != "done":
  if product in fruits:
    print("They're in aisle 5.")
    print("Their current price is: "+ str(fruitPrice))
    addProduct()
  elif product in vegetables:
    print("They're in aisle 6.")
    print("Their current price is: "+ str(vegetablePrice))
    addProduct()
  elif product in householdItems:
    print("They're in aisle 2.")
    print("Their current price is: "+ str(householdPrice))
   addProduct()
  elif product in pet:
    print("They're in aisle 7.")
    print("Their current price is: "+ str(petPrice))
    addProduct()
  elif product in baby:
    print("They're in aisle 8.")
    print("Their current price is: "+ str(babyPrice))
   addProduct()
    product = input().lower()
  elif product in dry:
    print("They're in aisle 3.")
    print("Their current price is: "+ str(dryPrice))
   addProduct()
  else:
    print("Are you sure you didn't make a typo?")
    print("Please type what you are looking for again.")
    product = input().lower()
if currentPrice != 0:
  for item in currentPrice:
    [float(i) for i in currentPrice]
  cartTotal = sum(currentPrice)
  tax = cartTotal*0.086
  totalPrice = tax + cartTotal
  roundedPrice= (round(totalPrice, 2))
  print("The items in your cart are: " +str(currentCart))
  print("Your estimated total (with a tax of 8.6%) of will be: "+ str(roundedPrice))
print("I hope I was able to help!")
time.sleep(5)