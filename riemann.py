"""calcular el área bajo la curva de la función f(x) = x^2 entre los puntos [2,5].
 Determine el área utilizando el método de Riemann con 4 subintervalos usando los puntos de la derecha, izquierda y centro."""
import numpy as np

a=2
b=5
n=4 #n coeficientes
Δ_x=(b-a)/n

print("Datos:")
print(f"a (inicio del intervalo) = {a}")
print(f"b (fin del intervalo) = {b}")
print(f"n (número de subintervalos) = {n}")
print(f"Δ_x (ancho de cada subintervalo) = {Δ_x}\n")

val_der=np.linspace(a+Δ_x,b,n)
val_izq=np.linspace(a,b-Δ_x,n)
val_med=np.linspace(a+(Δ_x/2),b-(Δ_x/2),n)

def f(x):
    x=x**2
    return x

print("Función:")
print("f(x) = x^2\n")

def riemann_izq():
    integral = np.sum(Δ_x * f(val_izq))
    return integral

def riemann_der():
    integral = np.sum(Δ_x * f(val_der))
    return integral

def riemann_med():
    integral = np.sum(Δ_x * f(val_med))
    return integral

integral_der = riemann_der()
integral_izq = riemann_izq()
integral_med = riemann_med()

print("Resultados:")
print(f"Integral de Riemann por la derecha: {integral_der}\n")
print(f"Integral de Riemann por la izquierda: {integral_izq}\n")
print(f"Integral de Riemann por punto medio: {integral_med}\n")