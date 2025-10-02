import turtle


class MozgoPont(turtle.Turtle):
    def __init__(self, szin, x ,y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(5)
        self.goto(x, y)
        self.sebesseg = sebesseg

    def inditas(self):
        self.forward(self.sebesseg)


ablak = turtle.Screen()
ablak.title("Pontverseny")
ablak.bgcolor("black")

def kilepes():
    ablak.bye()

'''def inditas():
    turtle.forward(10)'''

pont1 = MozgoPont("cyan", -200, 0, 15)
pont2 = MozgoPont("magenta", -200, 50, 10)
pont3 = MozgoPont("green", -200, 100, 20)

'''turtle.shape("circle")
turtle.color("red")
turtle.penup()
turtle.speed(5)
turtle.goto(-200,0)'''

ablak.listen()

ablak.onkey(kilepes, "Escape")
ablak.onkey(pont1.inditas, "d")
ablak.onkey(pont2.inditas, "k")
ablak.onkey(pont3.inditas, "h")


turtle.mainloop()

