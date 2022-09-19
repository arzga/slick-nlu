from SlickNLU import SlickNLU, interpret

dictionaries = {}

dictionaries["show_intent"] = """show
find
display
interested
"""

dictionaries["brand"] = """nike
adidas
ksubi
old navy
"""

dictionaries["color"] = """blue
red
green
"""

dictionaries["product"] = """jeans
jackets
bags
wheel nuts
wheelnuts
"""

dictionaries["size"] = """nine
ten
eleven
"""

dictionaries["department"] = """men
men's
women
women's
kids
"""

nlu = SlickNLU(dictionaries)

interpret(nlu, "I'm interested in women's blue jeans jeans from Ksubi, Old Navy or Adidas in size ten. And of course I'd like some wheel nuts, please.")

