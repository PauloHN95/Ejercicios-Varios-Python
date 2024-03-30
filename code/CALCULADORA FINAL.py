#COSAS A MEJORAR: 
    #-CUANDO SE ELIJA LA OPERACION, QUE TE IMPRIMA QUE OPERACION VAS A REALIZAR.
    #-REDUCIR EL CODIGO, MEDIANTE ALGUNA FORMULA PARA COMPROBAR QUE SE METEN SOLO VALORES NUMERICOS EN n1 y n2.

# DEFINIMOS LAS FUNCIONES QUE VAMOS A USAR:
def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2): # TENEMOS QUE TENER CUIDADO CON DIVIDIR ENTRE 0.
    if n2 != 0:
        return n1 / n2
    else:
        return 'No podemos dividir entre 0, selecciona un valor numérico válido'

def calcular(): #DEFINIMOS LA FUNCION CALCULAR, CON TODAS LAS CONDICIONES.
    operacion = True # OTROGAMOS A OPERACION VALOR TRUE PARA INICIAR EL BUCLE

    while operacion:
        print(""" 
        Selecciona qué operación quieres hacer:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir del programa
        """)

        opcion = input().lower() # USAMOS .lower PARA TRANSFORMAR TODO A MINUSCULAS Y EVITAR ERRORES.

        if opcion == "1" or opcion == "suma":
            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n1 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n1 = float(input("Selecciona el primer número: "))
                    break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n1 no es numérico. Introduce un valor numérico.")

            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n2 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n2 = float(input("Selecciona el segundo número: "))
                    break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n2 no es numérico. Introduce un valor numérico.")

            resultado = sumar(n1, n2)
            print(f"El resultado es {resultado}")

        elif opcion == "2" or opcion == "resta":
            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n1 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n1 = float(input("Selecciona el primer número: "))
                    break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n1 no es numérico. Introduce un valor numérico.")

            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n2 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n2 = float(input("Selecciona el segundo número: "))
                    break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n2 no es numérico. Introduce un valor numérico.")

            resultado = restar(n1, n2)
            print(f"El resultado es {resultado}")

        elif opcion == "3" or opcion == "multiplicar":
            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n1 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n1 = float(input("Selecciona el primer número: "))
                    break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n1 no es numérico. Introduce un valor numérico.")

            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n2 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n2 = float(input("Selecciona el segundo número: "))
                    break  # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n2 no es numérico. Introduce un valor numérico.")

            resultado = multiplicar(n1, n2)
            print(f"El resultado es {resultado}")

        elif opcion == "4" or opcion == "dividir":
            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n1 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n1 = float(input("Selecciona el primer número: "))
                    break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n1 no es numérico. Introduce un valor numérico.")

            while True: # AQUI INICIAMOS EL BUCLE PARA COMPROBAR QUE SE CUMPLE QUE EN n2 SOLO PODAMOS METER VALORES NUMERICOS.
                try:
                    n2 = float(input("Selecciona el segundo número: "))
                    if n2 == 0:
                        print("Error: No se puede dividir por 0. Introduce un valor numérico distinto de 0.")
                    else:
                        break # SE FINALIZA EL BUCLE SI SE INTRODUCE UN VALOR NUMERICO.
                except ValueError:
                    print("Error: Valor para n2 no es numérico. Introduce un valor numérico.")

            resultado = dividir(n1, n2)
            print(f"El resultado es {resultado}")

        elif opcion == "5" or opcion == "salir":
            print("Estamos saliendo del programa. ¡Hasta pronto!")
            operacion = False

        else:
            print("""
            No se ha podido seleccionar la operación debido a un error en el dato introducido.
            Por favor, introduce un valor correcto para seleccionar el tipo de operación a realizar.
            """)

calcular()
