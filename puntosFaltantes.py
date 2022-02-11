# 3. Crear un diccionario con variables
w = True
x = 5
y = "Juan"

diccionario = {
    w : w,
    x : x,
    y : y
}

z = diccionario.values()

#print(z)

# 4. Crear una lista con los números del 1 al 50
lista = [i for i in range(1,50+1)]
#print(lista)


# 5. Crear una lista con los números impares de la lista generada en el numeral 4

# 6. Crear un diccionario con los datos de un vehiculo (placa, marca, modelo, valor)
diccionarioVehiculo = {
    "placa": "ABC123",
    "marca": "Ford",
    "modelo": "Mustang",
    "valor" : 80000000
}

# 7. Listar los datos del diccionario generado en el punto 6
datosSalida = diccionarioVehiculo.items()
#print(datosSalida)

# 8. Crear una lista, con datos por teclado, que contenga las ciudades turisticas de Colombia
listaCiudades = []

ciudad = str(input("Ingrese una ciudad turistica (Para terminar programa presione N) = "))

while ciudad != "N":
    listaCiudades.append(ciudad)
    ciudad = str(input("Ingrese una ciudad turistica (Para terminar programa presione N) = "))

# 9. Listar las ciudades turisticas de Colombia, con base en la lista del numeral 8, en forma ordenada
listaCiudades.sort()
#print(listaCiudades)

# 10. Agregar una ciudad turistica a la lista de ciudades turisticas
listaCiudades.append("Cartagena")
listaCiudades.sort()
#print(listaCiudades)

# 11. Ingresar el nombre de una ciudad y borrarla de la lista ciudades turisticas
listaCiudades.append("Manizales")
listaCiudades.sort()
#print(listaCiudades)

listaCiudades.remove("Manizales")
#print(listaCiudades)

# 12. Crear una clase con los datos de un vehiculo(placa, marca, modelo, precio).Los atributos son privados
class vehiculo:

   def __init__(self, placa, marca, modelo, precio):
       self._placa = placa
       self._marca = marca
       self._modelo = modelo
       self._precio = precio
   

# 13. Instanciar un objeto de la clase vehiculo
vehiculo1 = vehiculo("ABC123", "Mazda", "R7", 75000000)
print(vehiculo1._placa)
print(vehiculo1._marca)
print(vehiculo1._modelo)
print(vehiculo1._precio)