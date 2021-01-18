from random import *
score = 0
doors = 0
print("""
Гра-шоу "Двацять один"!
========
За трьома дверима знаходяться числа!
Відкривайте двері щоб отримати точний результат 21!
     _________          __________           __________
   |           |      |            |       |            |          
   |           |      |            |       |            |        
   |    [1]    |      |     [2]    |       |     [3]    |        
   |           |      |            |       |            |     
   |          0|      |         0  |       |          0 | 
   |           |      |            |       |            |      
   |           |      |            |       |            |        
   | _________ |      | __________ |       | __________ |
""")
while score < 21:

    print("\nОбери двері(1,2 or 3)")

    choosendoor = input()
    choosendoor = int(choosendoor)

    windoor = randint(1, 10)

    print("\nОбрані двері мають номер", choosendoor)
    print("Число за дверима -", windoor)

    score = (score + windoor)
    doors = (doors + 1)
    if score > 21:
        print("\nТвій рахунок більше за 21")
    elif score == 21:
      print()    
    else:
        print("Твій рахунок =", score)
if score > 21:
    print("Тобі не вдалося отримати рівно 21")
if score == 21:
    print("Точний результат, твій рахунок = 21")
    print("Ти відкрив", doors, "дверей для перемоги!")
