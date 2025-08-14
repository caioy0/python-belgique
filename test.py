nom = [ "Oeufs",  "125 g de Sucre en poudre", 
"1/2 L de Lait entier", 
"1 Gousse de vanille", 
"125 g de Beurre + 20 g pour le moule", 
"115 g de Farine + 10 g pour le moule",
"1 Pincée de sel"]
quantite = [4, '125g', '1/2L', 1, '125g', '115g', 1]
liste = list(zip(quantite,nom))
for pair in liste:
    print(f"{pair[0]} {pair[1]}")