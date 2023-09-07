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

print("")
print("factorial_t")
print("0!: ", factorial_t(0))
print("1!: ", factorial_t(1))
print("2!: ", factorial_t(2))
print("33!: ", factorial_t(3))
print("42!: ", factorial_t(4))

print("")
print("div_t")
print("1/1: ", div_t(1))
print("1/2: ", div_t(2))
print("1/3: ", div_t(3))
print("1/4: ", div_t(4))
print("1/5: ", div_t(5))

print("")
print("exp_t")
print("e^0: ", exp_t(0))
print("e^1: ", exp_t(1))
print("e^2: ", exp_t(2))
print("e^3: ", exp_t(3))
print("e^4: ", exp_t(4))

print("")
print("sin_t")
print("sen 0: ", sin_t(0))
print("sen pi: ", sin_t(pi_t))
print("sen pi/4: ", sin_t(pi_t/4))
print("sen 180: ", sin_t(180))
print("sen 270: ", sin_t(270))
print("sen 360: ", sin_t(360))
print("sen 18: ", sin_t(18))

print("")
print("cos_t")
print("cos 0: ", cos_t(0))
print("cos pi: ", cos_t(pi_t))
print("cos pi/4: ", cos_t(pi_t/4))
print("cos 180: ", cos_t(180))
print("cos 270: ", cos_t(270))

print("")
print("tan_t")
print("tan 0: ", tan_t(0))
print("tan pi: ", tan_t(pi_t))
print("tan pi/4: ", tan_t(pi_t/4))
print("tan 180: ", tan_t(180))
print("tan 270: ", tan_t(270))

print("")
print("ln_t")
print("ln 0: ", ln_t(0))
print("ln 1: ", ln_t(1))
print("ln 12: ", ln_t(12))
print("ln 292: ", ln_t(292))
print("ln 333: ", ln_t(333))
print("ln 400: ", ln_t(400))

print("")
print("log_t")
print("log 0: ", log_t(0, 0))
print("log 1: ", log_t(1, 1))
print("log 12: ", log_t(12, 12))
print("log 292: ", log_t(292, 292))
print("log 333: ", log_t(333, 333))
print("log 400: ", log_t(400, 400))

print("")
print("power_t")
print("2^2: ", power_t(2, 2))
print("2^3: ", power_t(2, 3))
print("2^4: ", power_t(2, 4))
print("2^5: ", power_t(2, 5))
print("2^6: ", power_t(2, 6))

print("")
print("sinh_t")


print("")
print("cosh_t")

print("")
print("tanh_t")

print("")
print("sqrt_t")

print("")
print("root_t")

print("")
print("asin_t")

print("")
print("atan_t")

print("")
print("acos_t")

print("")
print("sec_t")

print("")
print("cot_t")

print("")
print("csc_t")