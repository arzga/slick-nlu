from SlickNLU import SlickNLU, interpret

dictionaries = {}

dictionaries["add_order_intent"] = """I'll have
I'd like
I'd like to have
I'd like to order
order
add
gimme
plus
extra
more
also
"""

dictionaries["burger"] = """Big Mac
Hamburger
Cheese burger
McFeast
Quarterpounder
"""

dictionaries["sides"] = """fries
french fries
side salad
salad
sweet potato fries
"""

dictionaries["upgrade"] = """meal
combo
"""

dictionaries["drink"] = """Coke
cola
Coca Cola
Coca Cola zero
Coca Cola light
Diet Coke
Fanta
water
soda water
bubble
"""

dictionaries["amount"] = """one
two
three
four
five
six
seven
eight
nine
ten
"""

dictionaries["size"] = """small
large
regular
"""

dictionaries["profanity"] = """fuck you
fucker
fuck
bitch
son of a bitch
"""

dictionaries["serving"] = """to go: to go, take away, outside, take with me
eat in: eat in, here, in restaurant, in the restaurant, inside
"""
  
nlu = SlickNLU(dictionaries)

interpret(nlu, "Good evening, sir, I'd like to have a Big Mac meal with french fries and a large Coke. Plus an extra cheese burger and large fries. Oh, it'll be to go. And one more Fanta. Could I also have a bottle of water, please? And fuck you, too!")
interpret(nlu, "A coke, please.")
interpret(nlu, "Big mac meal, please.")
interpret(nlu, "Take away")
