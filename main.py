import time

while True:
  result = 0
  position = 1

  base1 = int(input("What base do you want to convert from? "))
  base2 = int(input("What base do you want to convert base " + str(base1) + " to? "))
  query = int(input("What base " + str(base1) + " number do you want to convert to base " + str(base2) + "?\nUse only positive integers. "), base1)

  #Converts the query into the base you are converting to.
  while query != 0:
    step = query%base2
    result = result + step*position
    query = int(query/base2)
    position = position*10

  print(result)

  #Takes the output in base 10 and turns it into years, months, days, hours, minutes, and seconds.
  if base2 == 10:
    x = result
    y = int(x/31540000)
    x = x-(y*31540000)
    print("Years: " + str(y))
    mo = int(x/2628000)
    x = x-(mo*2628000)
    print("Months: " + str(mo))
    d = int(x/86400)
    x = x-(d*86400)
    print("Days: " + str(d))
    h = int(x/3600)
    x = x-(h*3600)
    print("Hours: " + str(h))
    m = int(x/60)
    x = x-(m*60)
    print("Minutes: " + str(m))
    s = x
    print("Seconds: " + str(s))
    
  #Takes the output in base 6 and turns it into words in etalanu mosa nonuwu nomamono.
  if base2 == 6:
    place = len(str(result)) - 1
    position = 1
    word = []
    numbers = []
    numberWords = ["","no", "po", "ko", "so"]

    for i in range(len(str(result))):
      value = int(str(result)[place]) * position
      numbers.append(value)
      place = place - 1
      position = position * 10

    position2 = len(numbers)
    for i in range(len(numbers)):
      position2 = position2 - 1
      placeholder = int(numbers[position2] / (10**len(str(numbers[position2])) / 10))
      if len(str(numbers[position2])) == 2:
        word.append("na")
      word.append(numberWords[placeholder])
      if len(str(numbers[position2])) == 3:
        word.append("mana")

      """mananaNum = (len(str(numbers[position2]))-1)/3
      print(mananaNum - int(mananaNum))
      if mananaNum - int(mananaNum) > .4 and mananaNum - int(mananaNum) < .9 and mananaNum + 1 > 4:
        word.append("mana")
      if mananaNum - int(mananaNum) > .1 and mananaNum - int(mananaNum) < .4 and mananaNum + 1 > 4:
        word.append("na")
        for i in range(2):
          print("test")

      if len(str(numbers[position2])) >= 4 and len(str(numbers[position2])) <= 7:
        word.append("tekasu")"""
      
      
      if word[len(word) - 1] != "na" or word[len(word) - 1] != "ni" or word[len(word) - 1] != "pi" or word[len(word) - 1] != "ji" or word[len(word) - 1] != "ki" or word[len(word) - 1] != "si":
        if placeholder == 0:
          continue
        word.append(" ")

    word = ''.join(word)
    print(word)
    time.sleep(1)
