from SlickNLU import SlickNLU, interpret

dictionaries = {}

dictionaries["intent"] = """show,show
find,show
search,show
browse,show
display,show
interested,show
looking for,show
i'd like,show
do you have,show
do you carry,show
need,show
want,show
clear
reset,clear
restart,clear
deselect,clear
hello,hello
hi, hello
help, hello
how are you,hello
speechly,speechly
"""

dictionaries["brand"] = """adidas,1289
Arena,831
ASICS,694
essex,694
a six,694
Better Bodies,20804
Billabong,121
Bjorn Borg,112
Burton,1323
Calvin Klein,974
Casio,4515
Champion,1142
CITIZEN,9382
Columbia,1123
Converse,348
Converses,348
all star,348
Crocs,707
D C,3641
DC,3641
Dickies,383
Diesel,18729
D K N Y,18731
Donna Karan,18731
DKNY,18731
EMPORIO ARMANI,1878
Armani,1878
Fila,842
feel,842
fear,842
FRED PERRY,3029
Gant,262
Garmin,18225
Guess,360
H and M,23014
H et M,23014
H M,23014
HM,23014
Helly Hansen,1476
Hugo Boss,3973
Boss,3973
Hugo,3973
Jack & Jones,273
Jack and Jones,273
Jack Wolfskin,339
Lacoste,88
Levis,441
Levi's,441
Levi,441
Michael Kors,18972
Molo,96
New Balance,281
New Balances,281
Nike,1273
Nikes,1273
Air Max,1273
Air Maxes,1273
Air Force Ones,1273
Air Force One,1273
Air Force,1273
Air Jordan,1273
Jordan,1273
O Neill,746
O'Neill,746
Oakley,234
Oakleys,234
Old Navy,1896
Patagonia,745
Peak Performance,4146
Big Performance,4146
junior frost down,4146
jr frost down,4146
Helium hood,4146
Puma,267
Quicksilver,21503
RALPH LAUREN,1778
Polo RALPH LAUREN,1778
Ray-Ban,4355
Ray-Bans,4355
Reebok,881
Skechers,12
Sloggi,997
Sloggis,997
Slogging,997
Speedo,1050
Speedos,1050
Superdry,125
Ted Baker,4106
The North Face,61
North Face,61
TIMBERLAND,3433
Timberlands,3433
Tommy Hilfiger,1671
Hilfiger,1671
Tommy Hilfiger Sport,23879
Under Armour,716
Vans,191
Versace,868
Craft,507
Dr. Martens,491
Doc Martens,491
Doc Martin's,491
Happy Socks,4315
Happy sox,4315
Lindberg,1327
Lindberg Sweden,1327
Salomon,1059
Solomon,1059
Tiger of Sweden,1566
Viking,289
Viking cascade,289
Viking Toasty,289
Viking toasty two,289
Viking cascade two,289
Viking cascade ii,289
Scarpe,2652
Zara,7695
zara,7695
"""

dictionaries["color"] = """beige,beige
light brown,beige
khaki,beige
sand,beige
fawn,beige
cocky,beige
black,black
dark,black
pitch black,black
blue,blue
navy,blue
indigo,blue
midnight blue,blue
navy blue,blue
St Pauls Blue,blue
light blue,blue
brown,brown
chestnut,brown
terra-cotta,brown
sepia,brown
gold,gold
golden,gold
amber,gold
gray,gray
grey,gray
ash,gray
smokey,gray
green,green
multicolored,multicolored
polychrome,multicolored
colorful,multicolored
multicolor,multicolored
multi color,multicolored
multi colored,multicolored
rainbow,multicolored
bright colors,multicolored
bright,multicolored
floral,floral
olive,olive
orange,orange
petrol,petrol
pink,pink
light red,pink
pinkish,pink
red,red
burgundy,red
scarlet,red
maroon,red
silver,silver
shiny,silver
metallic,silver
turquoise,turquoise
cyan,turquoise
aquamarine,turquoise
aqua,turquoise
violet,violet
purple,violet
lavender,violet
lilac,violet
plum,violet
mauve,violet
white,white
light,white
ivory,white
snow,white
off-white,white
cream,white
creamy,white
why,white
yellow,yellow
mustard,yellow
honey,yellow
"""

