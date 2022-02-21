# importer nos librairies
# on nous affiche : 

# on entre un caractère de a -> z
# on tape une lettre
# on retrouve la position de la lettre dans l'alphabet
# on affiche le code morse correspondant à l'index
# le programme nous retourne les symboles correspondants

import liste_morse
print ( " entrez un caractere de a -> z")
lettre = input( ">>>")

index = liste_morse.alphabet.index(lettre)
print( "le code morse est" , liste_morse.morse[index])





