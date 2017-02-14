# Moivre-Formula
Python program that calculates and plots the roots of index n of a complex number

Proyecto para clase de Matemicas Avanzadas programado en Python para ser utilizado en una línea de comando. La ejecución del interpretador se llama a través del shebang (!#) incluído en el script principal, raiz_compleja.py, y especifica la dirección del interpretador python3 predeterminado. También se puede ejecutar directamente del interpretador Python 3 que tenga instalado los módulos NumPy y MatPlotLib.

REQUISITOS:
-Python 3 para arriba
-Módulos matplotlib y numpy para Python 3.
-Terminal Linux (para ejecución directa)

USO:
La ejecución directa del programa se hace 

    ./raiz_principal <a+bj> <inice_de_raiz>
    
<a+bj>           Es un número complejo (sin espacios entre el signo y la "j") de la forma a + ib 
<indice_de_raiz> Es cualquier número real que servirá como índice de la raíz.

En caso de no contar con el S.O. Linux se puede llamar al interpretador Python de la siguiente forma:
    
    python raiz_principal <a+bj> <indice_de_raiz>
    