dictionaries["product"] = """Accessories,Accessories
Baby coveralls,Kick suits
Baby rompers,Kick suits
Baby one piece,Kick suits
Baby footie,Kick suits
Baby footies,Kick suits
baby clothes,Kick suits
babies,Kick suits
baby,Kick suits
baby outfit,Kick suits
Baby pants,Baby pants
Baby shirts,Baby shirts
Baby shoes,Baby shoes
Backpacks,Reput
Rucksacks,Reput
Backpack,Reput
Rucksack,Reput
Schoolbag,Reput
Schoolbags,Reput
Back pack,Reput
Back packs,Reput
Bags,Bags
Bag,Bags
Base layers,Underlays
Underlays,Underlays
Bathrobes,Bathrobes
Bathrobe,Bathrobes
Beach dresses,Beach dresses
Beach dress,Beach dresses
Beachwear,Beachwear
beach,Beachwear
Beanies,Pipot
Beanie,Pipot
Belt bags,Belt bags
Belt bag,Belt bags
Fanny pack,Belt bags
Fanny packs,Belt bags
Bum bags,Belt bags
Bum bag,Belt bags
waist pack,Belt bags
waist packs,Belt bags
Belts,Belts
Belt,Belts
Leather belts,Belts
Leather belt,Belts
Bicycle bags,Bicycle bags
Bicycle bag,Bicycle bags
Biker jackets,Biker jackets
Biker jacket,Biker jackets
Bikini,Bikini
Bikinis,Bikini
Bikini bra,Bikini bra
Bikini bras,Bikini bra
Blazers,Blazers
Blazer,Blazers
Blouses,Blouses
Blouse,Blouses
Bodys,Bodyt
Body,Bodyt
bodies,Bodyt
Boots,Boots
Boot,Boots
Bracelets,Bracelets
Bracelet,Bracelets
Bras,Bra
Bra,Bra
sports bra,Bra
sports bras,Bra
Caftans,Caftans
Caftan,Caftans
Caps,Caps
Cap,Caps
Cardigans,Cardigans
Cardigan,Cardigans
Cargo pants,Thigh pocket trousers
Cargo shorts,Cargoshortsit
Casual dresses,Casual dresses
Casual dress,Casual dresses
Casual pants,Casual pants
Casual shirts,Casual shirts
Casual shirt,Casual shirts
Chino shorts,Chino shorts
Chinos,Chinot
Khakis,Chinot
ginos,Chinot
she knows,Chinot
Sea shoe,Sea shoes
Aquatic shoes,Sea shoes
Aquatic shoe,Sea shoes
Aqua shoes,Sea shoes
Aqua shoe,Sea shoes
Water shoes,Sea shoes
Water shoe,Sea shoes
Climbing shoes,Climbing shoes
mountaineering shoes,Climbing shoes
mountaineering shoe,Climbing shoes
Camping gear,Camping gear
Camping equipment,Camping gear
Camping supplies,Camping gear
Cloth pants,Cloth pants
Cotton pants,Cloth pants
Linen pants,Cloth pants
cotton trousers,Cloth pants
Coats,Coats
Coat,Coats
Comfy pants,Comfy pants
Compression shirts,Compression shirts
Compression shirt,Compression shirts
Court shoes,Court shoes
Cross-country running shoes,Cross-country running shoes
Trail running shoes,Cross-country running shoes
Trail running trainers,Cross-country running shoes
Cross-country running trainers,Cross-country running shoes
Off-road running shoes,Cross-country running shoes
Off-road running trainers,Cross-country running shoes
Cycling backpacks,Cycling backpacks
Cycling backpack,Cycling backpacks
Cycling clothing,Cycling clothing
Cycling clothes,Cycling clothing
Cycling wear,Cycling clothing
Cycling,Cycling clothing
Cycling cloth,Cycling clothing
Cycling pants,Cycling pants
Cycling shoes,Cycling shoes
Daypacks,Daypacks
Denim,Jeans
Jeans,Jeans
Chains,Jeans
James,Jeans
Genes,Jeans
denim jeans,Jeans
jean,Jeans
Denim dresses,Denim dresses
Denim dress,Denim dresses
Denim jackets,Denim jackets
Denim jacket,Denim jackets
Denim shorts,Denim shorts
short jeans,Denim shorts
Denim skirts,Denim skirts
Denim skirt,Denim skirts
Down jackets,Down jackets
Down jacket,Down jackets
Down coat,Down jackets
Down coats,Down jackets
Dresses,Dresses
Dress,Dresses
Frock,Dresses
Frocks,Dresses
Dresses with stripes,Dress with stripes
Striped dress,Dress with stripes
Striped dresses,Dress with stripes
Earrings,Earrings
Earring,Earrings
Fitness shoes,Fitness shoes
Fleece,Fleece
Gloves,Gloves
Hair accessories,Hair accessories
Handbags,Handbags
Handbag,Handbags
Purse,Handbags
Purses,Handbags
Hats,Millinery
Hat,Millinery
beret,Millinery
berets,Millinery
Headphones,Headphones
wireless headphones,Headphones
Hiking clothing,Hiking clothing
Hiking clothes,Hiking clothing
Trekking clothes,Hiking clothing
Hoodies,Hoodies
Hoodie,Hoodies
Jackets,Jackets
Jacket,Jackets
check it,Jackets
Jewelry,Jewelry
Jumpsuits,Jumpsuits overalls
Jumpsuit,Jumpsuits overalls
Keychains,Keychains
Keychain,Keychains
Knit sweaters,Knit sweaters
Knit sweater,Knit sweaters
Knitted sweaters,Knit sweaters
Knitted sweater,Knit sweaters
Knitted skirts,Knitted skirts
Knitted skirt,Knitted skirts
Knitwear,Knitwear
Lace dresses,Lace dresses
Lace dress,Lace dresses
Lace-up shoes,Lace-up shoes
shoes with laces,Lace-up shoes
shoelaces,Lace-up shoes
leather shoes,Lace-up shoes
leather insoles,Lace-up shoes
ones with laces,Lace-up shoes
Leather boots,Leather boots
Leather boot,Leather boots
Leather jackets,Leather jackets
Leather jacket,Leather jackets
Leather coat,Leather jackets
Leather coats,Leather jackets
Leg warmers,Leg warmers
Leggings,Leggings
Oversized leggings,Leggings
Leisurewear,Living clothes
Leisure clothes,Living clothes
Leisure clothing,Living clothes
Long skirts,Long skirts
Long skirt,Long skirts
Long sleeve dresses,Long sleeve dresses
Long sleeve dress,Long sleeve dresses
Dress with long sleeves,Long sleeve dresses
Dresses with long sleeves,Long sleeve dresses
Long sleeve shirts,Long sleeve shirts
Long sleeve shirt,Long sleeve shirts
Shirt with long sleeves,Long sleeve shirts
Shirts with long sleeves,Long sleeve shirts
Long sleeves,Long sleeve shirts
Long sleeve t-shirts,Long sleeve t-shirts
Long sleeve t-shirt,Long sleeve t-shirts
T-shirt with long sleeves,Long sleeve t-shirts
T-shirts with long sleeves,Long sleeve t-shirts
Loose fit jeans,Loose fit jeans
Makeup bags,Makeup bags
Makeup bag,Makeup bags
Maternity clothes,Maternity clothes
Maternity clothing,Maternity clothes
Maternity wear,Maternity clothes
Pregnancy clothing,Maternity clothes
Maternity jeans,Maternity jeans
Maternity shirts,Maternity shirts
Maternity shirt,Maternity shirts
Maxi dresses,Maximekot
Maxi dress,Maximekot
Long dress,Maximekot
Long dresses,Maximekot
Midi dresses,Midimekot
Midi dress,Midimekot
Midi skirts,Midi-skirt
Midi skirt,Midi-skirt
Mini dresses,Minidresses
Mini dress,Minidresses
Short dress,Minidresses
Short dresses,Minidresses
Mini skirts,Miniskirts
Mini skirt,Miniskirts
Mittens,Mittens
Necklaces,Necklaces
Necklace,Necklaces
Outdoor clothing,Outdoor clothing
Outdoor clothes,Outdoor clothing
Outdoor jackets,Outdoor jackets
Outdoor jacket,Outdoor jackets
Outdoor trousers,Outdoor trousers
Outdoor pants,Outdoor trousers
Outerwear,Outerwear
Overalls,Overalls
Pajamas,Pajamas
Pajama,Pajamas
Pants,Pants
Trousers,Pants
trouser,Pants
colored pants,Pants
Parkas,Parkasakit
Anoraks,Parkasakit
Parka jackets,Parkasakit
Parka,Parkasakit
Anorak,Parkasakit
Parka jacket,Parkasakit
Party dresses,Party dresses
Party dress,Party dresses
Evening dress,Party dresses
Evening gown,Party dresses
Dress for evening,Party dresses
Evening gowns,Party dresses
Dresses for evening,Party dresses
Evening dresses,Party dresses
Pilot jackets,Pilot jackets
Pilot jacket,Pilot jackets
Playsuits,Playsuits overalls
Playsuit,Playsuits overalls
Polo shirts,Pique shirts
Pique shirts,Pique shirts
Tennis shirt,Pique shirts
Polo shirt,Pique shirts
Pique shirt,Pique shirts
Tennis shirts,Pique shirts
Printed t-shirts,Printed t-shirts
Printed t-shirt,Printed t-shirts
Rain pants,Rain pants
Waterproof pants,Rain pants
Water proof pants,Rain pants
Corduroy pants,Corduroy pants
Leather pants,Leather pants
Raincoats,Raincoats
Raincoat,Raincoats
Rain jacket,Raincoats
Rain jackets,Raincoats
waterproof jacket,Raincoats
waterproof jackets,Raincoats
sailing jackets,Raincoats
sailing jacket,Raincoats
rain clothes,Raincoats
Rainwear,Rainwear
Waterproof clothing,Rainwear
sailing clothes,Rainwear
Water proof clothing,Rainwear
Rubber boots,Rubber boots
Wellingtons,Rubber boots
Rubber boot,Rubber boots
Wellies,Rubber boots
Wellington boots,Rubber boots
Wellington boot,Rubber boots
Gumboots,Rubber boots
Gumboot,Rubber boots
Running clothes,Running clothes
Running shoes,Running shoes
Runners,Running shoes
Jogging shoes,Running shoes
Running shoe,Running shoes
Running trainers,Running shoes
Running sneakers,Running shoes
Sandals,Sandals
Flip flops,Sandals
Summer sandals,Sandals
Flip flop,Sandals
Scarves,Scarves
Scarf,Scarves
Shell jackets,Shell jackets
Shell jacket,Shell jackets
Shell pants,Shell pants
Shirt dresses,Shirt dresses
Shirt dress,Shirt dresses
Shirts,Collared shirts
Shirt,Collared shirts
Shoes,Shoes
Footwear,Shoes
Shoe,Shoes
Choose,Shoes
Kicks,Shoes
Shows,Shoes
Short tops,Short tops
Short top,Short tops
Short-sleeved shirts,Short sleeve shirts
Short-sleeved shirt,Short sleeve shirts
Short sleeve shirt,Short sleeve shirts
Short sleeve shirts,Short sleeve shirts
Shirt with short sleeves,Short sleeve shirts
short sleeves,Short sleeve shirts
Short-sleeved t-shirts,Short-sleeved t-shirts
Short-sleeved t-shirt,Short-sleeved t-shirts
Short sleeve t-shirts,Short-sleeved t-shirts
Short sleeve t-shirt,Short-sleeved t-shirts
T-shirt with short sleeves,Short-sleeved t-shirts
Shorts,Shorts
Shoulder bags,Shoulder bags
Shoulder bag,Shoulder bags
Ski clothing,Ski clothing
Ski clothes,Ski clothing
Ski wear,Ski clothing
Ski jumper,Ski clothing
Skinny jeans,Whistle jeans
Skirts,Skirts
Skirt,Skirts
Sleepwear,Sleepwear
Sleeping clothes,Sleepwear
Nightwear,Sleepwear
Sleep clothes,Sleepwear
Nightclothes,Sleepwear
Nightgown,Sleepwear
Nightie,Sleepwear
Sleeping bag,Sleepwear
Sleeveless dresses,Sleeveless dresses
Sleeveless dress,Sleeveless dresses
Dress without sleeves,Sleeveless dresses
Sleeveless tops,Sleeveless tops
Sleeveless top,Sleeveless tops
Top without sleeves,Sleeveless tops
Slippers,Slippers
Slipper,Slippers
Small bags,Small bags
Small bag,Small bags
Sneakers,Sneakers
Sneaker,Sneakers
Snickers,Sneakers
Trainers,Sneakers
sniker,Sneakers
snikers,Sneakers
basketball shoes,Sneakers
golf shoes,Sneakers
Snowboard clothing,Snowboard clothing
Snowboard clothes,Snowboard clothing
Snowboarding clothes,Snowboard clothing
snowsuit,Snowboard clothing
snow jacket,Snowboard clothing
snow jackets,Snowboard clothing
Snowboarding jacket,Snowboard clothing
Socks,Socks
Sock,Socks
Sox,Socks
Softshell jackets,Softshell jackets
Softshell jacket,Softshell jackets
Sports bags,Sports bags
Sports bag,Sports bags
Gym bag,Sports bags
Fitness bag,Sports bags
Gym bags,Sports bags
Fitness bags,Sports bags
Sports glasses,Sports glasses
Sports gloves,Sports gloves
Sports jackets,Sports jackets
Sports jacket,Sports jackets
Sports coat,Sports jackets
Sports coats,Sports jackets
Sport jackets,Sports jackets
Sport jacket,Sports jackets
Sports pants,Sports pants
Sports shirts,Sports shirts
Sports shirt,Sports shirts
Training shirt,Sports shirts
Training shirts,Sports shirts
Sports shoes,Sports shoes
Sports shoe,Sports shoes
Gym shoes,Sports shoes
Gym shoe,Sports shoes
Sport shoe,Sports shoes
Sport shoes,Sports shoes
Sports shorts,Sports shorts
Biking pants,Sports shorts
Biking shorts,Sports shorts
Training shorts,Sports shorts
Bicycle pants,Sports shorts
Bicycle shorts,Sports shorts
Sports tops,Sports tops
Sports top,Sports tops
Sports underwear,Sports underwear
Sports undergarments,Sports underwear
Sportswear,Sportswear
Sports clothes,Sportswear
Sports clothing,Sportswear
Active wear,Sportswear
Activity wear,Sportswear
Sport,Sportswear
Spring jackets,Spring jackets
Spring jacket,Spring jackets
Spring coats,Spring jackets
Spring coat,Spring jackets
Coat for spring,Spring jackets
Coats for spring,Spring jackets
Jacket for spring,Spring jackets
Jackets for spring,Spring jackets
Strings,Stringit
Thongs,Stringit
Thong,Stringit
Suit jacket,Costume jackets
Lounge jacket,Costume jackets
Lounge coat,Costume jackets
Suit coat,Costume jackets
Suit shoes,Costume shoes
Dress shoes,Costume shoes
Suit trousers,Suit trousers
Suit pants,Suit trousers
Suit vests,Suit vests
Suit vest,Suit vests
Suitcases,Suitcases
Suitcase,Suitcases
Suits,Suits
Suit,Suits
Summer dresses,Summer dresses
Summer dress,Summer dresses
Dress for summer,Summer dresses
Sunglasses,Sunglasses
Sweatshirts,College shirts
Sweatshirt,College shirts
Sweat shirt,College shirts
Sweaters,Sweaters
Jumpers,Sweaters
Jumper,Sweaters
Sweater,Sweaters
Pullover,Sweaters
Pullovers,Sweaters
Swimming shorts,Swimming shorts
Swimming trunks,Swimming trunks
Swimsuits,Swimsuits
Swimsuit,Swimsuits
Bathing suit,Swimsuits
Bathing suits,Swimsuits
Swimwear,Swimwear
T-shirts,T-shirts
T-shirt,T-shirts
striped t-shirt,T-shirts
striped t-shirts,T-shirts
Tennis shoes,Tennis shoes
Tennis shoe,Tennis shoes
Tops,Tops
Top,Tops
Tracksuits,Tracksuits
Tracksuit,Tracksuits
Travel bags,Travel bags
Travel bag,Travel bags
Tunics,Tunics
Tunic,Tunics
Underpants,Underpants
Panties,Underpants
Pantie,Underpants
Knickers,Underpants
Nickers,Underpants
Undershirts,Undershirts
Underwear,Underwear
Undies,Underwear
Lingerie,Underwear
Boxers,Underwear
Boxer shorts,Underwear
briefs,Underwear
brief,Underwear
undergarments,Underwear
jockstraps,Underwear
Vests,Vest
Vest,Vest
Walking shoes,Walking shoes
Wallets,Wallets
Wallet,Wallets
Watches,Watches
Watch,Watches
Weekend bags,Weekend bags
Weekend bag,Weekend bags
Wetsuits,Surf shirts and wetsuits
Wetsuit,Surf shirts and wetsuits
Wide leg jeans,Wide leg jeans
Windbreakers,Windbreakers
Wind stopper,Windbreakers
Windbreaker,Windbreakers
Windbreaker jacket,Windbreakers
Windbreaker jackets,Windbreakers
Wind proof jackets,Windbreakers
Windproof jackets,Windbreakers
Wind jacket,Windbreakers
Winter jackets,Winter jackets
Winter jacket,Winter jackets
Winter coat,Winter jackets
Winter coats,Winter jackets
Jacket for winter,Winter jackets
Warm jacket,Winter jackets
Winter clothing,Winter jackets
Coats for winter,Winter jackets
Winter shoes,Winter shoes
Shoes for winter,Winter shoes
Wrap dresses,Wrap dresses
Wrap dress,Wrap dresses
Wrapping skirts,Wrapping skirts
Wrapping skirt,Wrapping skirts
Wrap skirt,Wrapping skirts
Wrap skirts,Wrapping skirts
Ankle boots and booties,Ankle boots and booties
Ankle boots,Ankle boots and booties
Booties,Ankle boots and booties
Heeled ankle boots,Ankle boots and booties
Heeled boots,Ankle boots and booties
Ankle booties,Ankle boots and booties
Boots with heels,Ankle boots and booties
High heel boots,Ankle boots and booties
Bikini pants,Bikini pants
Bikini bottom,Bikini pants
Bikini bottoms,Bikini pants
Bikini tops,Bikini tops
Bikini top,Bikini tops
Bomber jackets,Bomber jackets
Bomber jacket,Bomber jackets
Business,Business
Work,Business
Professional,Business
Clothing,Clothing
Clothes,Clothing
Formal clothing,Formal clothing
High heels,High heels
Heels,High heels
High heel shoes,High heels
Shoes with high heels,High heels
Shoes with heels and pumps,High heels
Shoes with heels,High heels
Shoe with heels,High heels
Hiking shoes,Hiking shoes
Hiking shoe,Hiking shoes
Hiking boots,Hiking shoes
Turtlenecks,Polo shirts
Puffer jackets,Puffer jackets
Puffer jacket,Puffer jackets
Puffer,Puffer jackets
Puffers,Puffer jackets
Rings,Rings
Ring,Rings
Running pants and leotards,Running pants and leotards
Running pants,Running pants and leotards
Running bottoms,Running pants and leotards
jogging pants,Running pants and leotards
jogging bottoms,Running pants and leotards
Ski jackets,Ski jackets
Ski jacket,Ski jackets
Skiing jacket,Ski jackets
Skiing jackets,Ski jackets
Ski boots,Ski boots
Soccer shoes,Soccer shoes
Football shoes,Soccer shoes
Soccer cleats,Soccer shoes
Football shoe,Soccer shoes
Football boots,Soccer shoes
Sweat pants,Sweat pants
Joggers,Sweat pants
Track pants,Sweat pants
Sweatpants,Sweat pants
College pants,Sweat pants
Sweat clothes,Sweat clothes
Biking shoes,Biking shoes
Athletic shoes,Athletic shoes
Umbrellas,Umbrellas
Winter boots,Winter boots
Boots for winter,Winter boots
"""

