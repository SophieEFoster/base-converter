def main():
  while True:
    result = 0
    position = 1
  
    base1 = int(input("What base do you want to convert from? "))
    base2 = int(input("What base do you want to convert base " + str(base1) + " to? "))
    query = int(input("What base " + str(base1) + " number do you want to convert to base " + str(base2) + "?\nUse only positive integers. "), base1)
  
    #Converts the query into the base you are converting to.
    while query != 0:
      step = query%base2
      result += step*position
      query = int(query/base2)
      position *= 10
  
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
      positionPlaceholder = 0
      word = []
      numbers = []
      numberWords = ["no", "po", "jo", "ko", "so"]
  
      #Gets each place's value.
      for i in range(len(str(result))):
        value = int(str(result)[place]) * position
        if value != 0:
          numbers.append(value)
        place -= 1
        position *= 10
      position2 = len(numbers)
      
      for i in range(len(numbers)):
        position2 -= 1
        numLen = len(str(numbers[position2]))
        positionPlaceholder += 1
        placeholder = int(numbers[position2] / (10**numLen / 10))
        word.append(numberWords[placeholder - 1])
        if (numLen-2)%3 == 0:
          word.append("na")
          numLen -= 1
          #10
          #10,000
          #10,000,000
          #10,000,000,000
        if (numLen-3)%3 == 0:
          word.append("mana")
          numLen -= 2
        if numLen == 4 or numLen == 5 or numLen == 6:
          word.append("tekasu")
  
        if numLen > 6:
          numLen = int((numLen-1)/3-1)
          aResult = 0
          aStep = 0
          aPosition = 1
          while numLen != 0:
            step = numLen%base2
            aResult = aResult + step*aPosition
            numLen = int(numLen/base2)
            aPosition *= 10
          aPlace = len(str(aResult)) - 1
          aPosition = 1
          aPositionPlaceholder = 0
          aWord = []
          aNumbers = []
          aNumberWords = ["ni","pi","ji","ki","si"]
          
          for i in range(len(str(aResult))):
            aValue = int(str(aResult)[aPlace]) * aPosition
            if aValue != 0:
              aNumbers.append(aValue)
            aPlace -= 1
            aPosition *= 10
          aPosition2 = len(aNumbers)
          
          for i in range(len(aNumbers)):
            aPosition2 -= 1
            aNumLen = len(str(aNumbers[aPosition2]))
            aPositionPlaceholder += 1
            aPlaceholder = int(aNumbers[aPosition2] / (10**aNumLen / 10))
            aWord.append(aNumberWords[aPlaceholder - 1])
            if (aNumLen-2)%3 == 0:
              word.append("ne")
              numLen -= 1
            if (aNumLen-3)%3 == 0:
              word.append("mene")
              numLen -= 2
            if aNumLen == 4 or aNumLen == 5 or aNumLen == 6:
              word.append("tekese")
          aWord.append('kamo')
          word.append(''.join(aWord))
              
  
  
  
            
          """print(wordAppendage)
          word.append(''.join(wordAppendage))
          word.append('kamo')"""
          
  
        """if numLen > 6:
          while numLen > 6:
            nL = numLen - 1
            ex = int((nL/3)-2)%6
            #1,000,000 - 7 - 6 - 2 - 0 - 0 - 0
            #1,000,000,000 - 10 - 9 - 3 - 1 - 1 - 0
            #1,000,000,000,000 - 13 - 12 - 4 - 2 - 2 - 0
            #1,000,000,000,000,000 - 16 - 15 - 5 - 3 - 3 - 0
            #1,000,000,000,000,000,000 19 - 18 - 6 - 4 - 4 - 0
            #1,000,000,000,000,000,000,000 22 - 21 - 7 - 5 - 5 - 15 - 14 - 4 - 2 - 2 - 2
            print(str(ex) + ":" + str(nL))
            if ex == 0 or ex == 5:
              word.append("ni")
              numLen -= 7
            if ex == 1:
              word.append("pi")
              numLen -= 10
            if ex == 2:
              word.append("ji")
              numLen -= 13
            if ex == 3:
              word.append("ki")
              numLen -= 16
            if ex == 4:
              word.append("si")
              numLen -= 19
            print(numLen)
          word.append("kamo")"""
        word.append(" ")
  
      word = ''.join(word)
      print(word)

main()
