# -*- coding: utf-8 -*-
"""diagrama de dispersion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WVSjz_fw9HE5oVssgEZRrlFfjDzylIO0

Diagramas de dispersion o puntos (Matplotlib)

Un diagrama de dispersión es un gráfico que muestra puntos en un plano cartesiano, donde cada punto representa una observación con dos variables (por ejemplo, X e Y). Es ideal para visualizar relaciones o patrones entre dos variables.

quiere decir Un diagrama de dispersión es como un juego de unir puntos en un gráfico. Imagina que tienes una hoja de papel con una línea horizontal (eje X) y una línea vertical (eje Y). Cada punto en el gráfico representa dos cosas: una posición en el eje X y una en el eje Y.

***PASO A PASO ***

Paso 1: Importar las siguientes bibliotecas

import matplotlib.pyplot as plt           # Para gráficos

import numpy as np                        # Para trabajar con datos numéricos

Paso 2: Crear el primer grafico de dispersion
"""

# Coordenadas de los puntos
x = [1, 2, 3, 4, 5]  # Valores del eje X
y = [2, 3, 5, 7, 11]  # Valores del eje Y

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Añadir etiquetas y un título
plt.title("Mi primer gráfico de dispersión")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")

# Mostrar el gráfico
plt.show()

"""-x y y
son las coordenadas de los puntos que queremos graficar.

**-plt.scatter(x, y)**
crea el gráfico de dispersión con los puntos.  
(Un scatter plot es un gráfico donde cada punto representa un par de valores. El valor de `x` indica qué tan a la derecha está el punto, y el valor de `y` indica qué tan arriba está. Es útil para ver si dos cosas están relacionadas o cómo cambian juntas.)

**-plt.title, plt.xlabel y plt.ylabel **
agregan un título y etiquetas a los ejes.

**-plt.show() **muestra el gráfico.

`plt.show()` se usa para mostrar el gráfico en pantalla después de haberlo creado con comandos como `plt.scatter`, `plt.plot`, etc. Sin esta línea, el gráfico podría no aparecer dependiendo del entorno.


como podemos ver presenciar un grafico de 5 puntos distribuidos en el plano cartesiano

Paso 3: Personalizar los puntos (colores y tamaños)

1.Ahora vamos a cambiar el color y tamaño de los puntos.

2.Escribe este código en otra celda:
"""

# Coordenadas
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Tamaños de los puntos
sizes = [50, 100, 200, 300, 400]  # Cada punto tendrá un tamaño diferente

# Crear el gráfico
plt.scatter(x, y, color='red', s=sizes, alpha=0.7)

# Etiquetas y título
plt.title("Gráfico con puntos personalizados")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")

# Mostrar el gráfico
plt.show()

"""1.color='red':


Cambia el color de todos los puntos a rojo.
Ejemplo: Si antes los puntos eran azules (el color predeterminado), ahora serán rojos.

2.s=sizes:

Cambia el tamaño de cada punto en función de una lista llamada sizes.
sizes debe ser una lista con el mismo número de elementos que x e y. Cada valor de sizes determina el área de un punto.

3.alpha=0.7:

Controla la transparencia de los puntos.
Los valores van de 0 a 1:

alpha=0 hace que los puntos sean completamente transparentes (invisibles).

alpha=1 hace que los puntos sean completamente opacos.

alpha=0.7 significa que los puntos serán algo transparentes.

**Paso 4: Generar datos aleatorios**

A veces, no tienes datos listos y necesitas generarlos. Usaremos numpy para esto.
"""

# Generar 50 números aleatorios para X e Y
x = np.random.rand(50)  # Valores entre 0 y 1 para X
y = np.random.rand(50)  # Valores entre 0 y 1 para Y

# Crear el gráfico
plt.scatter(x, y, color='blue', s=50)

# Etiquetas y título
plt.title("Gráfico con datos aleatorios")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar el gráfico
plt.show()

"""-np.random.rand(50) genera 50 valores aleatorios entre 0 y 1.

-np.random.rand(n) es una función de NumPy que crea números aleatorios distribuidos de manera uniforme entre 0 y 1.
En este caso, n=50, lo que significa que se generarán 50 números aleatorios.

-El resto del código es igual al gráfico básico, pero ahora estamos usando datos aleatorios.

Paso 5: Usar colores para un dimension

Puedes usar colores para representar una variable extra en el gráfico. Así, cada punto tendrá una posición (X, Y) y un color según su valor.
"""

# Generar datos
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)  # Colores según una tercera variable

# Crear el gráfico
plt.scatter(x, y, c=colors, cmap='viridis', s=100)

# Agregar una barra de colores
plt.colorbar(label="Valor (tercera dimensión)")

# Etiquetas y título
plt.title("Gráfico con colores")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar el gráfico
plt.show()

"""-c=colors: Especifica que los colores de los puntos se asignarán según los valores de la variable colors.


-cmap='viridis': Define el mapa de colores a usar. 'viridis' es una paleta de colores que se ajusta a los valores para visualizar patrones.


-s=100: Cambia el tamaño de los puntos en el gráfico.

-plt.colorbar(label="Valor (tercera dimensión)")
La barra de colores indica el rango de valores que representan los colores en el gráfico.

La etiqueta "Valor (tercera dimensión)" le da contexto a esta barra.

Paso 6: Guardar tu grafico como una imagen
"""

# Crear el gráfico
plt.scatter(x, y, c=colors, cmap='viridis', s=100)
plt.title("Gráfico con colores")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Guardar el gráfico como imagen
plt.savefig("mi_grafico.png", dpi=300)

# Mostrar el gráfico
plt.show()

"""-plt.savefig("mi_grafico.png"): Guarda el gráfico como una imagen con el nombre mi_grafico.png.


-dpi=300: Especifica la resolución de la imagen en puntos por pulgada (dpi). Un valor de 300 es una calidad alta, adecuada para impresión.
"""