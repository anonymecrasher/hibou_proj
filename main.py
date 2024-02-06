## Importation des modules
from binarytree import Node
import pickle

## Déclaration des fonctions
def sauvegarde(arbre, nom_fichier):
    fichier = open(nom_fichier + '.obj', 'wb')
    pickle.dump(arbre,fichier)
    fichier.close()
    
def charge(nom_fichier):
    fichier = open(nom_fichier + '.obj', 'rb')
    arbre = pickle.load(fichier)
    fichier.close()
    return arbre

def q_hibou(start=False,arbre=None):
    if start:
        a = input('Voulez vous commencer avec un fichier contenant des donnés ? ')
        if a == 'o':
            arbre = charge(str(input('entrez le nom du dossier ')))
        elif a == 'n':
            ani,carac  = Node(str(input('''Donne moi un animal '''))), Node(str(input('''Donne moi une caracteristique de l'animal ''')))
            arbre = carac
            arbre.right = ani
            sauvegarde(arbre, 'hbarbre')
        return q_hibou(False,arbre)
    else:#aprés premier fois dans le programe
        if arbre == None:
            animal = str(input("""quel etait l'animal ? """))
            carac = str(input("""Donne une caracteristique qui le diferentie de l'autre animal """))
            ancien_a = arbre
            arbre = Node(carac,Node(animal),ancien_a)
            return arbre
        elif arbre.left == None and arbre.right == None:
            ans = input("""esque l'animal est """+ arbre.value+"""? y/n """)
            if ans == 'y':
                pass
            elif ans == 'n':
                animal = str(input("""quel etait l'animal ? """))
                carac = str(input("""Donne une caracteristique qui le diferentie de l'autre animal """))
                ancien_a = arbre
                arbre = Node(carac,Node(animal),ancien_a)
                return arbre
        else:
            valeur = str(arbre.value)
            message = """esque l'animal est """ + valeur +"""? y/n """
            ans = input(message)
            if ans == 'y':
                return Node(valeur,q_hibou(False, arbre.left),arbre.right)
            else:
                return Node(valeur,arbre.left,q_hibou(False, arbre.right))
                
            
        
    
            
            
    

## Déclaration des classes


## fonction principale
def main():
    arbre = charge('hbarbre')
    arbre = q_hibou(True,arbre)
    sauvegarde(arbre,'hbarbre')
    
    print(arbre)
    
    
    

## Programme principal
if __name__ == '__main__':
    main()