dictionaries["size"] = """X X S,XXS
extra extra small,XXS
double X S,XXS
double XS,XXS
two XS,XXS
XXS,XXS
two X S,XXS
X S,XS
extra small,XS
S,S
small,S
M,M
medium,M
L,L
large,L
big,L
X L,XL
extra large,XL
x large,XL
excel,XL
X X L,XXL
extra extra large,XXL
double X L,XXL
double XL,XXL
XXL,XXL
two XL,XXL
two X L,XXL
X X X L,3XL
extra extra extra large,3XL
three X L,3XL
three extra large,3XL
triple X L,3XL
triple XL,3XL
three XL,3XL
XXXL,3XL
35,35
4,35
4 and a half,35
UK 4,35
four point five,35
36,36
5,36
5 and a half,36
UK 5,36
five point five,36
37,37
6,37
6 and a half,37
UK 6,37
six point five,37
38,38
7,38
7 and a half,38
UK 7,38
seven point five,38
39,39
8,39
8 and a half,39
UK 8,39
eight point five,39
40,40
9,40
9 and a half,40
UK 9,40
nine point five,40
41,41
10,41
10 and a half,41
UK 10,41
ten point five,41
42,42
11,42
11 and a half,42
UK 11,42
eleven point five,42
43,43
12,43
12 and a half,43
UK 12,43
twelve point five,43
44,44
13,44
13 and a half,44
UK 13,44
thirteen point five,44
45,45
14,45
14 and a half,45
UK 14,45
fourteen point five,45
46,46
15,46
15 and a half,46
UK 15,46
fifteen point five,46
47,47
16,47
16 and a half,47
UK 16,47
sixteen point five,47
"""

