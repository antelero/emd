# -*- coding: utf-8 -*-
"""
 algoritmo que determine el valor a pagar cuando al 
 total de la factura se le aplica un 20 % de descuento, 
 presentando en la pantalla el importe bruto (previo al descuento), 
 el monto del descuento y el importe final a pagar.
"""
print("Ingrese los Valores, a medida que se le vaya solicitando")
importeFactura = float(input("Importe Factura: "))
importeBruto = importeFactura 
descuento = importeFactura * 20 / 100
valorAPagar = importeFactura - descuento


print(f"Importe Bruto: {importeBruto}")
print(f"Descuento: {descuento}")
print(f"Valor a Pagar: {valorAPagar}")