'''import math
import random

print(math.sqrt(9))
for _ in range(50):
    print(random.randint(1,6)) '''
try:
    eredmeny = 10/ertek
except ZeroDivisionError:
    print("Hiba: Nullával való osztés")
except NameError:
    print("Hiba: névhiba")
else:
    print(eredmeny)
