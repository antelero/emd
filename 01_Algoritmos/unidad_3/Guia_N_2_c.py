# -*- coding: utf-8 -*-
"""
c) Agregue los métodos ordenarClientes y buscarCliente a la clase promotor de 
modo que el ordenamiento se realice sobre todos los clientes según su DNI 
utilizando alguno de los algoritmos tratados en esta semana. Note que, debido a 
que la clase persona incorpora métodos para comparar objetos de su tipo según 
el DNI es posible comparar objetos clientes de modo directo y la relación de orden 
estará dada por su número de DNI. Se recomienda utilizar una implementación del 
método quick sort, pero no es obligatorio que elija este método (fundamente su 
elección). En lo que respecta al algoritmo de búsqueda, implemente el método de 
búsqueda por bisección (o búsqueda binaria), a fin de que sea posible buscar un 
Página 3 / 4 
cliente a partir de su DNI, retornando el objeto de la clase cliente o None si no 
existe un cliente con el número de DNI indicado. 
Modifique la aplicación a fin de que permita ver los datos del promotor y el listado 
de todos los DNI y nombres de sus clientes. Luego permita ingresar números de 
DNI, busque este valor sobre la lista de clientes ordenada utilizando los métodos 
implementados. Si se encuentra coincidencia con el DNI de un cliente deberá 
presentar sus datos por pantalla, así como los seguros que contrató. En caso de 
no encontrar un cliente con el DNI indicado se deberá mostrar un mensaje alusivo.  
La aplicación debe repetir el proceso de ingreso de DNI y búsqueda hasta que el 
valor ingresado sea cero o negativo.  

"""
class Persona:
    def __init__(self, dni, nom):
       self._nom = nom 
       self._dni = int(dni)  # Convertir a entero
       
    def getDNI(self):
        return self._dni
    
    def getNombre(self):
        return self._nom
    
    def __lt__(self, per):
        return self._dni < per._dni
        
    def __le__(self, per):
        return self._dni <= per._dni
    
    def __gt__(self, per):
        return self._dni > per._dni
    
    def __ge__(self, per):
        return self._dni >= per._dni
    
    def __eq__(self, per):
        return self._dni == per._dni
    
    def __ne__(self, per):
        return self._dni != per._dni
    
    def __str__(self):
        return f"({self._dni:8} | {self._nom})"
        
class Promotor(Persona):
    def __init__(self, dni, nom):
        super().__init__( dni, nom)
        self._clientes = []
    
    def addCliente(self, cli):
        self._clientes.append(cli)

    def getCntClientes(self):
        return len(self._clientes)
    
    def getClientes(self):
        return self._clientes
    
    def __str__(self):
        return f"(Promotor: {self._nom})"
    
    def buscarCliente(self, dni):
        self.ordenarClientes()
        inicio, fin = 0, len(self._clientes) - 1

        while inicio <= fin:
           medio = (inicio + fin) // 2
           if self._clientes[medio]._dni == dni:
               return self._clientes[medio]
           elif self._clientes[medio]._dni < dni:
               inicio = medio + 1
           else:
               fin = medio - 1
        return None

        
   # Método para ordenar con Quick Sort
    def ordenarClientes(self):
        def _ordenar_quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivote = arr[-1]
            menores = [x for x in arr[:-1] 
                               if x < pivote]
            mayores = [x for x in arr[:-1] 
                               if x >= pivote]
            return _ordenar_quickSort(menores) + [pivote] + _ordenar_quickSort(mayores)
        self._clientes = _ordenar_quickSort(self._clientes)
        

        
        
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
    
def cargaArchivoClientes(prom):
    file = open('clientes.txt', 'r', encoding='utf8')  
    for linea in file: 
        #linea = file.readline()
        lineaLimpia = linea.strip() 
        datosCliente = lineaLimpia.split(";")
        if(len(datosCliente) == 3): 
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
    cargaArchivoClientes(prom)
    # Mostramos los datos del promotor 
    print(f"Promotor: {prom}") 
    # Y el listado de sus clientes 
    print("Listado de clientes:") 
    prom.ordenarClientes()
    for cli in prom.getClientes(): 
        print(f"{cli}") 
        print("Productos contratados:") 
        for s in cli.getSeguros(): 
            print(f"\t {s}")
    # Búsqueda
    dni_buscar = 27654987
    cliente_encontrado = prom.buscarCliente(dni_buscar)
    if cliente_encontrado:
        print(f"\nCliente encontrado: {cliente_encontrado}")
    else:
        print("\nCliente no encontrado")
if __name__ == "__main__":
    main()
