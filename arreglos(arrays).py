# -*- coding: utf-8 -*-
#RF1:Obtener la mayor nota y la menor nota
#RF2:Imprimir la nota promedio del curso
#RF3:Cuántos estudiantes aprobaron y cuántos reprobaron
#RF4:imprimir el código y un mensaje de acuerdo con la nota:
#❖ Cuántos obtuvieron una nota Muy bien [ 4.0 ­ 5.0]
#❖ Cuántos obtuvieron una nota Bien [ 3.0 ­ 4.0 )
#❖ Cuántos obtuvieron una nota suficiente [ 2.0 ­ 3.0 )
#❖ Cuántos obtuvieron una nota Insuficiente [ 0,5 ­ 2.0 )
#RF5:Decir cuántos estudiantes quedaron en cada una de las categorías anteriores
#RF6:mostrar el porcentaje de estudiantes aprobados y reprobados.
#RF7:Imprimir un listado con los códigos de los estudiantes que obtuvieron la más alta nota
#solicito el tamaño del vector
n=(input("digite el numero de estudiantes: "))
#inicializo/creo vectores
v1=["" for x in range(0,n)]
v2=[0.0 for x in range (0,n)]
#doy valor inicial a las variables
#variable para la suma de las notas
a=0
#variable para la condicion "insuficiente"
b=0
#variable para la condicion de estudiantes aprobados
c=0
#variable para la condicion de "suficiente"
d=0
#variable para la condicion "insuficiente"
e=0
#variable para la condicion "bien"
f=0
#variable para la condicion "muy bien"
g=0
#solicitar datos de los vectores
for i in range (0,n):
    print ("codigo----->", i+1)
    #solicito codigo
    v1[i]=raw_input("")
    #solicito nota
    nota=(input("digite la nota"))
    #condicion nota entre 0.0 y 5.0
    while(nota<0.0 or nota>5.0):
        nota=(input("nota"))
    #se guarda la nota dentro del vector     
    v2[i]=nota
    #se va sumando y guardando en a la suma de todas las notas
    a=a+v2[i]
#Doy valor inicial  a k(mayor nota) y m(menor nota)
k=v2[0]
m=v2[0]

for i in range(0,n):
    #condicionales para el RF4
    if (v2[i]<3 and v2[i]>2):
        #contador est.reprob
        b=b+1
        #contador para esta condicion
        d=d+1
        #mostrar datos
        print (v1[i],v2[i],"suficiente")
    elif(v2[i]>=3 and v2[i]<4):
        #contador est.aprob
        c=c+1
        #contador para esta condicion
        f=f+1
        #mostrar datos
        print (v1[i], v2[i], "bien")
    elif(v2[i]>=4 and v2[i]<=5):
        #mostrar datos
        print (v1[i], v2[i], "muy bien")
        #contador est. aprob
        c=c+1
        #contador para esta condicion
        g=g+1
    else:       
        #contador para esta condicion
        e=e+1
        #mostrar datos
        print (v1[i], v2[i], "insuficiente")
        #contador est.reprob
        b=b+1
for i in range(0,n):
    #condicion para sacar la menor nota
    if v2[i]<m:
        m=v2[i]
    #condicion para sacar la mejor nota
    if v2[i]>k:
        k=v2[i]
#mostrar la mayor(k) y menor nota(m)
print("la menor nota fue ", m)
print ("la mayor nota fue de ",k)


for i in range(0,n):
    #condicion para hayar posicion
    if k==v2[i]:
        l=i
        #se busca la misma posicion en la otra lista para mostrar su codigo 
        print("el/los estudiante(s) que tiene(n) dicha nota es/son",v1[i])
        
        
#porcentaje est. reprob.
h=float(b*100)/n 
#porcentaje est aprob
j=float(c*100)/n   
#promedio 
p=float(a)/n  
#se muestran los datos sacados los datos 
print("el promedio del curso es: ", p)
print("Reprueban ",b," estudiantes y aprueban ",c," estudiantes")
print (d," estudiantes quedaron en suficiente ",e,"estudiantes quedaron en insuficiente")
print (f," estudiantes quedaron en bien y ",g,"estudiantes quedaron en muy bien")
print (h,"% reprobaron ",j,"% aprobaron")
