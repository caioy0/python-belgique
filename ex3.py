# '''
# l1 = [1,2,3,4,]
# for i in range (1):
#     l1.append(float(input('Insert numbers: ')))

# print(l1)

# for i in range (0,l1):
#     print("")
# '''
# #EX1
# valeurs = [None] * 5
# valeurs[-1] = float(input("Entrez un nombre flottant pour la dernière valeur de la liste : "))
# for i in range(len(valeurs) - 2, -1, -1):
#     valeurs[i] = valeurs[i + 1] ** 0.5
# print("valeurs =", valeurs)

# #EX2 
# valeurs = [int(input("Entrez un nombre entier pour la première valeur de la liste : "))]
# for i in range(1, 10):
#     valeurs.append(sum(valeurs[:i])) #VER APPEND E SUM
# print("valeurs =", valeurs)

# #Ex3
# valeurs = [3, 7, 1, 9, 4] #Inicilaizacao aleatoria da lista
# valeur = int(input("Entrez une valeur entre 0 et 10 : "))
# for i in range(len(valeurs)):
#     if valeur < valeurs[i]:
#         valeurs.insert(i, valeur)
#         break
# else:
#     valeurs.append(valeur)

# valeurs.sort()  # Ordena a lista

# print("valeurs triées:", valeurs)


# #Ex4
# valeurs = []
# for _ in range(10):
#     valeur = float(input("Entrez une valeur flottante : "))
#     if valeur not in valeurs:
#         for i in range(len(valeurs)):
#             if valeur > valeurs[i]:
#                 valeurs.insert(i, valeur)
#                 break
#         else:
#             valeurs.append(valeur)  # Adiciona no final se for o maior valor
#     else:
#         print("La valeur est déjà présente dans la liste. Elle ne sera pas ajoutée.")
# print("valeurs =", valeurs)

#Ex5
import random
valeurs = [random.randint(0, 7) for _ in range(5)]
print("valeurs initial =", valeurs)
valeur_a_supprimer = int(input("Entrez une valeur entière à supprimer : "))
while valeur_a_supprimer in valeurs:
    valeurs.remove(valeur_a_supprimer)
print("valeurs après suppression =", valeurs)
'''
#Ex6
valeurs = [3, 17, 10, -8]
print("valeurs inicial =", valeurs)
valeurs_com_zeros = []
for valor in valeurs:
    valeurs_com_zeros.append(valor)
    valeurs_com_zeros.append(0)
valeurs_com_zeros.pop()
print("valeurs com zeros entre eles =", valeurs_com_zeros)
'''

#logan soluction
#import math
# valeurs = [None] * 5
# valeurs[-1] = float(input("Entrez un nombre flottant pour la dernière valeur de la liste : "))
# for i in range(len(valeurs) - 2, -1, -1):
#     valeurs[i] = valeurs[i + 1] ** 0.5
# print("valeurs =", valeurs)

# valeurs = [None] * 5
# valeurs[0] = float(input("Entrez un nombre flottant pour la dernière valeur de la liste : "))
# for i in range(1, len(valeurs)):
#     valeurs[i]=math.sqrt(valeurs[i-1])


# print(valeurs[::-1])