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

d) ....
A partir de estas ideas, modifique la aplicación original a fin de que el procesamiento se
realice utilizando los datos contenidos en el archivo de texto en vez de ser ingresados
por el usuario.
"""

def leeDatosArchivo():
    fp = open('datos.txt', 'r', encoding='utf8')
    listasEdades = []
    for linea in fp:
        lineaLimpia = linea.strip()
        datosCliente = lineaLimpia.split(";")
        if(len(datosCliente) == 2):
            dni = int(datosCliente[0].strip())
            edad = int(datosCliente[1].strip())
            listasEdades.append(edad)
            print(f"DNI: {dni} Edad: {edad}")
    fp.close()
    return listasEdades


def clientePotencial(edad):
    if edad >= 35 and edad <= 45:
        return True
    else:
        return False



def cantEncimaPromedio(listasEdades, prom):
    cantidadProm = 0
    for x in range((len(listasEdades))):
        print(x)
        if listasEdades[x] > prom:
            cantidadProm+=1
    return cantidadProm

def main():
     listasEdades = []
     cantidadTotal = 0
     cantidadTotalCriterio = 0
     porcClientesPotenciales = 0
     listasEdades = leeDatosArchivo()    
     cantidadTotal = len(listasEdades)
     sumaTotal = sum(listasEdades)     
     if cantidadTotal > 0:
              promedio = sumaTotal / cantidadTotal   
              cantidadEncimaProm = cantEncimaPromedio(listasEdades, promedio)
              print("Promedio " + str(promedio) + " cantidadEncimaProm " + str(cantidadEncimaProm))
              porcentaje_potenciales = (cantidadTotalCriterio / cantidadTotal) * 100              
              print(f"Porcentaje de clientes potenciales: {porcentaje_potenciales:.2f}%")
              if cantidadEncimaProm > 0:
                  porcentaje_potencialesEncProm = (cantidadTotal / cantidadEncimaProm) * 100
                  print(f"Porcentaje de clientes potenciales encima del promedio: {porcentaje_potencialesEncProm:.2f}%")
              else:
                  print("No se ingresaron clientes potenciales válidos.")
     else:
              print("No se ingresaron clientes válidos.")
             
if (__name__ == "__main__"):
    main()
