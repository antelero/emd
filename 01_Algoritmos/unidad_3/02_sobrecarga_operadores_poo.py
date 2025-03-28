import math

class Punto:
    """ Representa un punto en el plano cartesiano """
    def __init__(self, x = 0, y = 0):
        """ Inicializa los valores de las coordenadas x e y """
        self._x = x
        self._y = y
        
    def __str__(self):
       return f"({self._x}, {self._y})"
        
       
    def distancia(self):
        """ Calcula la distancia de un punto particular al origen """
        return math.sqrt(math.pow(self._x, 2) + math.pow(self._y, 2))
    
    def set_x(self, new_x):
        self._x = new_x
    
    def get_x(self):
        return self._x
    
    def set_y(self, new_y):
        self._y = new_y
    def get_y(self):
        return self._y
    
    def __lt__(self, p):
        return self.distancia() < p.distancia()
    
    def __le__(self, p):
        return self.distancia() <= p.distancia()
    
    def __gt__(self, p):
        return self.distancia() > p.distancia()
    
    def __ge__(self, p):
        return self.distancia() >= p.distancia()

    def __eq__(self, p):
        ret = self.distancia() == p.distancia()
        return ret
    
    def __ne__(self, p):
        ret = self.distancia() != p.distancia()
        return ret

def main():
    """ Aplicacion principal """
    pMayor = None
    listaPuntos = []
    for nroPunto in range(1, 5):
        print(f"Ingrese los datos del punto {nroPunto} ")
        x = float(input ("x:"))
        y = float(input ("y:"))
        unPunto = Punto(x, y)
        listaPuntos.append(unPunto)
        
        if pMayor is None:
            pMayor = unPunto
        elif (unPunto > pMayor):
            pMayor = unPunto
            
    d = pMayor.distancia()
    x = pMayor.get_x()
    y = pMayor.get_y()
    print(f"La mayor distancia fue {d} (x={x}, y={y})")
    
    print(f"El punto más distante fue {pMayor}")
    
if(__name__ == "__main__"):
  main()