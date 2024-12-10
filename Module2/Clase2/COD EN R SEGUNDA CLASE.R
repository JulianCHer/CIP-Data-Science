library(readr)
str(df)

T1=table(df$City)#tabla Uno
T1

library(ggplot2)#Diagrama de frecuencias absolutas
TDF1=data.frame(T1)
ggplot(TDF1,aes(x=Var1, y=Freq, fill=Var1))+
  geom_bar(stat = "identity",
           position=position_dodge())+
  labs(title="Diagrama de barras de frecuencia Absoluta",
       x="Gender",
       y="Frecuencia Absoluta")+
  geom_text(aes(label=Freq),
            position = position_dodge(0.5),
            vjust=1)

TP1=round(prop.table(T1),2)#Diagrama circular
TDF2=data.frame(TP1)
TDF2
ggplot(TDF2,aes(x="", y=Freq, fill=Var1))+
  geom_bar(stat = "identity")+
  geom_text(aes(label=Freq),
            position = position_stack(vjust=0.1))+
  coord_polar(theta = "y")+
  labs(title="Diagrama de circular de frecuencia relativa")

library(ggplot2)#Histograma edad solo cuantitativas
ggplot(df, aes(x=PaymentTier))+
  geom_histogram(bins=clases,
                 color="red",
                 lwd=0.1,
                 linetype=1, 
                 position = "identity", 
                 fill="blue")+
  labs(title="Histograma de edad", 
       x="Edad",
       y="Frecuencia Absoluta")

TC1=table(df$Education,#Gender y Educacion 
          df$City)
TC1



tab.prob=prop.table(table(df$Age))#sex es V2, tener en cuenta como estan llamadas las variables
tab.prob#probabilidad
cbind(round(tab.prob,4))#redondear decimales
addmargins(table(df$Gender,df$Education))#tabla de contingencia
barplot(tab.prob,
        main="Diagrama de barras (sexo,dirección)",
        ylab="Probabilidad",
        xlam="Sexo vs Dirección",
        beside=TRUE,
        col=c("red","blue"))

library(vtree)
vtree(df$Age)#árbol



