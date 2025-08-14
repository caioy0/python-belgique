''' commands print/if/else/format/intput/
n = 5 ** 3 or n = pow(5,3)
n = 5/3 da o valor em float
n = 5//3 da o valor em int
'''
# exercices:
'''
print("Saisir le nom de l'immeuble",)
nom=input()

print("Saisir le numero de l'immeuble",)
num=input()

print("Saisir le largura de l'immeuble",)
medid1=float(input())

print("Saisir le comprimento de l'immeuble",)
medid2=float(input())
area= medid1*medid2

print(f"La superficie du local: {num}, se trouvant dans l'immeuble: {nom} est de {area} m^2")
'''
'''print("Saisir les valeurs pour R: ")
res=float(input())
print("Saisir les valeurs pour I: ")
cur=float(input())
volt=cur*res
print("U valeurs c'est: ", volt)
'''
'''
print('saisir les minut: ')
minut=float(input())
heure = int(minut/60)
minut2= int(minut%60)
print(f'l heure c est: {heure} e minut {minut2}')
'''
"""
rayon=float(input('sansir ici rayon: '))
area= 3.14*rayon**2
print(f'c est suface: {area} cm2')
"""
'''
print('Saisir la distance en km: ')
km=float(input())
print('durée d un trajet (heures): ')
herus=int(input())
print('durée d un trajet (minutes): ')
minut=int(input())
minut2= float(minut/60)
vm=float(km/(herus+minut2))
print(f'pour un trajet de {km} km effectué en {herus} heures et {minut} minutes, on a une vitesse de {vm} km/h')
'''
'''
print('Entrer la taille pour les côtés a: ')
a=int(input())
print('Entrer la taille pour les côtés b: ')
b=int(input())
print('Entrer la taille pour les côtés c: ')
c=int(input())
if pow(c,2) == pow(a,2) + pow(b,2):
    print('C est triangle retangle')
else:
    print('c est pas dans trinagle retangle')
'''
'''
print('Entrer la taille pour les côtés a: ')
a=int(input())
print('Entrer la taille pour les côtés b: ')
b=int(input())
print('Entrer la taille pour les côtés c: ')
c=int(input())
if a==b and a==c and b==c:
    print('C est triangle equilateral')
elif a==b or a==c or b==c:
    print('c est trinagle isocele')
else :
    print('c est triangle')
'''

