liste1 = ["a" ,"b" , "c"]
liste2 = [ "ananas" , "banane" , "citron"]

# print(liste1[0])
# index = liste1.index( "a" )
# print ( "position de la lettre" , index)

print ( "quelle lettre voulez vous ? a -> c")
lettre = input(">>>") # on demande de taper une lettre au clavier

index = liste1.index(lettre) # on recherche la position de la lettre dans la premiere liste
print(liste2[index]) # on affiche le mot associé à l'index dans la liste 2
