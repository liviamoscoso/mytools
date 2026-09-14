# MYTOOLS.py

# 100 primeiras casas decimais de PI (sem o 3.)
PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

# 100 primeiras casas decimais de Euler/Neperiano (sem o 2.)
E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def pi_real(N):
    """Retorna a aproximação de Pi com N casas decimais."""
    if 0 < N <= 100:
        return f"3,{PI_INT[:N]}"
    raise ValueError("N deve ser maior que 0 e menor ou igual a 100.")

def e_real(N):
    """Retorna a aproximação do número de Euler com N casas decimais."""
    if 0 < N <= 100:
        return f"2,{E_INT[:N]}"
    raise ValueError("N deve ser maior que 0 e menor ou igual a 100.")