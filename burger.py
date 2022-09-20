from SlickNLU import SlickNLU, interpret

dictionaries = {}

dictionaries["intent"] = """
add_order: I'll take, I take, I'll want, I want, I'll have, I'd like, I'd like to have, I'd like to order, order, add, gimme, plus, extra, more, also, May I have
"""

dictionaries["main"] = """
Big Mac
Quarter Pounder with Cheese: Quarter Pounder with Cheese, Quarter Pounder
Double Quarter Pounder with Cheese
Quarter Pounder with Cheese Deluxe
McDouble: McDouble, Mac Double
Quarter Pounder with Cheese Bacon
Spicy Deluxe Crispy Chicken Sandwich
Crispy Chicken Sandwich
Spicy Crispy Chicken Sandwich
Deluxe Crispy Chicken Sandwich
Chicken McNuggets
McChicken
Hamburger: Hamburger, regular hamburger, normal hamburger, classic hamburger
Cheeseburger: Cheeseburger, cheese burger
Egg McMuffin: Egg McMuffin, McMuffin, Mc Muffin, Mac Muffic
Chicken Mc Grill
Veggie Burger
"""

dictionaries["sides"] = """
fries: fries, french fries
salad: side salad, salad
sweet potato fries
Apple Slices
"""

dictionaries["combo"] = """
happy meal
meal: meal, combo
"""

dictionaries["beverage"] = """
Coke
cola
Coca Cola
Coca Cola zero
Coca Cola light
Diet Coke
Fanta
water
soda water
bubble
orange juice
"""

dictionaries["amount"] = """
one
two
three
four
five
six
seven
eight
nine
ten
twenty
fourty
"""

dictionaries["size"] = """
small
medium: medium, regular
large: large, super size
"""

dictionaries["profanity"] = """
fuck you
fucker
fuck
bitch
son of a bitch
"""

dictionaries["serving"] = """
to go: to go, take away, outside, take with me
eat in: eat in, here, in restaurant, in the restaurant, inside
"""
  
nlu = SlickNLU(dictionaries)

interpret(nlu, "Good evening, sir, I'd like to have a Big Mac meal with french fries and a large Coke. Plus an extra cheese burger and large fries. Oh, it'll be to go. And one more Fanta. Could I also have a bottle of water, please? And fuck you, too!")
interpret(nlu, "A coke, please.")
interpret(nlu, "Big mac meal, please.")
interpret(nlu, "Take away")
interpret(nlu, "I'll take a Quarter Pounder and a small coke.")
interpret(nlu, "I'll take a coke.")
interpret(nlu, "I'll have an orange juice.")
interpret(nlu, "Water will be fine.")
interpret(nlu, "Can I have a glass of water?")
interpret(nlu, "Yes, I want two large French Fries, Also, Can you make a Happy meal of Egg and Cheese Mc Muffin?")
interpret(nlu, "Twenty piece Chicken McNuggets.")
interpret(nlu, "May I have two big mac meals to go, please.")