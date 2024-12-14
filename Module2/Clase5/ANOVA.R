summary(Anovaiq)
Anovaiq #solo el nombre de la base de datos muestra los datos en consola 
attach(Anovaiq)#separan los datos
names(Anovaiq)#separan los datos
class(Grupo)#me dice que clase de variable es grupo
class(IQ)#me dice que clase de variable es IQ 
factor(Grupo)#me dice cuantos grupos tiene la variable, en este caso fisica, matematicas y fisica
library(rapportools)
boxplot(IQ~Grupo)#genera el diagrama de caja para verificar las medias 
aov(IQ~Grupo)#genera la suma de cuadrados y los grados de libertad
anova1=aov(IQ~Grupo)#se busca encontrar los grados de libertad
summary(anova1) #Analisis estadistico
TukeyHSD(anova1)#la prueba tukey tiene como objetivo identificar cuales grupos son significativamente diferentes entre si
#en este caso nos dice que matematicas y fisica tiene medias muy parecidas, las otras dos comparaciones
#son diferentes al ser menor a 0,5

