import re
import sys

rules="""hello (intent_hello)...
show (intent_show) me...
show (intent_show)...

...$brand...
...from $brand...
...by $brand...

...$product...

...$color...
...in $color...
...in $color color...
...$color color...
...color $color...

...$size...
...size $size...

...department...
...for $department...

...cheapest (sort)...
...popular (sort)..."""

dictionaries = {}

dictionaries["brand"] = """nike
adidas
ksubi
"""

dictionaries["color"] = """blue
red
green
"""

dictionaries["product"] = """jeans
jackets
bags
"""

dictionaries["size"] = """nine
ten
eleven
"""

dictionaries["department"] = """men
women
kids
"""

class Rule:
  
  def __init__(self, rule: str, dictionaries: dict) -> None:
    self.context_words = []
    self.entity_types = []
    self.dict_refs = []

    # Remove dots for now
    rule = rule.replace(".", "")
    rule_tokens = rule.split(" ")
    while len(rule_tokens) > 0:
      token = rule_tokens.pop(0)
      entity_type = None
      dict_ref = None
      if (token[0] == "$"):
        dict_ref = token.replace("$", "")
        if (not dict_ref in dictionaries):
          sys.exit(str.format("Unknown dict '{}'", dict_ref))
      if (len(rule_tokens) > 0 and rule_tokens[0][0] == "("):
        entity_type = rule_tokens.pop(0).replace("(","").replace(")","")
      self.context_words.append(token)
      self.entity_types.append(entity_type)
      self.dict_refs.append(dict_ref)

  def __repr__(self) -> str:
    return " ".join(self.context_words)

d = {key: [word for word in words.split("\n") if word != ""] for key, words in dictionaries.items()}
r = [Rule(rule, d) for rule in rules.split("\n") if rule != ""]

print (d)
print (r)