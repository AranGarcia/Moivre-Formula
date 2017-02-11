#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy

def graficar_complejos(lista_complejos = None):
    """
    Abre una nueva venta en la que se muestra un plano complejo
    y todos los números complejos en la lista que se pasó como argumento

    Argumentos:
    lista_complejos: lista con todos los numeros complejos a graficar
    """
    if lista_complejos == None:
        return
    
    plt.ylabel('Imaginarios')
    plt.xlabel("Reales")

    for i in range(len(lista_complejos)):
        plt.plot([0, numpy.real(lista_complejos[i])], [0, numpy.imag(lista_complejos[i])])

    plt.show()