'''
Created on 28 ene. 2019

@author: Nathan
'''



class Barco():

    def iniciar(self, x, y, longitud):
        self.x = x
        self.y = y
        self.longitud = longitud
        self.vida = longitud
        self.impactos = 0




    def colocar_barco(self, x, y):
        self.x = x
        self.y = y
        self.partida.colocar_barco(self.x, self.y)


    def longitud_barco(self):
        return self.longitud

    def __str__(self):
        return "{}".format(self.longitud)


    def tocado(self):
        self.vida = self.vida-1


    def get_vida(self):
        return self.vida

    def get_impactos(self):
        return self.impactos




