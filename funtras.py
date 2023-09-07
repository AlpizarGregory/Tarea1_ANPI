# Funciones trascendentes de la tarea de análisis numérico para ingeniería

tol = 1e-8
iterMax = 2500
pi_t = 3.14159265358979323846
eps = 2.2204e-16


# qué pasa si el número es mayor a iterMax?
def factorial_t(x):
    """
    Calcula el factorial de un número x
    Entradas: x es el número máximo del factorial
    Salidas: x!
    Restricciones: x debe ser positivo
    """
    temp = 1
    count = 0

    while count < x and count < iterMax:
        temp = temp * (count + 1)
        count += 1

    return temp


def div_t(a):
    """
    Calcula la división de 1/a
    Entradas: a es el denominador de la fracción
    Salidas: 1/a
    Restricciones: a debe ser positivo
    """
    if a == 0:
        return [-1, False, "Division by zero: input", 0]
    elif a == 1:
        return [1, True, "Success"]
    elif a < 0:
        return [-1, False, "Input must be positive", 0]

    prev = 0
    if factorial_t(0) < a and a < factorial_t(20):
        prev = power_t(eps, 2)
    elif factorial_t(20)-1 < a < factorial_t(40):
        prev = power_t(eps, 4)
    elif factorial_t(40)-1 < a < factorial_t(60):
        prev = power_t(eps, 8)
    elif factorial_t(60)-1 < a < factorial_t(80):
        prev = power_t(eps, 11)
    elif factorial_t(80)-1 < a < factorial_t(100):
        prev = power_t(eps, 15)
    else:
        return [-1, False, "Division by zero: overflow", 0]

    iter = 0
    act = 0

    while True:
        act = prev * (2 - a * prev)
        iter += 1
        if abs(act - prev) < tol * abs(act) or iter > iterMax:
            break
        prev = act

    return [act, True, "Success", iter]


def exp_t(x):
    """
    Calcula el valor de e^x
    Entradas: x es el exponente de e
    Salidas: e^x
    Restricciones: x debe ser un número real
    """
    act = 0
    prev = 0

    for n in range(iterMax):
        act += power_t(x, n) * div_t(factorial_t(n))[0]
        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, True, "Iteration limit reached", iterMax]


def sin_t(a):
    """
    Calcula el valor de sen(a)
    Entradas: a es el ángulo en radianes
    Salidas: sen(a)
    Restricciones: a debe ser un número real
    """
    act = 0
    prev = 0

    while a > 2 * pi_t:
        a -= 2 * pi_t

    for n in range(iterMax):
        act += power_t(-1, n) * power_t(a, 2 * n + 1) * div_t(factorial_t(2 * n + 1))[0]

        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, True, "Iteration limit reached", iterMax]


def cos_t(a):
    """
    Calcula el valor de cos(a)
    Entradas: a es el ángulo en radianes
    Salidas: cos(a)
    Restricciones: a debe ser un número real
    """
    act = 0
    prev = 0

    while a > 2 * pi_t:
        a -= 2 * pi_t

    for n in range(iterMax):
        act += power_t(-1, n) * power_t(a, 2 * n) * div_t(factorial_t(2 * n))[0]

        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, True, "Iteration limit reached", iterMax]


def tan_t(x):
    """
    Calcula el valor de tan(x)
    Entradas: x es el ángulo en radianes
    Salidas: tan(x)
    Restricciones: x debe ser un número real diferente de pi/2"""
    if cos_t(x) == 0:
        return "Division by zero"
    else:
        return sin_t(x)[0] * div_t(cos_t(x))[0]


def ln_t(a):
    """
    Calcula el valor de ln(a)
    Entradas: a es el número del logaritmo
    Salidas: ln(a)
    Restricciones: a debe ser un número real positivo diferente de 1
    """
    iter = 0
    act = 0
    prev = 0

    while abs(act - prev) < tol and iter < iterMax:
        prev = act
        act += div_t(2 * iter + 1) * power_t((a - 1) * div_t(a + 1), 2 * iter)
        iter += 1

    return 2 * (a - 1) * div_t(a + 1) * act


