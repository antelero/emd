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

d) Se propone incorporar otro indicador al procesamiento realizado, el promedio de edades
considerado y cuantas edades del conjunto se encuentran por encima del promedio. Para
esto realice las modificaciones requeridas a fin de que se almacenen las edades según se
ingresan en una lista.
Puede determinar el promedio utilizando las funciones sum y len e indicando como
argumento la lista de edades.
Luego implemente una función que, tomando como argumento la lista de edades y su
promedio, retorne la cantidad por encima del promedio.
"""

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
     edadStr = input("Ingrese la primer edad: ")
     edadInt = int(edadStr)
     while (edadInt > 0):
         #
         # Agregue aquí el procesamiento a realizar
         #
         listasEdades.append(edadInt)
         
         edadStr = input("Siguiente: ")
         #if edadStr == '':
         #    break
         
         edadInt = int(edadStr)
         if clientePotencial(edadInt):
             cantidadTotalCriterio = cantidadTotalCriterio + 1
          
         #
         # Realice las operaciones requeridas
         # y presente los resultados correspondientes
         #
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
