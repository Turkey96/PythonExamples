# -*- coding: utf-8 -*-
#RF1. ​Calcular el promedio de edad del curso.
#RF2​. Imprimir la mayor edad del grupo.
#RF3.​Imprimir la menor edad del grupo.
#RF4.​Imprimir Cuántos estudiantes están entre los 17 y 20 años.
#RF5. Mostrar cuál es la edad que más se repite ( moda ) y cuantas veces se encuentra en el vector.
#RF6.​Calcular la desviación estándar de los datos.
#imporot de la biblioteca math
import math
#inicializo vector
v1=[16, 16, 15, 16, 17, 18, 17, 15, 18, 16, 20, 19, 17, 15, 16, 20, 20, 22, 16, 15, 16, 16, 18, 17, 20, 21, 22, 15, 16, 15, 15, 16, 20, 20, 21, 22, 19, 18, 17, 17]
#inicializo variable para la sumatoria
k=0
for i in range (0,40):
    k=k+v1[i]
#se realiza la operacion para el promedio
p=float(k)/40
#se muestra el promedio
print("el promedio de edad es: ", p)
#inicializo las variables de mayor(Me) y menor(m)  edad
Me=0
m=v1[0]
#se busca la mayor edad con ayuda de "for"
for i in range(0,39):
    if v1[i]<v1[i+1]:
        Me=v1[i+1]
#se busca la menor edad con ayuda de "for"
for i in range(0,40):
    if v1[i]<m:
            m=v1[i]   
#se muestran los valores
print ("la mayor edad es: ", Me)
print (" la menor edad es: ", m)
#inicializo contador
c=0
#se buscan los valores que esten entre 17 y 20
for i in range (40):
    if (v1[i]<=20) and v1[i]>=17:
        c=c+1 
#se muestra el resultado
print ("la cantidad de estudiantes entre 17 y 20 es: ", c)
#inicializo k
k=0
#se realiza la operacion que requierre condicional
for i in range (0,40):
    #se guarda en k
    k=k+(v1[i]-p)**2
#se termina de realizar la operacion y se guarda en "de" 
de=math.sqrt((k)/(40-1))
#se muestra el valor
print("la desviacion estandar es de: ", de)