def log_t(x, a):
    """
    Calcula el valor de log_a(x)
    Entradas: x es el número del logaritmo, a es la base del logaritmo
    Salidas: log_a(x)
    Restricciones: x y a deben ser números reales positivos diferentes de 1
    """
    return ln_t(x) * div_t(ln_t(a))


def power_t(x, y):
    """
    Calcula el valor de x^y
    Entradas: x es la base, y es el exponente
    Salidas: x^y
    Restricciones: x debe ser un número real, y debe ser un número real
    """
    return x**y

def sinh_t(x):
    pass

def cosh_t(x):
    pass


def tanh_t(x):
    pass


def sqrt_t(x):
    pass


def root_t(x, y):
    pass


def asin_t(x):
    pass


def atan_t(x):
    pass


def acos_t(x):
    pass


def sec_t(x):
    pass


def cot_t(x):
    pass


def csc_t(x):
    pass


# pruebas

print ("")
print ("factorial_t")
print (factorial_t(0))
print (factorial_t(1))
print (factorial_t(2))
print (factorial_t(3))
print (factorial_t(4))
print (factorial_t(5))

print ("")
print ("div_t")
print (div_t(2))
print (div_t(3))
print (div_t(4))
print (div_t(5))

print ("")
print ("exp_t")
print (exp_t(1))
print (exp_t(2))
print (exp_t(3))
print (exp_t(4))
print (exp_t(5))

print ("")
print ("sin_t")
print (sin_t(pi_t))
print (sin_t(2 * pi_t))
print (sin_t(3 * pi_t))
print (sin_t(4 * pi_t))
print (sin_t(5 * pi_t))

print ("")
print ("cos_t")
print (cos_t(0))
print (cos_t(pi_t))
print (cos_t(2 * pi_t))
print (cos_t(3 * pi_t))
print (cos_t(4 * pi_t))
print (cos_t(5 * pi_t))

print ("")
print ("tan_t")
print (tan_t(pi_t * div_t(4)))
print (tan_t(pi_t * div_t(2)))
print (tan_t(3 * pi_t * div_t(4)))
print (tan_t(pi_t))

print ("")
print ("ln_t")
print (ln_t(1))
print (ln_t(2))
print (ln_t(3))
print (ln_t(4))
print (ln_t(5))

print ("")
print ("log_t")
print (log_t(2, 2))
print (log_t(3, 2))
print (log_t(4, 2))
print (log_t(5, 2))

print ("")
print ("power_t")
print (power_t(2, 2))
print (power_t(2, 3))
print (power_t(2, 4))
print (power_t(2, 5))

"""
print ("")
print ("sinh_t")
print (sinh_t(0))
print (sinh_t(2 * pi_t))

print ("")
print ("cosh_t")
print (cosh_t(0))
print (cosh_t(2 * pi_t))

print ("")
print ("tanh_t")
print (tanh_t(0))
print (tanh_t(2 * pi_t))

print ("")
print ("sqrt_t")
print (sqrt_t(2))
print (sqrt_t(3))

print ("")
print ("root_t")
print (root_t(2, 2))
print (root_t(2, 3))

print ("")
print ("asin_t")
print (asin_t(0))
print (asin_t(1))

print ("")
print ("atan_t")
print (atan_t(0))
print (atan_t(1))

print ("")
print ("acos_t")
print (acos_t(0))
print (acos_t(1))

print ("")
print ("sec_t")
print (sec_t(0))
print (sec_t(pi_t))

print ("")
print ("cot_t")
print (cot_t(0))
print (cot_t(pi_t))

print ("")
print ("csc_t")
print (csc_t(0))
print (csc_t(pi_t))
"""