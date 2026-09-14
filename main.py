# main.py
import MYTOOLS

# Exibindo as constantes
print("Constante PI_INT (primeiras casas):", MYTOOLS.PI_INT)
print("Constante E_INT (primeiras casas):", MYTOOLS.E_INT)
print("-" * 50)

# Testando as funções
print("Pi com 5 casas decimais:", MYTOOLS.pi_real(5))
print("Euler com 4 casas decimais:", MYTOOLS.e_real(4))
print("Pi com 10 casas decimais:", MYTOOLS.pi_real(10))