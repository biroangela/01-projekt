class Teglalap():
    alakzat = "téglalap"
    def init(self, alap = 10, magassag = 5):
        self.alap = alap
        self.magassag = magassag
        self.adatok

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")
        print(f"A {self.alakzat} amagassaga = {self.magassag}")

    def kerulet(self):
        return 2 * self.alap + 2 * self.magassag

    def terulet(self):
        return self.alap * self.magassag


class Negyzet(Teglalap):
    alakzat = "negyzet"
    def init(self,alap = 5):
        super().init()
        self.alap = alap
        self.magassag = alap

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")

class Haromszog(Teglalap):
    alakzat="derékszügű háromszög"
    def init(self,alap = 10, magassag = 5):
        self.alap = alap
        self.magassag = magassag




tegla = Teglalap()
print(tegla.adatok())
print("A kerülete = ", tegla.kerulet())
print("A területe = ", tegla.terulet())
print()
negy = Negyzet(8)
print(negy.adatok())
print("A kerülete = ", negy.kerulet())
print("A területe = ", negy.terulet())
print()

harom = Haromszog()
print(harom.adatok())
print("A területe = ", harom.terulet())

