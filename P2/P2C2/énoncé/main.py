nombres= input("saisissez une suites de nombres séparées par la virgule:")
listes = nombres.split(",")
listees_entiers= []
for x in listes:
  listes_entiers.append(int(x))
print(listes_entiers)
# Exemple de liste d'entiers
liste_entiers = [1, 2, 3, 4, 5]

# 1. Calculer et afficher la somme
somme = sum(liste_entiers)
print("Somme :", somme)

# 2. Calculer et afficher la moyenne
moyenne = somme / len(liste_entiers)
print("Moyenne :", moyenne)

# 3. Compter les nombres supérieurs à la moyenne
compteur = 0
for x in liste_entiers:
    if x > moyenne:
        compteur += 1

print("Nombre de nombres supérieurs à la moyenne :", compteur)
