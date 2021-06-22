"""
Creado por: Jonathan Osorio Sepulveda
Fecha: 
"""

import math

lista_lacteos = []
lista_aseo = []
lista_granos = []
inventario_lacteos = []
inventario_aseo = []
inventario_granos = []

def ingreso_productos ():
  
  nuevo = 1
  #nuevo = int(input("digite 1 para nuevo producto o 2 para mostrar inventario: "))
  if nuevo == 1:
    producto = input("ingrese el nombre del producto: ")
    cantidad = int(input("ingrese la cantidad del producto: "))
    categoria = input("ingrese la categoria del producto: (Lacteos, Aseo o Granos)")
    if categoria == "Lacteos":
      validacion = 0
      for posicion in  range(0, len(lista_lacteos)):
        if producto == lista_lacteos[posicion]:
          
          cantidad = cantidad + inventario_lacteos[posicion]
          
          inventario_lacteos[posicion] = cantidad

          validacion = 1
      if validacion == 0:
        lista_lacteos.append(producto)
        inventario_lacteos.append(cantidad)
    
    if categoria == "Aseo":
      validacion = 0
      for i in range(0, len(inventario_aseo)):
        if producto == lista_aseo[i]:
          cantidad = cantidad + inventario_aseo[i]
          inventario_aseo[i] = cantidad
          validacion = 1
      if validacion == 0: 
        lista_aseo.append(producto)
        inventario_aseo.append(cantidad)
    
    if categoria == "Granos":
      validacion = 0
      for pos in range(0, len(inventario_granos)):
        if producto == lista_granos[pos]:
          cantidad = cantidad + inventario_granos[pos]
          inventario_granos[pos] = cantidad
          validacion = 1
      if validacion == 0:
        lista_granos.append(producto)
        inventario_granos.append(cantidad)
    
""""
  elif nuevo == 2:
      print ("Lacteos")
      print (lista_lacteos) 
      print(inventario_lacteos)
      print ("Aseo")
      print (lista_aseo)
      print (inventario_aseo)
      print ("Granos")
      print (lista_granos)
      print (inventario_granos)
  else:
    print("ingrese un valor valido")
   
  """



modificar = 1
while modificar == 1:
  ingreso_productos ()
  modificar = int(input("digite 1 para ingresar producto al inventario o 2 para imprimir el inventario: "))


print ("Lacteos")
print (lista_lacteos) 
print(inventario_lacteos)
print ("Aseo")
print (lista_aseo)
print (inventario_aseo)
print ("Granos")
print (lista_granos)
print (inventario_granos)