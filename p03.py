#3.alkalom
if 50>10 or 20<10:
    print("igaz")
else:
    print("nem igaz")
    print("Ez is a hamis ág")
print("Vége")

uzenet= "Helo" if 10>1 else "Bye"
print (uzenet)

def szam_bekerese(legnagyobb_szam):
    szam = input("Kérek egy számot:")
    if szam.isdigit():
        szam = int(szam)

        if szam == 0:
            print("Nem ismerem a 0 számot")
        elif szam > legnagyobb_szam:
            print("Nem ismerem a negaív számokat!")
        else:
            print("Mostmár tudok a számmal dolgozni!")
    else:
        print("Nem számot adtál meg!")
    return szam

#A program indítása
def szamologep():
    muvelet = input("Milyen műveletet akar végrehajtani (+,-,*,/):")
    egyik_szam = szam_bekerese(10)
    masik_szam = szam_bekerese(100)
    if muvelet == "+":
     eredmeny =egyik_szam + masik_szam
    elif muvelet == "-":
        eredmeny =egyik_szam - masik_szam
    elif muvelet == "*":
        eredmeny = egyik_szam * masik_szam
    else:
        eredmeny = egyik_szam / masik_szam

    print(f"Az eredmény: {egyik_szam} {masik_szam} = {eredmeny}")

    if __name__=="__main__":
        szamologep()



masik_szam = input("Kérek még egy számot:")