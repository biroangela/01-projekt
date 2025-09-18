#adattipusok

szoveg = 'autorendszam'
szam = 15
logikai = True

print(szoveg)
print(szam)

szam *=2
print(szam)
print(logikai)
print(not logikai)
print(szam > 20)

print(szoveg[0])
print(szoveg[0:4])
print(szoveg[4:])
print(szoveg[4:8])
print(szoveg[-4:])

lista = ["habos", "kakao"]
print(lista[0])
print(lista[1])
print(lista[0]+lista[1])
lista+= ["tejszines"]
print(lista)
print(lista[2], lista[0] + lista[1])

halmaz = {5 , 4 , 8 , 5, "alma"}
print(halmaz)

szotar = {"nev": "Béla", "kor": 23}
print(szotar)

eletkor = int(input("Kérem adja meg az életkorát: "))
eletkor += 5
print(eletkor)
print(szotar["nev"], "kora\n", eletkor, sep="-", end="\n")

print("valami".rjust(20, "-"))
print("valami".ljust(20, "-"))
print("valami".center(20, "-"))


