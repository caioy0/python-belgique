import turtle
import math
#Ex1
'''
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)

    def desenhar_retangulo(self):
        t = turtle.Turtle()
        t.forward(self.comprimento)
        t.left(90)
        t.forward(self.largura)
        t.left(90)
        t.forward(self.comprimento)
        t.left(90)
        t.forward(self.largura)
        t.left(90)
        turtle.done()

# Exemplo de uso da classe Retangulo
# Criando um retângulo com comprimento 100 e largura 50
meu_retangulo = Retangulo(100, 50)

# Exibindo a área e o perímetro
print("Área do retângulo:", meu_retangulo.calcular_area())
print("Perímetro do retângulo:", meu_retangulo.calcular_perimetro())

# Desenhando o retângulo na tela
meu_retangulo.desenhar_retangulo()
'''
#Ex2
'''
a=input()
b=input()
class Elipse:
    def __init__(self, grandaxe, petitaxe):
        self.grandaxe = grandaxe
        self.petitaxe = petitaxe

    def formule_perimetre(self):
        a = self.grandaxe
        b = self.petitaxe
        h = ((a - b) ** 2) / ((a + b) ** 2)
        perimeter = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        return perimeter

    def surface(self):
        a = self.grandaxe
        b = self.petitaxe
        return math.pi * a * b

    def dessiner_elipse(self):
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(0, -self.petitaxe)
        t.pendown()
        t.color("blue")

        angle = 0
        while angle < 360:
            x = self.grandaxe * math.cos(math.radians(angle))
            y = self.petitaxe * math.sin(math.radians(angle))
            t.goto(x, y)
            angle += 1
        
        t.hideturtle()
        turtle.done()

# Exemplo de uso da classe Elipse
a = 100  # Demi-grand axe
b = 50   # Demi-petit axe
minha_elipse = Elipse(a, b)

# Calcular e exibir o perímetro
perimetro = minha_elipse.formule_perimetre()
print(f"Perímetro da elipse: {perimetro:.2f} cm")

# Calcular e exibir a área
area = minha_elipse.surface()
print(f"Área da elipse: {area:.2f} cm²")

# Desenhar a elipse usando o módulo Turtle
minha_elipse.dessiner_elipse()
'''
#Ex3
class Relogio:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

    def avancar_minuto(self):
        self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
            if self.horas >= 24:
                self.horas = 0

    def __str__(self):
        return f'{self.horas:02d}:{self.minutos:02d}'

# Exemplo de uso da classe Relogio
meu_relogio = Relogio(12,30)
print("Horário inicial:", meu_relogio)

# Avançar o relógio em 1 minuto
meu_relogio.avancar_minuto()
print("Horário após avançar 1 minuto:", meu_relogio)

# Avançar o relógio em mais 30 minutos
for _ in range(30):
    meu_relogio.avancar_minuto()
print("Horário após avançar mais 30 minutos:", meu_relogio)
