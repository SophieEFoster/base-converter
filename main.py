result = 0
position = 1

base1 = int(input("What base do you want to convert from? "))
base2 = int(input("What base do you want to convert base " + str(base1) + " to? "))
query = int(input("What base " + str(base1) + " number do you want to convert to base " + str(base2) + "? (Use only positive integers.) "), base1)

#Converts the query into the base you are converting to.
while query != 0:
    step = query%base2
    result = result + step*position
    query = int(query/base2)
    position = position*10
print(result)

#Takes the output in base 6 and turns it into words in etalanu mosa nonuwu nomamono.
if base2 == 6:
    place = len(str(result)) - 1
    position = 1
    word = []
    mo = {0: "mo"}
    no = {1: "no"}
    po = {2: "po"}
    jo = {3: "jo"}
    ko = {4: "ko"}
    so = {5: "so"}
    na = {10: "na"}
    mana = {100: "mana"}
    tekasu = {1000: "tekasu"}
    ni = {1000000, "ni"}
    pi = {1000000000, "pi"}
    ji = {1000000000000, "ji"}
    ki = {1000000000000000, "ki"}
    si = {1000000000000000000, "si"}
    for i in range(len(str(result))):
        value = int(str(result)[place]) * position
        print(value)
        place = place - 1
        position = position * 10