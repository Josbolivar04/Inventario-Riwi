print("-----------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------")

print("Bienvenido al Inventario")

print("-----------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------")



nombre=str(input("Ingrese al nombre del producto ")) #Pedir el nombre del producto

#Validar que no se acepten precios menores a 0
while True:
    try:
        precio=float(input(f"Ingrese el precio de {nombre}: ")) #Pedir el precio del producto
        if precio < 0:
            print("No se aceptan valores negativos")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número entero")

#Validar las cantidades
while True:
    try:
        cantidad=int(input(f"Ingrese el número en stock de {nombre}: ")) #Pedir la cantidad del producto
        if cantidad < 0:
            print("No se aceptan valores negativos")
        else:
            break
    except ValueError:
        print("Error: debe ingresar un número entero")

#Multiplicacion para hallar el costo total
costo_total=float(precio*cantidad)

#Resumen final del inventario
print("\n------Resumen del Inventario------") 
print("Nombre del producto: ",nombre)
print("Precio del producto: ",precio)
print(f"Cantidad de {nombre}: ",cantidad)
print(f"Costo total del inventario de {nombre}: ",costo_total)


#Este programa basico permite crear un inventario el cual creamos a nuestra disposicion y su funcionalidad esta distinguida en su practicidad y sencillez.