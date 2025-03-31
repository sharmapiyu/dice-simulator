# dice simulator
import random
import time
print("lets roll the dice")
x=int(input("click 1 to roll the dice"))
if x == 1:
    for i in range(1,4):
        print(i)
        time.sleep(2)
    print("Here's your luck")
    print("DICE : ",random.randint(0,6))
else:
    print("invald button pressed")
