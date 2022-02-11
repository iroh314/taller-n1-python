import math

# A. Imprimir el factorial de cualquier numero
def factorialNumero(numero):
    print (math.factorial(numero))
    
#factorialNumero(5)

# B. Mostrar los n primeros números de la serie de fibonnaci
def serieFibonacci(numero):
    
    x = 1
    y = 1
    z = 0
    if numero == 1:
        print(z)
    elif numero == 2:
        print(z , x)
    else:
        print(z)
        print(x)
        print(y)
        for i in range(numero - 3):
            faltantes = x + y
            y = x
            x = faltantes
            print(faltantes)

#serieFibonacci(6)

""" C. Retornar el valor de la cuota de un prestamo, teniendo en cuenta que se debe especificar 
el valor del prestamo, numero de cuotas, tasa mensual """
def valorCuota(valorPrestamo, numeroCuotas, tasaInteresM):

    valorCuotaF = ((valorPrestamo/numeroCuotas) * (tasaInteresM/100)) + (valorPrestamo/numeroCuotas)
    print(f"El valor de la cuota mensual es = ${round(valorCuotaF,2)}")

#valorCuota(10000,3,15)

# D. Mostrar los datos de cualquier Array
arrayPrueba = ["Manzanas", "Peras", "Uvas", "Mango"]

def mostrarArray():
    for i in arrayPrueba:
        print(i)

#mostrarArray()

# E. Mostrar los datos de cualquier diccionario
diccionarioPrueba = {
    "Marca" : "Ford",
    "Modelo" : "Mustang",
    "Año" : 1964
}

def mostrarDiccionario():
    for x, y in diccionarioPrueba.items():
        print(x, y)

#mostrarDiccionario()

""" F. Retornar el total de los pagos de diccionario dpagos = {
    "placa": "tis123",
    "marca": "aveo",
    "pagos": [100, 200, 30, 400]
}, enviado como parametro
"""
dpagos = {
    "placa": "tis123",
    "marca": "aveo",
    "pagos": [100, 200, 30, 400]
}

def mostrarPagos(pagos):
    print(pagos)

mostrarPagos(dpagos["pagos"])
