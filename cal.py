# function addition
def addition(num1, num2):
    som = num1 + num2
    print(som)
    return som

# function soustraction
def soustraction(num1, num2):
    som = num1 - num2
    print(som)
    return som

# function multiplication
def multiplication(num1, num2):
    som = num1 * num2
    print(som)
    return som

# function division
def division(num1, num2):
    som = num1 / num2
    print(som)
    return som

# function modulo
def modulo(num1, num2):
    som = num1 % num2
    print(som)
    return som

# function exposant
def exposant(num1, num2):
    som = num1 ** num2
    print(som)
    return som

# Liste pour choisir Operation
def listChoix():
    print('Choisissez parmi les options suivantes:') 
    print("""
      1. 'a' pour faire une addition
      2. 's' pour faire une soustration
      3. 'm' pour faire une multiplication
      4. 'd' pour faire une division
      5. 'r' pour trouver le reste
      6. 'e' pour trouver un exposant       
      7. 'x' pour quitter l' application
      """) 
    choix = input('Tapez votre choix: ')
    return choix

choixRetenue = listChoix()
choixRetenue = choixRetenue.strip(" ").lower()

i = 0
if choixRetenue == 'a' or choixRetenue == 's' or choixRetenue == 'm' or choixRetenue == 'd' or  choixRetenue == 'r' or choixRetenue == 'e' or choixRetenue == 'x':
    i = 1
else:
    i = 0
    print()
    print('Vous avez choisi une valeur incorrecte. Essayez a nouveau...')
    listChoix()
    
#logique pour la gestion de choix
if choixRetenue == 'a':
    print('Vous voulez faire une addition...')
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la  dexieme valeur: '))
    addition(val1, val2)

elif choixRetenue == 's':
    print(' ')
    print('Vous voulez faire une Soustraction...')
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la  dexieme valeur: '))
    soustraction(val1, val2)
    
elif choixRetenue == 'm':
    print(' ')
    print('Vous voulez faire une Multiplication...')
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la  dexieme valeur: '))
    multiplication(val1, val2)

elif choixRetenue == 'd':
    print(' ')
    print('Vous voulez faire une Division...')
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la  dexieme valeur: '))
    division(val1, val2)
    
elif choixRetenue == 'r':
    print(' ')
    print('Vous voulez trouver le reste...')
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la  dexieme valeur: '))
    modulo(val1, val2)

elif choixRetenue == 'e':
    print(' ')
    print('Vous voulez trouver l\exposant d\'une valeur...')
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la l\'exposant: '))
    exposant(val1, val2)

elif choixRetenue == 'x':
    print('vous avez quitte l\'application, Bye!!!')
    exit()
    
else:
    listChoix()
