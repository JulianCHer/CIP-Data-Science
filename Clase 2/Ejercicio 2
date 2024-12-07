#Clasificar una persona segun su país y la longitud del nombre

nombre = input("Digita tu nombre: ")
pais = input("Digita su pais: ")
group = ""

count_letters = len(nombre)
Pais = pais.capitalize()
if Pais == 'Colombia' and count_letters < 5:
  group = f"{Pais} A"
elif Pais == 'Mexico' and count_letters >= 5:
  group = f"{Pais} B"
else:
  group = "Otros"

print(f" Su grupo es: {group}")
