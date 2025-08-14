# class Keyboard:
#     def __init__(self, keys, type):
#         self.keys = keys
#         self.type = type
    
#     def keyboard_type(self):
#         if self.type == 1:
#             print('QWERTY')
#         else:
#             print('AZERTY')
    
#     def keyboard_keys(self):
#         self.keys = 61

# class Screen:
#     def __init__(self, mresx, mresy, mcolors):
#         self.mresx = mresx
#         self.mresy = mresy
#         self.mcolors = mcolors
    
#     def monitor_info(self):
#         print(f"Resolution: {self.mresx}x{self.mresy}, Colors: {self.mcolors}")

# class Processor:
#     def __init__(self, brand, cores, speed):
#         self.brand = brand
#         self.cores = cores
#         self.speed = speed
    
#     def brandscpu(self):
#         if self.brand == 1:
#             print('Intel')
#         else:
#             print('AMD')
    
#     def specs(self):
#         if self.brand == 1:
#             self.cores = 6
#             self.speed = 3.0
#         else:
#             self.cores = 8
#             self.speed = 4.0

# class Computer:
#     def __init__(self, ram):
#         self.ram = ram
    
#     def memory(self):
#         print(f"RAM: {self.ram}GB")

# USA=input('Press 1 for USA or another key to AMD?: ')
# # Criando objetos e testando as classes
# my_keyboard = Keyboard(60, USA)
# my_keyboard.keyboard_type()

# my_screen = Screen(1920, 1080, 18000000)
# my_screen.monitor_info()

# my_processor = Processor(USA, 0, 0)
# my_processor.brandscpu()
# my_processor.specs()

# #EX 3 MEU CODIGO

# class Ingredient:
#     def __init__(self, nom, quantite, unite):
#         self.nom = nom
#         self.quantite = quantite
#         self.unite = unite
    
#     def __str__(self):
#         return f"{self.quantite} {self.unite} {self.nom}"
    
# class Recette:
#     def __init__(self, nom2, temps, liste):
#         self.nom2 = nom2
#         self.temps = temps
#         self.liste = liste
    
#     def type_nom(self):
#         if choose == 1:
#             self.nom = ('Gâteau magique à la vanille')
#         else:
#             self.nom = ('Gâteau invisible aux pommes et pralines roses')

# class Livre:
#     def __init__(self, titre, lauteur, nombre, lrecettes):
#         self.titre = titre
#         self.lauteur = lauteur
#         self.nombre = nombre
#         self.lrecettes = lrecettes

# book =Livre('Book great', 'Copper', 4, 2)
# print(book)

# choose=input('Choose the cake that u want to see (1 or 2): ')
# if choose == 1:
#     nom = [ "Oeufs", 
#         "de Sucre en poudre", 
#         "de Lait entier", 
#         "Gousse de vanille", 
#         "de Beurre + 20 g pour le moule", 
#         "de Farine + 10 g pour le moule",
#         "Pincée de sel"
#     ]
#     quantite = [4, 125, 1/2, 1, 125, 115, 1]
#     unite = ['', 'g', 'L', '', 'g', 'g', '']
#     liste = list(zip(quantite,unite ,nom))
#     listcake=Ingredient(liste)

#     for pair in liste:
#         print(f"{pair[0]} {pair[1]} {pair[2]}")

#     my_cake=Ingredient(nom)
#     nom2= 'Gâteau magique à la vanille'
#     temps='Temps de cuisson 65 min'

# # Temps de cuisson 65 min Ingrédients :
# else:
#     my_cake=Livre()

#GPT
class Ingredient:
    def __init__(self, nome, quantidade, unidade):
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
    
    def __str__(self):
        return f"{self.quantidade} {self.unidade} de {self.nome}"

class Recipe:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo
        self.ingredientes = []
    
    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

class Book:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.receitas = []
    
    def adicionar_receita(self, receita):
        self.receitas.append(receita)
    
    def mostrar_livro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.paginas}")
        print("\nReceitas:")
        for receita in self.receitas:
            print(f"\nNome: {receita.nome}")
            print(f"Tempo de cozimento: {receita.tempo}")
            print("Ingredientes:")
            for ingrediente in receita.ingredientes:
                print(ingrediente)


# Criando os ingredientes
ingredientes_bolo_magico = [
    Ingredient("Ovos", 4, ""),
    Ingredient("Açúcar de confeiteiro", 125, "g"),
    Ingredient("Leite integral", 1/2, "L"),
    Ingredient("Vagem de baunilha", 1, ""),
    Ingredient("Manteiga", 125, "g"),
    Ingredient("Farinha", 115, "g"),
    Ingredient("Sal", 1, "pitada"),
]

ingredientes_bolo_invisivel = [
    Ingredient("Maçãs", 10, ""),
    Ingredient("Limão", 1, ""),
    Ingredient("Ovos", 2, ""),
    Ingredient("Açúcar", 50, "g"),
    Ingredient("Manteiga derretida", 20, "g"),
    Ingredient("Leite", 10, "cl"),
    Ingredient("Farinha", 75, "g"),
    Ingredient("Amido de milho", 25, "g"),
    Ingredient("Fermento em pó", 1/2, "sachê"),
    Ingredient("Sal", 1, "pitada"),
    Ingredient("Praliné rosa", 50, "g"),
]

# Criando as receitas
bolo_magico = Recipe("Bolo mágico de baunilha", "Tempo de cozimento 65 min")
bolo_invisivel = Recipe("Bolo invisível com maçãs e bombons rosa", "Tempo de cozimento 50 min")

# Adicionando os ingredientes às receitas
for ingrediente in ingredientes_bolo_magico:
    bolo_magico.adicionar_ingrediente(ingrediente)

for ingrediente in ingredientes_bolo_invisivel:
    bolo_invisivel.adicionar_ingrediente(ingrediente)

# Criando o livro de receitas
livro_receitas = Book("Livro de Receitas", "Chef Renomado", 100)

# Adicionando as receitas ao livro
livro_receitas.adicionar_receita(bolo_magico)
livro_receitas.adicionar_receita(bolo_invisivel)

# Exibindo o livro de receitas
livro_receitas.mostrar_livro()
