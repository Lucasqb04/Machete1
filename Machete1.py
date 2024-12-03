# LOGICA DE PROGRAMACION #

# En python tenemos lo que son variables que cada variable debe tener su valor por ejemplo: 
 
variableuno = "Lucas"
variabledos = 2  
variabletres = 1.5 
variablecuatro = "el cielo es rojo"

## Las variables representadas anteriormente tambien tienen una clasificacion
print(type(variableuno))  # esta variable es de tipo str -> (Textos)
print(type(variabledos))  # esta variable es de tipo int -> (Entero)   
print(type(variabletres))  # esta variable es de tipo float -> (numeros flotantes)
print(type(variablecuatro)) # esta variable es de tipo bool -> (Con respuesta True/False)

#OPERADORES
# Operadores aritmeticos 
print(f"Suma {3 + 4 = }") # La suma se representa con +
print(f"Resta { 4 - 3 = }") # La resta se representa con - 
print(f"Multiplicacion { 4 * 4 = }") # La multiplicacion se representa con * 
print(f"Division { 8 / 2 = }") # La division se representa con /
print(f"Modulo { 10 % 3 = }") # El modulo se representa con %
print(f"Exponente { 10 ** 3 = }") # El exponente se representa con **

#Operadores de comparación 
print (f"Igualdad { 3 == 3 }") # Para realizar igualdades se escribe == y da como resultado true/false
print (f"Desigualdad { 3 != 4 }") # Para realizar desigualdad se escribe != y da como resultado true/false 
print (f"mayor que { 4 > 3 }") # Mayor que se representa con >
print (f" menor que { 3 < 4 }") # Menor que se representa con < 
print (f"mayor o igual que { 1 >= 2 }") # Mayor o igual que se representa con >=
print (f"menor o igual que { 2 <= 3 }") # Menor o igual que se representa con <=

# Operadores de asignación 
"""
Este operador es especialmente para calcularle a otra variable por ejemplo
"""
variablesol = 11

print(variablesol)

variablesol =+ 1

print(variablesol)

# Estructuras de control 

#Condicionales -> If, elif y else

variable_azul = "marron"
if variable_azul == "Rojo":
    print ("variable_azul es Roja")
elif variable_azul == "Verde":
    print ("variable_azul es verde")
else: 
    print("variable_azul no es ni verde ni roja")

# Iterativas -> for, while 

for i in range (10):   # Se utiliza para iterar sobre una secuencia (como listas, tuplas, cadenas, rangos, etc.)
    print (i)

i = 0 
while i <= 10:  #Se utiliza para repetir un bloque de código mientras una condición sea verdadera. Es más adecuado cuando no sabes exactamente cuántas iteraciones se necesitan, pero tienes una condición que las controla.Se utiliza para repetir un bloque de código mientras una condición sea verdadera. Es más adecuado cuando no sabes exactamente cuántas iteraciones se necesitan, pero tienes una condición que las controla.
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)    # De a cuerdo a los datos que se pongan aqui es como se ejecutara el except y el finally
except:
    print("Se ha producido un error")
finally:
    print("Se ha finalizado el programa")


# 