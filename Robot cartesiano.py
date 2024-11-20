print ("Elige una opcion")
print ("Selecciona 1. para mover boton para eje X")
print ("Selecciona 2. para mover boton para eje Y")
print ("Selecciona 3. para mover boton para eje Z")

class Robot_cartesiano:
    def __init__(self, status):
        self.status = " "

    def eje_X (self):
        print ("AVANCE EN POSICION EN EJE X")
        Dimension = int (input("Coloca la dimension en cm que debe moverse en X:  "))
        if Dimension <= 300:
            print ("El robot avanza", Dimension , "cm en eje X")
            print ()
            opcion = int (input("Selecciona 0 para elegir otro movimiento:  "))
            if opcion == 0:
                Robot_cartesiano.info(self)
            else:
                Robot_cartesiano.termino(self)
        else:
            print ()
            print ("ALERTA, Sobrepasada la dimension permitida")
            opcion = int (input("Selecciona 5 para regresar:  "))
            if opcion == 5:
                Robot_cartesiano.eje_X(self)
            else:
                Robot_cartesiano.termino(self)

    def eje_Y (self):
        print ("AVANCE EN POSICION EN EJE Y")
        Dimension1 = int (input("Coloca la dimension en cm que debe moverse en Y:  "))
        if Dimension1 <= 300:
            print ("El robot avanza", Dimension1 , "cm en eje Y")
            print ()
            opcion = int (input("Selecciona 0 para elegir otro movimiento:  "))
            if opcion == 0:
                Robot_cartesiano.info(self)
            else:
                Robot_cartesiano.termino(self)
        else:
            print ()
            print ("ALERTA, Sobrepasada la dimension permitida")
            opcion = int (input("Selecciona 5 para regresar:  "))
            if opcion == 5:
                Robot_cartesiano.eje_Y(self)
            else:
                Robot_cartesiano.termino(self)           
    
    def eje_Z (self):
        print ("AVANCE EN POSICION EN EJE Z")
        Dimension2 = int (input("Coloca la dimension en cm que debe moverse en Z:  "))
        if Dimension2 <= 150:
            print ("El robot avanza", Dimension2 , "cm en eje Z")
            print ()
            print ("Selecciona 0 para elegir otro movimiento")
        else:
            print ()
            print ("ALERTA, Sobrepasada la dimension permitida")
            opcion = int (input("Selecciona 5 para regresar:  "))
            if opcion == 5:
                Robot_cartesiano.eje_Z(self)
            else:
                Robot_cartesiano.termino(self) 
       

    def termino (self):
        print ("Se termina el programa")

    def info(self):
        print ()
        Boton = int(input("Selecciona la OPCION:  "))
        if Boton == 1:
            Robot_cartesiano.eje_X(self)
            
        elif Boton == 2:
            Robot_cartesiano.eje_Y(self)
            

        elif Boton == 3:
            Robot_cartesiano.eje_Z(self)
        
        else:
            print("No existe avance")
           

Robot1 = Robot_cartesiano("uno")
Robot1.info()