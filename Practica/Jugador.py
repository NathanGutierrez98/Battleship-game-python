'''
Created on 28 ene. 2019

@author: Nathan
'''
class Jugador():

    def iniciarJugador(self, tablero):
        self.tablero = tablero



    def disparar(self,x,y):
        self.tablero.disparar(x,y)