dictionaries["department"] = """kids,child
children's,child
kids',child
child,child
children,child
toddler,child
kits,child
toddlers,child
kid,child
women,female
women's,female
ladies,female
girls,female
woman's,female
woman,female
female,female
female's,female
men,male
man's,male
mens,male
men's,male
man,male
menswear,male
male,male
boys,male
gents,male
unisex,unisex
gender neutral,unisex
gender fluid,unisex
"""

dictionaries["sort"] = """exclusive,price_desc
price descending,price_desc
most exclusive,price_desc
most pricey,price_desc
exclusivity,price_desc
luxurious,price_desc
luxury,price_desc
expensive,price_desc
most expensive,price_desc
price high to low,price_desc
highest price,price_desc
highest,price_desc
high price,price_desc
price,price_asc
pricing,price_asc
price ascending,price_asc
price low to high,price_asc
lowest price,price_asc
lowest,price_asc
low price,price_asc
lower price,price_asc
cheap,price_asc
cheapest,price_asc
least expensive,price_asc
increasing price,price_asc
cost,price_asc
popular,popularity_desc
most popular,popularity_desc
popularity,popularity_desc
best,popularity_desc
top sellers,popularity_desc
top seller,popularity_desc
top selling,popularity_desc
favorite,popularity_desc
fanciest,popularity_desc
fancy,popularity_desc
most sold,popularity_desc
new,new_desc
latest,new_desc
"""

dictionaries["filter"] = """brand
color
size
department
sex,department
product
category,product
sort
order,sort
"""

nlu = SlickNLU(dictionaries, keyword_last=True)

interpret(nlu, "I'm interested in women's blue jeans jeans from Ksubi, Old Navy or Adidas in size 10.")

interpret(nlu, "I'd like to browse socks.")

interpret(nlu, "I need a new watch.")

interpret(nlu, "Women's dresses.")

interpret(nlu, "Clear. A golden jacket.")

interpret(nlu, "white casual shoes for women")

interpret(nlu, "i'm looking for a white t shirt")

interpret(nlu, "i'd like a s* fleece jacket please i'd like a fleece jacket please do you have any fleece jackets do you have any ski jackets")

interpret(nlu, "find me black shoes in size twelve")

interpret(nlu, "show me yellow dresses in a size small")

interpret(nlu, "i want some shoes which are from the company adidas")

interpret(nlu, "i'm looking for some cheap white vans shoes for men's size eight")

interpret(nlu, "i would like to find zip up hoodie")

interpret(nlu, "women's seventy seven")

interpret(nlu, "black shirt")

interpret(nlu, "deselect color")

interpret(nlu, "hello how are you doing")