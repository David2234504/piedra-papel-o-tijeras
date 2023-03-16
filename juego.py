print("-------------------------------------")
print("-------Piedra, papel o tijeras-------")
print("-------------------------------------")
import random

print("1 ---> Tijeras")
print("2 ---> Piedra")
print("3 ---> Papel")
Tijeras = 1
Piedra = 2
Papel = 3

p = int(input("Escoja entre piedra, papel o tijeras: "))
pc = random.randint(1,3)

if 1 <= p <= 3:
    if p == pc:
        rta = "Empate"
    elif p == 1 and pc == 2:
        rta = "Ganó la Maquina"
    elif p == 1 and pc== 3:
        rta = "Ganó la persona"
    elif p == 2 and pc== 1:
        rta = "Ganó la persona"
    elif p == 2 and pc== 3:
        rta = "Ganó la maquina"
    elif p == 3 and pc== 1:
        rta = "Ganó la maquina"
    elif p == 3 and pc== 2:
        rta = "Ganó la persona"


    if p == 1:
        p = "tijeras"
    elif p == 2:
        p = "piedra"
    elif p == 3:
        p = "papel"

    if pc == 1:
        pc = "tijeras"
    elif pc == 2:
        pc = "piedra"
    elif pc == 3:
        pc = "papel"

    print("Opcion persona:",p,)
    print("Opcion maquina:",pc)
    print(str(rta))
else:
    rta = "Entrada invalida"
    print(str(rta))
