# Calculadora Simple (Sumar, restar, multiplicar y dividir)

# creamos una funcion para sumar
def sumar():
    try:
        primer_numero = operacion.split(" ")[0]
        segundo_numero = operacion.split(" ")[2]
        suma = int(primer_numero) + int(segundo_numero)
        print(f"Resultado: {suma}")
    except:
        print("ERROR")


# creamos una funcion para restar
def restar():
    try:
        primer_numero = operacion.split(" ")[0]
        segundo_numero = operacion.split(" ")[2]
        resta = int(primer_numero) - int(segundo_numero)
        print(f"Resultado: {resta}")
    except:
        print("ERROR")


# creamos una funcion para multiplicar
def multiplicar():
    try:
        primer_numero = operacion.split(" ")[0]
        segundo_numero = operacion.split(" ")[2]
        multiplicacion = int(primer_numero) * int(segundo_numero)
        print(f"Resultado: {multiplicacion}")
    except:
        print("ERROR")


# creamos una funcion para dividir
def dividir():
    try:
        primer_numero = operacion.split(" ")[0]
        segundo_numero = operacion.split(" ")[2]
        divicion = int(primer_numero) / int(segundo_numero)
        print(f"Resultado: {divicion}")
    except:
        print("ERROR")


# creamos una funcion para pedirle al usuario que ingrese la operacion
def numeros():
    while True:
        global operacion
        operacion = input("> ")
        if "+" in operacion:
            sumar()
        elif "-" in operacion:
            restar()
        elif "x" in operacion:
            multiplicar()
        elif "/" in operacion:
            dividir()
        else:
            print("Error, prueba con '+' , '-' , 'x', '/'")


numeros()