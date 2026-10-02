from noeud import Noeud, notation_polonaise

arbre = {
0: ('exp ', [1]) ,
1: ('+', [2, 3]) ,
2: ('2', []) ,
3: ('y', [])
}

deux = Noeud(2,None)
y = Noeud("y",None)
plus = Noeud("+",[deux.val, y.val])
exp = Noeud("exp", [plus.val])

print(exp.enfants)

#e = notation_polonaise()

#print(e)
