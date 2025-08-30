#Trabajo Practico 1
#------------------

#ejercicio1

print("Hola mundo");

#ejercicio2

nombre = input("Ingresa tu nombre: ");
print(f"Hola", nombre);

#ejercicio3

nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
edad = int(input("Ingrese su edad: "));
lugar_de_residencia=input("Donde vives: ");
print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugar_de_residencia}");

#ejecicio4

import math;
radio = float (input("Ingrese el radio: "));
area = math.pi * radio **2;
perimetro = 2 * math.pi*radio;
print (f"El area del circulo es: {area} y el perimetro es: {perimetro}");

#ejercicio5

segundos = int(input("Ingrese la cantidad de segundos: "));
horas = segundos // 3600;
print(f"La cantidad de horas ingresadas en segundos son: {horas}");

#ejercicio6

numero = int(input("Ingrese un numero: "));
print(numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10);

#ejercicio7

numero1 = int(input("Ingrese un primer numero mayor que 0: "));
numero2 = int(input("Ingrese un segundo numero mayor que 0: "));
suma = numero1 + numero2;
resta= numero1 - numero2;
multiplicacion = numero1 * numero2;
division = numero1 / numero2;
print(f"La suma es: {suma}, la resta es: {resta}, la multiplicacion es: {multiplicacion}, y la division es:{division} ");

#ejercicio8

altura = float(input("Ingrese su altura: "));
peso = float(input("Ingrese su peso: "));
masa_corporal = peso / altura ** 2;
print(f"La masa corporal es: {masa_corporal}");

#ejercicio9

grados_c = float(input("Ingrese la temperatura en grados celsius: "));
grados_f = 9/5 * grados_c + 32;
print(f"Los grados en fahrenheit son: {grados_f}");

#ejercicio10

num1 = int(input("Ingrese el primer numero: "));
num2 = int(input("Ingrese el segundo numero: "));
num3 = int(input("Ingrese el tercer numero: "));
promedio = (num1 + num2 + num3) / 3;
print("El promedio es ", promedio);