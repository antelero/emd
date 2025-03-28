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

c) A fin de separar de un modo más claro el criterio de selección de los clientes potenciales
respecto del algoritmo de procesamiento, implemente una función que, considerando la edad
de un cliente, retorne verdadero o falso a fin de indicar si se trata o no de un posible cliente.
Modifique la aplicación del punto anterior a fin de utilizar esta función.

"""

def clientePotencial(edad):
    if edad >= 35 and edad <= 45:
        return True
    else:
        return False

def main():
     cantidadTotal = 0
     cantidadTotalCriterio = 0
     porcClientesPotenciales = 0
     edadStr = input("Ingrese la primer edad: ")
     edadInt = int(edadStr)
     while (edadInt > 0):
         #
         # Agregue aquí el procesamiento a realizar
         #
         cantidadTotal = cantidadTotal + 1
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
     if cantidadTotal > 0:
              porcentaje_potenciales = (cantidadTotalCriterio / cantidadTotal) * 100
              print(f"Porcentaje de clientes potenciales: {porcentaje_potenciales:.2f}%")
     else:
              print("No se ingresaron clientes válidos.")
             
if (__name__ == "__main__"):
    main()
