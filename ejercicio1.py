//#Clasificar a una persona segun su edad y nombre en python

edad = int(input("Digita la edad: "))
nombre = input("Digita su nombre: ")
group = 0

first_letter = nombre[0]
vocales = ['A','E','I','O','U']
validate = 0

for i in vocales:
  if nombre[0].capitalize() == i:
    validate = 1

if edad < 18 and validate == 1:
  group = 1
elif edad >= 18 and validate != 1:
  group = 2
else:
  group = 3

print("Su grupo es: ",group)
