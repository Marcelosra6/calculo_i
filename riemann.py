"""calcular el área bajo la curva de la función f(x) = x^2 entre los puntos x = 2 y x = 5.
 Determine el área utilizando el método de Riemann con 4 subintervalos usando los datos de la derecha."""
import numpy as np

a=2
b=5
n=4 #n coeficientes
var_x=(b-a)/n
coeficientes=