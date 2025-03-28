# -*- coding: utf-8 -*-
"""
La compañía de seguros de la guía de ejercicios N° 1, a avanzado en la implementación de 
su nuevo producto de seguros de vida, requiriendo un modelo que le permita representar a 
los productores de seguros y los clientes de cada tipo de seguro.  
El objetivo es poder consultar información que tienen disponible para cada uno de los 
promotores en archivos de texto.   
a) Implemente un modelo que represente personas, promotores y clientes 
considerando que: - - - 
persona: representa una persona en el modelo a partir de su nombre (atributo 
_nom de tipo cadena de caracteres) y DNI (atributo _dni de tipo numérico 
entero).  
Permite la carga de los valores de interés a través del constructor e incorpora 
métodos para acceder a estos valores (getDNI y getNombre).  
También implementa métodos que permiten establecer relación de orden entre 
dos objetos de esta clase a partir de su número de documento (__lt__, __le__, 
__gt__, __ge__, __eq__, __ne__) y genera una representación de cadena de 
caracteres (método __str__) utilizando el número de documento con 8 
posiciones y el nombre separado uno del otro utilizando el carácter pipe “|” (por 
ejemplo “ 8765123 | Juan Pérez”). 
promotor: clase derivada de la clase persona, representa un promotor de 
seguros. Agrega una lista de objetos de la clase cliente descrita más abajo 
(atributo _clientes), esta lista contiene todos los objetos que representan los 
clientes de un promotor de seguros particular.  Además del constructor, que 
crea una lista de clientes vacía, incorpora los siguientes métodos: 
o addCliente: agrega un objeto cliente dado como argumento a la lista 
utilizando el método append.  
o getCntClientes: retorna la cantidad de clientes almacenados en la lista 
de clientes. Este valor es determinado utilizando la función len y la lista 
de clientes como argumento. 
o getClientes: retorna la lista de clientes a fin de poder iterar sobre ella 
(atributo _clientes).  
o __str__: sobre escribe el método definido en la clase base a fin de 
retornar solo el nombre completo del promotor. 
cliente: clase derivada de la clase persona que incorpora como atributo el 
promotor con el que se relaciona y el tipo de seguro. El promotor es un objeto 
de la clase promotor, mientras que el tipo de seguro está dado como una 
cadena de caracteres que puede ser “Seguro de Vida” o “Seguro Automotor 
(AA 000 AA)” donde AA 000 AA corresponde con la patente del automotor 
asegurado.  
El objeto de la clase promotor puede ser (y será en esta actividad) compartido 
por múltiples objetos de la clase cliente, mientras que el promotor contendrá 
una lista de objetos de la clase cliente. De este modo se representa el hecho 
que un cliente tiene un promotor y un promotor tiene múltiples clientes. La clase 
cliente deberá incorporar un método getPromotor que retornará el objeto 
promotor. De este modo a partir de un objeto cliente es posible acceder a los 
datos de su promotor de seguros.  
En lo que respecta al tipo de seguro sucede algo similar, un mismo cliente 
puede tener contratados diferentes tipos de seguros, por lo que el tipo de 
seguro en la clase cliente es representado a través de una lista de cadenas de 
caracteres.  
Debido a que a través del constructor se indica un tipo de seguro (forzando a 
que todos los clientes tienen por lo menos un seguro contratado), los demás 
seguros que se contraten se agregan a través del método addTipoSeguro. 
Este método recibe como argumento una cadena de caracteres y la agrega a 
la lista de seguros utilizando el método append.   
Finalmente, la clase cliente incorpora el método getSeguros que retorna la 
lista de cadenas de caracteres con los seguros contratados por un cliente 
particular.  
Utilice el modelo anterior en una aplicación como la que se muestra a continuación a 
fin de comprobar que el modelo funciona correctamente:  

"""
class Persona:
    def __init__(self, nom, dni):
       self._nom = nom 
       self._dni = dni
       
    def getDNI(self):
        return self._dni
    
    def getNombre(self):
        return self._nom
    
    def __lt__(self, per):
        return self._dni < per._dni()
        
    def __le__(self, per):
        return self._dni <= per._dni()
    
    def __gt__(self, per):
        return self._dni > per._dni()
    
    def __ge__(self, per):
        return self._dni >= per._dni()
    
    def __eq__(self, per):
        return self._dni == per._dni()
    
    def __ne__(self, per):
        return self._dni != per._dni()
    
    def __str__(self):
        return f"({self._dni:8} | {self._nom})"
        
class Promotor(Persona):
    def __init__(self, nom, dni):
        super().__init__(nom, dni)
        self._clientes = []
    
    def addCliente(self, cli):
        self._clientes.append(cli)

    def getCntClientes(self):
        return len(self._clientes)
    
    def getClientes(self):
        return self._clientes
    
    def __str__(self):
        return f"({self._nom})"
        
    
class Cliente(Persona):
    def __init__(self, nom, dni, prom, tipoSeguro):
        super().__init__(nom, dni ) 
        self._prom = prom
        self._tipoSeguro = []
        self._tipoSeguro.append(tipoSeguro)  

    def addTipoSeguro (self, tipoSeguro):
        self._tipoSeguro.append(tipoSeguro)
        
    def getSeguros(self):
        return self._tipoSeguro
    
    def getPromotor(self):
        return self._prom
    
def cargaClientes(prom):
    file = open('clientes.txt', 'r', encoding='utf8')  
    for linea in file: 
        #linea = file.readline()
        lineaLimpia = linea.strip() 
        datosCliente = lineaLimpia.split(";")
        if len(datosCliente)==3:
            dni = datosCliente[0].strip()        
            nom = datosCliente[1].strip() 
            segs = datosCliente[2].strip().split('|')
           
            if len(segs)==1:
                cli = Cliente(dni,nom,prom,segs[0].strip())
            elif len(segs)>1:
                i=0
                for x in segs:         
                    if i==0:
                        cli = Cliente(dni,nom,prom,x.strip())
                    else:    
                        cli.addTipoSeguro(x.strip())
                    i+=1
            prom.addCliente(cli)
    # Close the file when you're done
    file.close()
    
    
def main(): 
    # Creamos el promotor 
    prom = Promotor(24317128, "Diego de la Vega") 
    # Creamos un cliente, vinculándolo al promotor 
    cargaClientes(prom)
    # Mostramos los datos del promotor 
    print(f"Promotor: {prom}") 
    # Y el listado de sus clientes 
    print("Listado de clientes:") 
    for cli in prom.getClientes(): 
        print(f"{cli}") 
        print("Productos contratados:") 
        for s in cli.getSeguros(): 
            print(f"\t {s}")

if __name__ == "__main__":
    main()
