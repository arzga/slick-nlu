# slick-nlu

Experiments with "lite NLU": Will keyword-focused approach suffice for most applications?

## Design principles

- Focus on output keywords
- Reduce configuration: only specify what needs to be outputted
- Exact match is always respected
- Make best effeort guess the type of keywords that are not on the keyword list
- Acknowledge some intepretation is context specific, but scoped out from NLU side. Make it easy to implement context in app-side.

## Current PoC

Usage
```
python3 fashion.py
python3 burger.py
```

### Rules in pseudo-config language

#### Main config (implicit from order of keyword dictionaries)
```
...{$intent}(intent)...
...{$brand}(brand)...
...{$color}(color)...
...{$product}(product)...
...{$size}(size)...
...{$fiter}(fiter)...
```

#### Intent
```
hello, hi, help, how are you: hello
show, find, search, browse, display, interested, looking for, i'd like, do you have, do you carry, need, want: show
clear, reset, restart, deselect: clear
```

#### Brand
```
Arena,831
Asics,694
Better Bodies,20804
Billabong,121
Bjorn Borg,112
Burton,1323
...
```

### Specificity matching

Specifity (X,Z)

- X keyword specificity (bigger (more words) = more specific): Value: Number of words in keyword;
- Z Order in definition list. Top of list matched first. Value -line number
- Higher X wins Z


## Roadmap

Improve keyword matching with additional context

### Rules in pseudo-config language

```
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
```

### Specificity matching

Specificity (X,Y,Z)

- X keyword specificity (bigger (more words) = more specific): Value: Number of words in keyword;
- Y context specificity (bigger (more words)
- Z Order in definition list. Top of list matched first. Value -line number
- Higher X wins Y wins Z
? Also consider fuzzy near-matches (e.g. word specificity = 1 / edit distance errors + 1)

Optimization: First attempt to match context in specificity order

### Simulation

```
Show me blue jeans, please
=======
SHOW (intent_show), specificity 2,
SHOW ME (intent_show)


SHOW ME blue jeans, please
             =====
JEANS -> DENIM (product)


SHOW ME blue JEANS, please
        ====
BLUE (color)

SHOW ME BLUE JEANS, please
no further matches, done!
```
