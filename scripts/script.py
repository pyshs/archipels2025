sortie_fichier = True
noeuds = []
liens = []
entree = None
print("Entrez les liens du réseau (source, cible, poids). Tapez 'fin' pour terminer.")
while entree != "fin":
    entree = input()
    entree = entree.lower()
    if entree != "fin":
        elements = entree.split(",")
        if len(elements) != 3:
            print("Format incorrect. Veuillez entrer 'source,cible,poids'.")
            continue
        source, cible, poids = elements
        if source not in noeuds:
            noeuds.append(source)
        if cible not in noeuds:
            noeuds.append(cible)
        liens.append((source, cible, int(poids)))
print("Noeuds :", noeuds)
print("Liens :", liens)
if sortie_fichier:
    with open("reseau.txt", "w") as f:
        f.write("Noeuds:\n")
        for n in noeuds:
            f.write(f"{n}\n")
        f.write("Liens:\n")
        for s, c, p in liens:
            f.write(f"{s},{c},{p}\n")
    print("Résultat écrit dans le fichier reseau.txt")
