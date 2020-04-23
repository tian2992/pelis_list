

#fibonacci

# Para obtener un numero de la secuencia fibonacci
# necesitamos el indice a generar de la secuencia
#
# obtenemos el termino correspondiente

#fibo(0) = 1
#fibo(1) = 1n
#fibo(2) = 2
#fibo(3) = 3
#fibo(4) = 5
#fibo(5) = 8

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
from nose.tools import *

from fibo import fibo

import unittest


class FiboTest(unittest.TestCase):

    def test_first3(self):
        assert_equal(fibo(1),1)
        assert_equal(fibo(2),1)
        assert fibo(3) == 2
        assert fibo(4) == 3

    def test_more(self):
        assert_equal(fibo(10), 55)
        assert_equal(fibo(15), 610)


## Funcion 2
## Para un numero dado una funcion que imprima solo los numeros impares

## Funcion 3
# # Para un numero dado retorne el total de numeros menores a el divisibles por 3, 4 y 5
#
# func3(100) = {
#     3: 34
#     4: 25
#     5: 20
# }