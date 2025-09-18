import p03 as sajat
from p03 import szamologep as calculator

szam = 10
while szam < 2:
    szam-= 1
    if szam == 4:
        continue
    if szam == 3:
        break
    print(szam)
else:
    print("Vége a ciklusnak")

while True:
    szam+=1
    print(szam)
    if szam == 30:
        break

print(sajat.veletlenszam(50))
sajat.szam_bekerese(5)
calculator()