def salaire_Mensuel(salaire_annuel):
  return salaire_annuel  /  12

def salaire_hebdomadaire(salaire_Mensuel):
  return salaire_Mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heure_travaillées):
  return salaire_hebdomadaire / heure_traillées

salaire_annuel= float(input("quel est ton salaire annuel?")
heure_travaillées = float(input("quel est ton nombre d'heure par semaine?:)
mois = salaire_Mensuel(salaire_annuel)
semaine = salaire_hebdomadaire(mois)
heure = salaire_horaire(semaine, heure_travaillées)
print(f""Votre salaire horaire est de {heure} euros.")
