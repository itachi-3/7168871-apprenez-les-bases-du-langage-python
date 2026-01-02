numéro_1= input("quel est le premier nombre ?")
numéro_2= input("quel est mon deuxiéme nombre?")
if not numéro_1.isnumeric() or not numéro_2.isnumeric():
  print("erreur les deux nombres sont pas des entiers")
  raise SystemExit("Fin du programme")
numéro_1= int(numéro_1)
numéro_2= int(numéro_2)
opération = input("choisi l'une de ces opérations +,-,:,*")
if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")
