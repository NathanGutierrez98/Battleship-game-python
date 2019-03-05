'''
Created on 28 ene. 2019

@author: Nathan
'''
from Barco import Barco


import sys

class Tablero():
    aguas = 0
    barcos_hundidos = 0
    barcos_tocados = 0
    mapa = []
    mapaJugador = []
    def inicializar_mapa(self):
       
        for x in range(10):
            self.mapa.append([])
            self.mapaJugador.append([])
            for y in range(10):
                self.mapa[x].append(y)
                self.mapa[x][y] = " "
                self.mapaJugador[x].append([y])
                self.mapaJugador[x][y] = " "




    def mostrar_mapa_maquina(self):
        print("      0     1     2     3     4     5     6     7     8     9\n")
        for x in range (10):
            print(x, end = "    ")
            for y in range (10):
                 print("["+str(self.mapa[x][y]), end="]   ")
            print("\n")


    def mostrar_mapa_jugador(self):
        print("      0     1     2     3     4     5     6     7     8     9\n")
        for x in range (10):
            print(x, end = "    ")
            for y in range (10):
                
                print("["+str(self.mapaJugador[x][y]), end="]   ")
                
            print("\n")




    def comprobar_posicion_x(self,x,y,longitud,barco):
        contador = x
        for i in range(longitud):
            if contador > 9 or y > 9:
                return False
            if self.mapa[contador][y] != " ":
                return False
            contador = contador + 1

        contador = x
        for i in range(longitud):
            self.mapa[contador][y] = barco
            contador = contador + 1
        return True



    def comprobar_posicion_y(self,x,y,longitud,barco):

        contador = y
        for i in range (longitud):
            if contador >9 or x > 9:
                return False
            if self.mapa[x][contador] != " ":
                 return False
            contador = contador+1

        contador = y
        for i in range (longitud):
            self.mapa[x][contador] = barco
            contador = contador + 1
        return True



    def disparar(self,x,y):
        
        if self.mapaJugador[x][y] == " ":
            if self.mapa[x][y] != " ":
                
               
                barco = Barco()
                barco = self.mapa[x][y]
                barco.tocado()

                self.mapaJugador[x][y] = barco
                self.mostrar_mapa_jugador()
                if(barco.get_vida() == 0):
                    print ("TOCADO Y HUNDIDO")
                    self.barcos_hundidos = self.barcos_hundidos +1

                    self.barcos_tocados = (self.barcos_tocados+1) - barco.longitud_barco()
                    self.ganador()
                else:
                    self.barcos_tocados = self.barcos_tocados +1

                    print("TOCADO")

            
            else:
                print("AGUA")
                self.mapaJugador[x][y] = "A"
                self.aguas = self.aguas +1
        else:
            print("POSICION YA DISPARADA")

    #comprueba si finalmente se han hundido todos los barcos
    def ganador(self):
        ganador = False

        for x in range(10):

            for y in range(10):
               if str(type(self.mapa[x][y])) == "<class 'Barco.Barco'>":
                    barco = Barco()
                    barco = self.mapa[x][y]
                    if barco.get_vida() == 0:
                        ganador = True
                    else:
                        ganador = False
                        break
                        break


        if ganador:
            print("¡Enhorabuena! Eres el Ivan Sidorenko de los barcos. Los has fulminado.\n ☭☭☭☭☭☭ ¡Gloria a la patria Odoo!☭☭☭☭☭☭☭")
            self.finalizar_juego()

    def estadisticas(self):
        return "Fin del juego, las estadisticas son las siguientes: \n aguas: {} \n barcos hundidos: {} \n barcos tocados: {}".format(self.aguas, self.barcos_hundidos, self.barcos_tocados)
        
    def finalizar_juego(self):
        print(self.estadisticas())
        sys,exit(1)
cuadro = Tablero()
cuadro.inicializar_mapa()



    
    




            
            
        
                
        

            
       
        
        
        
       



    
    