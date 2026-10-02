
class Lieu :
    pass

def est_lieu(objet):
    return isinstance(objet, Lieu)

class Ville :
    pass

def ajouter_attribut_ville(ville, nom, pop):
    ville.nom = nom
    ville.population = pop

ajouter_attribut_ville()
