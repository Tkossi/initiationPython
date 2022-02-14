# variables
var1 = 10 # int
var2 = 4.2 # float
var3 = "Bonjour" # string
var4 = True # Boolean
var5 = [ "Bonjour", 5 , 3.2] # list

print("total est egal a")
total = var1 + var2
print(total)

#conditions
if var1 > var2 :
    print( "c'est plus grand")
elif var1 < var2 :
    print( " c'est plus petit")
else:
    print( " c'est égal ")

# Boucles
#while var1 > var2 :
   # print( var1 )
    #var1 = var1 - 1

for element in var5 :
    print(element)

print ( "----------------------------------------")
# Fonctions
def add( a ,b ) :
    resultat = a + b
    return resultat

total = add( var1 , var2 )
print( total)

def div ( a, b):
    resultat = a / b
    return resultat

total = div ( var1 , var2)
print( total )

def mult( a ,b ):
    resultat = a*b
    return resultat
total = mult ( var1 , var2 )
print(total)

def soust( a,b):
    resultat = a - b
    return resultat
total = soust ( var1 , var2 )
print( total )