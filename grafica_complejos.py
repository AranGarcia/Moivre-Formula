import math
import matplotlib.pyplot as plt
import numpy

def graficar_complejos(radicando, indice, lista_complejos = None, ):
    """
    graficar_complejos(lista_complejos)
    Abre una nueva venta en la que se muestra un plano complejo
    y todos los números complejos en la lista que se pasó como argumento

    Argumentos:
    radicando: El numero complejo que es el radicando de la raíz.
        Ayuda a agregar el título de la ventana.
    indice: El indice de la raíz. Ayuda a a agregar el título de la ventana.
    lista_complejos: lista con todos los numeros complejos a graficar
    """
    if lista_complejos == None:
        return

    #Prepara la ventana donde se va graficar
    fig = plt.gcf()
    fig.canvas.set_window_title("Raices grado " + str(indice) + " de " + str(radicando))
    plt.ylabel('Imaginarios')
    plt.xlabel("Reales")
    plt.axis('equal')
    plt.grid()

    #Dibuja lineas desde el origen al número complejo
    for i in range(len(lista_complejos)):
        plt.plot([0, numpy.real(lista_complejos[i])], [0, numpy.imag(lista_complejos[i])])

    #Dibuja el círculo para representar el límite de todas las raíces
    radio = math.sqrt( numpy.real(lista_complejos[0]) ** 2 + numpy.imag(lista_complejos[0]) ** 2 )
    print(radio)
    circulo = plt.Circle((0,0), radio, color = 'k', fill = False)
    ax = plt.gca()
    ax.add_artist(circulo)

    #Dibuja linea desde el origen al complejo original (radicando)
    plt.plot([0, numpy.real(radicando)], [0, numpy.imag(radicando)], 'k--', label = "Radicando: " + str(radicando))

    plt.show()