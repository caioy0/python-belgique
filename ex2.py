#1 while

n = int(input('Insert number: '))
if n < 0:
    print('Número negative. Insert positive.')
else:
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10
    print('Número invertido:', reversed_number)

#2
'''
n = int(input('Saisir un nombre entier positif : '))
if n < 0:
    print('Nombre négatif. Veuillez saisir un nombre positif.')
else:
    total = 0
    count = 0
    while n > 0:
        digit = n % 10
        total += digit
        count += 1
        n //= 10
    if count == 0:
        print("Le nombre est 0")
    else:
        moyenne = total / count
        print(f"La somme des chiffres est {total} et la moyenne est {moyenne}.")
'''
#3
'''
from math import sqrt

numero = float(input('Saisir un nombre flottant : '))

for _ in range(4):  #_= sem variavel, possso utilzar o i.
    raiz = sqrt(numero)
    print(raiz)
    numero = raiz
'''
#4
'''
for i in range(1, 11):  
    for j in range(1, 11): 
        print(f"{i*j:3}", end=" ")  # Usando f-strings para formatar os números
    print()  # Mudar para a próxima linha após cada linha concluída
'''
#5
'''
# Solicitar o número de linhas ao usuário
num_linhas = int(input("Insira o número de linhas para o triângulo: "))
# Loop para imprimir as linhas do triângulo
for linha in range(1, num_linhas + 1):
    print("*" * linha)
'''
#6
'''
import random

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Instruções do jogo
print("Devinez le nombre entre 1 et 100.")

# Loop para permitir múltiplas tentativas
tentativas = 0
while True:
    # Incrementar o número de tentativas
    tentativas += 1

    # Solicitar uma tentativa do jogador
    tentativa = int(input(f"Essai {tentativas}: que proposez-vous? "))

    # Verificar se a tentativa está correta
    if tentativa == numero_secreto:
        print(f"C'est correct! Le nombre à trouver était {numero_secreto}")
        break
    elif tentativa < numero_secreto:
        print("Non. Le nombre à trouver est plus grand.")
    else:
        print("Non. Le nombre à trouver est plus petit.")
'''

#solucao do professor
#1

'''
nb = int(input("entrez un entier: "))
nbOrigine = nb
nbNouveau = 0
i = 0
while i < 4: #or for i in range (0,4,1): 
    nbNouveau = nbNouveau * 10 + nb%10
    nb=nb//10
    i=1+1

print(f"nbOrigine = {nbOrigine}, nbNouveau {nbNouveau}")

nb = int(input("entrez un entier: "))
nbOrigine = nb
nbNouveau = 0 #or for i in range (0,4,1): 
i = 0
for i in range (0,4,1): 
    nbNouveau = nbNouveau * 10 + nb%10
    nb=nb//10

print(f"nbOrigine = {nbOrigine}, nbNouveau {nbNouveau}")


nb = int(input("entrez un nbre de lignes: "))

j=1
while j <=nb:
    i=0
    while(1<j):
        print("*",end=' ')
        i+i+1
    j += 1
    print("")
    
'''

