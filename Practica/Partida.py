
from Tablero import Tablero
from Jugador import Jugador
from Maquina import Maquina
'''
Created on 28 ene. 2019

@author: Nathan
'''

class Partida:
 while True:
    try:
        entrada = int (input("Pulsa 1 para crear una partida\n"))
        if(entrada == 1):
            tablero = Tablero()
            maquina = Maquina()
            maquina.iniciar(tablero)
            jugador = Jugador()
            jugador.iniciarJugador(tablero)
            while True:
             try:
                print("----------------------------------------------------")
                print("1 para disparar")
                print("2 para ver el mapa del jugador")
                print("3 para finalizar el juego")
                print("4 para ver el mapa de la maquina NO HAGAS TRAMPAS")
                print("----------------------------------------------------\n")
                entrada = int(input("\n"))
                if entrada == 1:
                    entradax = input("Ingresa la coordenada X\n")
                    entraday = input("Ingresa la coordenada Y\n")
                    x = int(entradax)
                    y = int(entraday)
                    if (x >= 0 and x <= 9 and y >= 0 and y <= 9 ):
                        jugador.disparar(x,y)
                    else:
                        print("las coordenadas para X e Y deben ser mayores o iguales a 0 Y menores o iguales a 9")

                if entrada == 2:
                    tablero.mostrar_mapa_jugador()

                if (entrada == 3):
                    tablero.finalizar_juego()

                if (entrada == 4):
                    tablero.mostrar_mapa_maquina()
             except ValueError:
                 print("Debes ingresar numeros")
    except ValueError:
        print("Debes ingresar numeros")









