#No lleva main y no hay ;
print("Hola mundo!")
#Declaraciones de variable de tipo inferido
miNumero = 5
miNumero = 7.5
#Variables que cambian de tipo de dato
miNumero = "Siete punto cinco"
#MiNumero = "Ocho"
print('Mi número: ' + str(miNumero))

a = 16
b = 80
#condiciones
if a > b:
    print("A es mayor que B")
    print("Sigo estando en el bloque del if")
else:
    print("A no es mayor que B")
    
print("Aquí ya estoy fuera del if")

#ciclos
frutas = ["Manzana", "Sandía", "Melón", "Mango"]
for fruta in frutas:
    print("Fruta: " + fruta)

#funciones
def mi_funcion():
    print("Estoy dentro de la funcion mi_funcion")
    
#funciones con parámetros
def saludar(nombre, apellidos):
    print("Hola " + nombre + " " + apellidos)

mi_funcion()
saludar("Emiliano","Lopez Noriega")