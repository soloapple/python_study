import random
#from 1 to 6
die1=random.randint(1,6)
#from 0 to 9, but not include 10
die2=random.randrange(10)+1
total=die1+die2
print(die1, die2, total)


