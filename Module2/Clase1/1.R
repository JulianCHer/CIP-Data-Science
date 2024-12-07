library(readr)
View(df)#muestra la tabla de las variables
summary(df)#resumen estadistico
#medidas de tendencia central
#media
mean(df$Age)
#mediana
median(df$Age)
#moda
table(df$Age)
#cbind es pasar de fila a columna una serie de datos 
mods=cbind(table(df$Age))
unique(ifelse(mods==max(mods),1,0))
#medidas de variacion
#la varianza es un promedio de distancia del dato a la media 
var(df$Age)
#la desviación estandar es la disperción de los datos
sd(df$Age)
sqrt(var(df$Age))
#medidas de posición
#Q1 corresponde al 25% de la distribución de los datos 
#Q2 es el mediana, es decir el 50% de la distribución de los datos
#Q3 es el 75% de la distribución de los datos 
quantile(df$Age,0.25)
#menores o iguales a Q1
quantile(df$Age,0.50)
#menores o iguales a Q2
quantile(df$Age,0.75)
#menores o iguales a Q3
quantile(df$Age,c(0.25,0.5,0.75))
#diagrama de caja y bigote
boxplot(df$Age,
        main="Diagrama de caja y bigote",
        horizontal=TRUE,
        col="red")
install.packages("moments")
library(moments)
kurtosis(df$Age)
#grafica
table (df$Gender)
table (df$Product)
attach(df)
View(df)
x<-table(df$Product)
color= c("blue", "orange","purple")
barplot(x, xlab ="Productos", ylab = "Frecuencias", main = "Products", col = color)