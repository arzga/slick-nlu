# slick-nlu

Experiments with "lite NLU"

## Current PoC

Usage
```
python3 fashion.py
python3 burger.py
```

### Keyword extraction in pseudo-config language

...{$intent}(intent)...
...{$brand}(brand)...
...{$color}(color)...
...{$product}(product)...
...{$size}(size)...
...{$fiter}(fiter)...

### Specificity rules

Specifity (X,Z)

- X keyword specificity (bigger (more words) = more specific): Value: Number of words in keyword;
- Z Order in definition list. Top of list matched first. Value -line number
- Higher X wins Z


## Roadmap

Improve keyword matching with additional context

### Keyword extraction in pseudo-config language

hello (intent_hello)...
show (intent_show) me... (specificity 1,1,-2)
show (intent_show)... (specificity 1,0,-3)

...$brand... (specificity 1,0,-4)
...from $brand... (specificity 1,1,-5)
...by $brand... (specificity 1,1,-6)

...$product(s)...

...$color...
...in $color {color}...
...{in} color $color... (specificity 2/3)

...$size...
...size $size...

...department...
...for $department...

...cheapest (sort)...
...popular (sort)...


Principles:
-------------------------

- Exact match is always respected
- Always return defined keywords
- Make best attempt to guess keyword even if it's not in list.

Specificity rules
-------------------------
X,Y,Z

- X keyword specificity (bigger (more words) = more specific): Value: Number of words in keyword;
- Y context specificity (bigger (more words)
- Z Order in definition list. Top of list matched first. Value -line number
- Higher X wins Y wins Z
? Also consider fuzzy near-matches (e.g. word specificity = 1 / edit distance errors + 1)

Optimization: First attempt to match context in specificity order



-------------------------


Show me blue jeans, please
-------
SHOW (intent_show), specificity 2,
SHOW ME (intent_show)


SHOW ME blue jeans, please
             -----
JEANS -> DENIM (product)


SHOW ME blue JEANS, please
        ----
BLUE (color)

SHOW ME BLUE JEANS, please
no further matches, done!

