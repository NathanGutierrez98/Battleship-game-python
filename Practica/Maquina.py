from Barco import Barco
from Tablero import Tablero
import random as randint
'''
Created on 28 ene. 2019

@author: Nathan
'''
class Maquina():

 def iniciar(self, tablero):
    self.tablero = tablero
    t_barcos = (2, 3, 3, 4, 5)

    for i in range (len(t_barcos)):

            barco = Barco()

            longitud = t_barcos[i]
            barco.longitud = t_barcos[i]
            while True:
                x = randint.randint(0, 10)
                y = randint.randint(0, 10)

                opcion = randint.randint(0,1)

                if opcion == 0:

                    if self.tablero.comprobar_posicion_x(x, y, longitud,barco) == True:
                        barco.iniciar(x, y, longitud)
                        break
                    else:
                        if self.tablero.comprobar_posicion_y(x, y, longitud,barco) == True:
                            barco.iniciar(x, y, longitud)
                            break


                if opcion == 1:
                    if self.tablero.comprobar_posicion_y(x, y, longitud, barco) == True:
                        barco.iniciar(x, y, longitud)
                        break
                    else:
                        if self.tablero.comprobar_posicion_x(x, y, longitud,barco) == True:
                            barco.iniciar(x, y, longitud)
                            break

































