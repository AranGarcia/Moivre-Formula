#!/usr/bin/python3

import formula_moivre
import grafica_complejos
import sys

#Determina la cantidad correcta de argumentos
if len(sys.argv) != 3:
    sys.exit("\n  ERROR: cantidad de argumentos inválidos\n"
        "\t Uso: raiz_compleja <radicando> <indice>\n")

#Verifica que el segundo argumento sea un complejo valido
try:
    z = complex(sys.argv[1])
except ValueError:
    sys.exit("\n  ERROR: " + str(sys.argv[1]) + " no es un numero complejo válido de la forma a+bj'\n")

#Verifica que el tercer argumento sea un numero natural
try:
    indice = int(sys.argv[2])
    if indice <= 0:
        raise ValueError()
except ValueError:
    sys.exit("\n  ERROR: " + str(sys.argv[2]) + " no es un numero natural'\n")


r = formula_moivre.sacarRaices(z, indice);

for i in r:
    print(i)

grafica_complejos.graficar_complejos(z, indice, r)
