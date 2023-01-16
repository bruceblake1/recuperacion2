import random
intentos = 0
print ("Hola ¿Cual es tu nombre?")
nombre = input()
numero = random.randint(1,10)
print ("Piensa en un numero del 1 al 10")
while intentos < 10:
    print ("Hola", nombre, "Tienes 10 intentos suerte")
    adivina = input()
    adivina = int(adivina)
    intentos = intentos + 1
    if adivina < numero:
        print("Debes ingresar un numero mas grande")
    if adivina > numero:
        print("Debes ingresar un numero mas pequeño")
    elif adivina == numero:
        print("Bingo encontraste el número")
        break