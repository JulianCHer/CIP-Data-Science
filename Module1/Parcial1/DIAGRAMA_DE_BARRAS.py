# -*- coding: utf-8 -*-
"""parcial1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SuSgaDulaQNeoz1TVyfL_-KAmndg12kF
"""

import matplotlib.pyplot as plt

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# Creamos el gráfico
# para dar color a las barras usamos color='nombre del color'
# para el color del borde edgecolor='color del borde'
# para definir grosor del borde usamos linewidth
# para el grosor de las barras usamos width que por defecto viene como 0.8
plt.bar(categorias, valores, color='RED', edgecolor='black', linewidth=1.5, width=0.6)

# Personalizamos
# para dar titulo usamos TITLE
# para dar nombre al eje X usamos plt.xlabel
# para dar nombre al eje Y usamos plt.ylabel
# para ajustar el tamaño de la letra usamos fontsize='TAMAÑO DE LA LETRA'
plt.title("Diagrama de Barras Personalizado TITULO", fontsize=16)
plt.xlabel("Categorías SUBTITULO EJEMPLOS", fontsize=12)
plt.ylabel("Valores SUBTITULO EJEMPLO", fontsize=12)

# para crear las cuadriculas para una mejor guia usamos el siguiente comando
plt.grid(axis='y', linestyle='--', alpha=1)

# para mostrar nuestra grafica usamos .show()
plt.show()

import matplotlib.pyplot as plt
# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# podemos personalizar los titulos
# para el titulo principal usamos .title("nombre de el titulo")
# para el titulo de los ejes usamos plt.xlabel para eje X -- plt.ylabel para el eje Y
plt.title("Título del Diagrama EJEMPLO TITULO PRINCIPAL")
plt.xlabel("Categorías EJEMPLO TITULO EJE X")
plt.ylabel("Valores EJEMPLO TITULO EJE Y")


# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# podemos personalizar los titulos
# para el titulo principal usamos .title("nombre de el titulo")
# para el titulo de los ejes usamos plt.xlabel para eje X -- plt.ylabel para el eje Y
plt.title("Título del Diagrama EJEMPLO TITULO PRINCIPAL")
plt.xlabel("Categorías EJEMPLO TITULO EJE X")
plt.ylabel("Valores EJEMPLO TITULO EJE Y")

# PARA AÑADIRLE COLOR A LAS BARRSA USAMOS color ='color que queremos que salgan las barras'
plt.bar(categorias, valores, color='red')


# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# podemos personalizar los titulos
# para el titulo principal usamos .title("nombre de el titulo")
# para el titulo de los ejes usamos plt.xlabel para eje X -- plt.ylabel para el eje Y
plt.title("Título del Diagrama EJEMPLO TITULO PRINCIPAL")
plt.xlabel("Categorías EJEMPLO TITULO EJE X")
plt.ylabel("Valores EJEMPLO TITULO EJE Y")

# PARA AÑADIRLE COLOR A LAS BARRSA USAMOS color ='color que queremos que salgan las barras'
# para poner borde usamos edgecolor = "color del borde"
# para definir el tamaño de el borde usamos linewidth
plt.bar(categorias, valores, color='orange', edgecolor='black', linewidth=1.5)


# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# podemos personalizar los titulos
# para el titulo principal usamos .title("nombre de el titulo")
# para el titulo de los ejes usamos plt.xlabel para eje X -- plt.ylabel para el eje Y
plt.title("Título del Diagrama EJEMPLO TITULO PRINCIPAL")
plt.xlabel("Categorías EJEMPLO TITULO EJE X")
plt.ylabel("Valores EJEMPLO TITULO EJE Y")

# PARA AÑADIRLE COLOR A LAS BARRSA USAMOS color ='color que queremos que salgan las barras'
# para poner borde usamos edgecolor = "color del borde"
# para definir el tamaño de el borde usamos linewidth
# para definir el ancho de las barras usamos width, por defecto el ancho de las barras viene en 0.8
plt.bar(categorias, valores, color='orange', edgecolor='black', linewidth=1.5, width=0.9)





# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# podemos personalizar los titulos
# para el titulo principal usamos .title("nombre de el titulo")
# para el titulo de los ejes usamos plt.xlabel para eje X -- plt.ylabel para el eje Y
# podemos usar fontsize para modificar el tamaño de las letras
plt.title("Mi Diagrama de Barras TITULO PRINCIPAL", fontsize=20)
plt.xlabel("Categorías TITULO EJE X", fontsize=15)
plt.ylabel("Valores TITULO EJE Y", fontsize=17)

# PARA AÑADIRLE COLOR A LAS BARRSA USAMOS color ='color que queremos que salgan las barras'
# para poner borde usamos edgecolor = "color del borde"
# para definir el tamaño de el borde usamos linewidth
# para definir el ancho de las barras usamos width, por defecto el ancho de las barras viene en 0.8
plt.bar(categorias, valores, color='orange', edgecolor='black', linewidth=1.5, width=0.9)





# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()

# definimos los datos, categorias = X y valores = Y
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 20]

# usamos plt bar para crear el grafico
plt.bar(categorias, valores)

# podemos personalizar los titulos
# para el titulo principal usamos .title("nombre de el titulo")
# para el titulo de los ejes usamos plt.xlabel para eje X -- plt.ylabel para el eje Y
# podemos usar fontsize para modificar el tamaño de las letras
plt.title("Mi Diagrama de Barras TITULO PRINCIPAL", fontsize=20)
plt.xlabel("Categorías TITULO EJE X", fontsize=15)
plt.ylabel("Valores TITULO EJE Y", fontsize=17)

# PARA AÑADIRLE COLOR A LAS BARRSA USAMOS color ='color que queremos que salgan las barras'
# para poner borde usamos edgecolor = "color del borde"
# para definir el tamaño de el borde usamos linewidth
# para definir el ancho de las barras usamos width, por defecto el ancho de las barras viene en 0.8
plt.bar(categorias, valores, color='orange', edgecolor='black', linewidth=1.5, width=0.9)

# para poder crear la cuadricula usamos:
plt.grid(axis='y', linestyle='--', alpha=0.7)


# Personalizamos
# para mostrar nuestra grafica usamos .show()
plt.show()