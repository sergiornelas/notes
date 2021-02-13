"""
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""

#Character input ----------------------
"""
name = input("Enter yor name: ")
age = int(input("Enter yor age: "))
extra1 = int(input("Another number: "))

year = 2020
total = (year-age) + 100

for i in range(extra1):
    print (f'Dear {name}, you\'ll be 100 years old in: {total}')
"""

#Odd or Even ----------------------
"""
number = int(input("Give me a number: "))

if number % 2 == 0:
    print("It\'s odd")
    if number % 4 == 0:
        print("It's multiple of 4")
else:
    print("It\'s even")
"""

#list less than ten ----------------------
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
number = int(input("Enter a number: "))

print (number)

for element in a:
    if element < number:
        b.append(element)

print(b)
"""

#divisors ----------------------

"""
#entero de entrada
num = int(input("Please choose a number to divide: "))

#numeros del 1 al num se almacenan en la lista listRange
listRange = list(range(1,num+1))

#se crea una lista para los divisores
divisorList = []

#para cada numero dentro de la lista listRange
for number in listRange:
    #si el residuo del entero de entrada y cada numero es igual a 0
    if num % number == 0:
        #almacena el residuo a la lista para los divisores
        divisorList.append(number)

#imprimir lista de divisores
print(divisorList)
"""

#List Overlap ----------------------

"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
#c = {}
#c = set()

for element in a:
    if element in b:
        #c.add(element)
        c.append(element)

c = list(dict.fromkeys(c))
print (c)
"""

#String lists ----------------------
# comprobar si el string de entrada es un palíndromo
"""
string = list(input("Enter yor name: "))

largoCadena = len(string)-1

string2 = string[::-1]
puntos = 0

for i in string:
        if string[0] == string2[0]:
            puntos += 1
            if largoCadena == puntos:
                print ("es palindromo")
"""

#List comprehensions ----------------------
#solo dame los números pares de la lista utilizando una linea
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [element for element in a if element %2 == 0]

print(b)
"""

#Rock Paper Scissors----------------------

def juego (p1, p2):
    if p1 == p2:
        return ("It's a draw")
    elif p1 == "rock":
        if p2 == "paper":
            return ("player 2 wins!")
        elif p2 == "scissors":
            return ("player 1 wins!")
    elif p1 == "paper":
        if p2 == "rock":
            return ("player 1 wins!")
        elif p2 == "scissors":
            return ("player 2 wins!")
    elif p1 == "scissors":
        if p2 == "rock":
            return ("player 2 wins!")
        elif p2 == "paper":
            return ("player 1 wins!")
    
while (True):
    player1 = input("P1, enter rock, paper or scissors: ")

    while(player1 != "rock" and player1 != "paper" and player1 != "scissors"):
        player1 = input("P1, enter rock, paper or scissors AGAIN: ")

    player2 = input("P2, enter rock, paper or scissors: ")

    while(player2 != "rock" and player2 != "paper" and player2 != "scissors"):
        player2 = input("P2, enter rock, paper or scissors AGAIN: ")

    print(juego(player1, player2))

    newGame = input ("Start new game?: yes/no ")
    while (newGame != "yes" and newGame != "no"):
        newGame = input ("Start new game AGAIN?: yes/no ")
    if newGame == "no":
        break
