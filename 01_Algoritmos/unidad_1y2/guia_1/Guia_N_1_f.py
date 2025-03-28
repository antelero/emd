"""
Una compañía dedicada a la venta de seguros para automotores ha incorporado a su oferta
un nuevo producto: seguros de vida. Ya que se cuenta con una cartera de clientes inicial se
pretende identificar los clientes potenciales para este nuevo producto.
En principio el procesamiento se realizará de forma manual, sobre pequeñas muestras datos
de diferentes promotores de seguros, por lo que la cantidad a procesar no es conocida y se
propone ingresar datos mientras el valor de la edad sea válido (mayor a cero).
Se debe determinar el porcentaje de clientes potenciales (cantidad de clientes con un criterio
particular dividido la cantidad total de clientes considerados multiplicado por 100). El primer
criterio que se utilizará para considerar un cliente como potencial es su edad, debido estar en
el rango entre 35 y 45 años (ambos valores inclusive). 

f) ....
Utilizando estas ideas, modifique la aplicación anterior de modo que, al comienzo, se
cree y cargue el diccionario con los datos de los clientes. Luego, se procesen los datos
del archivo que contiene las edades y, por cada cliente potencial, se muestre su nombre
utilizando el diccionario creado. 
"""

def leeDatosArchivo():
    fp = open('datos.txt', 'r', encoding='utf8')
    listasEdades = []
    listasDni = []
    for linea in fp:
        lineaLimpia = linea.strip()
        datosCliente = lineaLimpia.split(";")
        if(len(datosCliente) == 2):
            dni = int(datosCliente[0].strip())
            edad = int(datosCliente[1].strip())
            listasEdades.append(edad)
            listasDni.append(dni)
            print(f"DNI: {dni} Edad: {edad}")
    fp.close()
    return listasEdades, listasDni

def leeNombresArchivo():
    dicNombres = {}
    fp = open('nombres.txt', 'r', encoding='utf8')
    for linea in fp:
        lineaLimpia = linea.strip()
        datosCliente = lineaLimpia.split(";")
        if(len(datosCliente) == 2):
            dni = int(datosCliente[0].strip())
            nombre = datosCliente[1].strip()
            dicNombres.update({dni: nombre})
    fp.close()
    for vDni in dicNombres.keys():
        nom = dicNombres[vDni]
        print(f"DNI: {vDni} - Nombre: {nom}")
    return dicNombres
 
def clientePotencial(edad):
    if edad >= 35 and edad <= 45:
        return True
    else:
        return False



def cantEncimaPromedio(listasEdades, prom):
    cantidadProm = 0
    for x in range((len(listasEdades))):
        if listasEdades[x] > prom:
            cantidadProm+=1
    return cantidadProm

def getPotencialesContactos(listasEdades, listasDni, dicNombres, prom):
    cantidadProm = 0
    for x in range((len(listasEdades))):
        if listasEdades[x] > prom:
            print(f"Edad: {listasEdades[x]} - DNI: {listasDni[x]} - Nombre: {dicNombres.get(listasDni[x])}")

def main():
     listasEdades = []
     listasDni = []
     dicNombres = {}
     cantidadTotal = 0
     cantidadTotalCriterio = 0
     porcClientesPotenciales = 0
     #Leo archivo de datos
     listasEdades, listasDni = leeDatosArchivo()    
     #Leo archivo de nombres
     dicNombres = leeNombresArchivo()
     cantidadTotal = len(listasEdades)
     sumaTotal = sum(listasEdades)     
     if cantidadTotal > 0:
              promedio = sumaTotal / cantidadTotal   
              cantidadEncimaProm = cantEncimaPromedio(listasEdades, promedio)
              print("Promedio " + str(promedio) + " cantidadEncimaProm " + str(cantidadEncimaProm))
              porcentaje_potenciales = (cantidadTotalCriterio / cantidadTotal) * 100              
              print(f"Porcentaje de clientes potenciales: {porcentaje_potenciales:.2f}%")
              if cantidadEncimaProm > 0:
                  #Llamo a la funcion para que me devuelva los datos de los potenciales clientes
                  getPotencialesContactos(listasEdades, listasDni, dicNombres, promedio)
                  porcentaje_potencialesEncProm = (cantidadTotal / cantidadEncimaProm) * 100
                  print(f"Porcentaje de clientes potenciales encima del promedio: {porcentaje_potencialesEncProm:.2f}%")
              else:
                  print("No se ingresaron clientes potenciales válidos.")
     else:
              print("No se ingresaron clientes válidos.")
             
if (__name__ == "__main__"):
    main()
