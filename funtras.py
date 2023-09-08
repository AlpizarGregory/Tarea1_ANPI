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
    Uso: factorial_t(x)
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
    Salidas: [1/a, Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: a debe ser positivo
    Uso: div_t(a) y utilice índices para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    sign = 1
    if a < 0:
        a = -a
        sign = -1
        
    elif a < tol:
        return [-1, False, "Division by zero", 0]
    elif a == 1:
        return [1, True, "Success"]

    prev = 0
    if a < factorial_t(0):
        prev = eps
    elif factorial_t(0) < a and a < factorial_t(20):
        prev = power_t(eps, 2)
    elif factorial_t(20) <= a < factorial_t(40):
        prev = power_t(eps, 4)
    elif factorial_t(40) <= a < factorial_t(60):
        prev = power_t(eps, 8)
    elif factorial_t(60) <= a < factorial_t(80):
        prev = power_t(eps, 11)
    elif factorial_t(80) <= a < factorial_t(100):
        prev = power_t(eps, 15)
    else:
        return [0, False, "Division by infinite: overflow", 0]

    iter = 0
    act = 0

    while True:
        act = prev * (2 - a * prev)
        iter += 1
        if abs(act - prev) < tol * abs(act) or iter > iterMax:
            break
        prev = act

    return [sign * act, True, "Success", iter]


def exp_t(x):
    """
    Calcula el valor de e^x
    Entradas: x es el exponente de e
    Salidas: [e^x, Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: exp_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    act = 0
    prev = 0

    for n in range(iterMax):
        division = div_t(factorial_t(n))
        if division[1] == False:
            return [act, False, division[2], n]
        act += power_t(x, n) * division[0]
        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, False, "Iteration limit reached", iterMax]


def sin_t(a):
    """
    Calcula el valor de sen(a)
    Entradas: a es el ángulo en radianes
    Salidas: [sen(a), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: a debe ser un número real
    Uso: sin_t(a) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    act = 0
    prev = 0

    while a > 2 * pi_t:
        a -= 2 * pi_t

    for n in range(iterMax):
        division = div_t(factorial_t(2 * n + 1))
        if division[1] == False:
            return [act, False, division[2], n]
        act += power_t(-1, n) * power_t(a, 2 * n + 1) * division[0]

        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, False, "Iteration limit reached", iterMax]


def cos_t(a):
    """
    Calcula el valor de cos(a)
    Entradas: a es el ángulo en radianes
    Salidas: [cos(a), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: a debe ser un número real
    Uso: cos_t(a) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    act = 0
    prev = 0

    while a > 2 * pi_t:
        a -= 2 * pi_t

    for n in range(iterMax):
        division = div_t(factorial_t(2 * n))
        if division[1] == False:
            return [act, False, division[2], n]
        act += power_t(-1, n) * power_t(a, 2 * n) * division[0]

        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, False, "Iteration limit reached", iterMax]


def tan_t(x):
    """
    Calcula el valor de tan(x)
    Entradas: x es el ángulo en radianes
    Salidas: [tan(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real diferente de pi/2
    Uso: tan_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """

    while x > 2 * pi_t:
        x -= 2 * pi_t

    sin = sin_t(x)
    if sin[1] == False:
        return [0, False, sin[2], 0]

    cos = cos_t(x)
    if cos[1] == False:
        return [0, False, cos[2], 0]

    division = div_t(cos[0])
    if division[1] == False:
        return [0, False, division[2], 0]

    return [sin[0] * division[0], True, "Success", 0]


def ln_t(a):
    """
    Calcula el valor de ln(a)
    Entradas: a es el número del logaritmo
    Salidas: [ln(a), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: a debe ser un número real positivo diferente de 1
    Uso: ln_t(a) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    iter = 0
    act = 0
    prev = 0

    while abs(act - prev) < tol and iter < iterMax:
        prev = act
        division1 = div_t(2 * iter + 1)
        if division1[1] == False:
            return [act, False, division1[2], iter]

        division2 = div_t(a + 1)
        if division2[1] == False:
            return [act, False, division2[2], iter]
        act += division1[0] * power_t((a - 1) * division2[0], 2 * iter)
        iter += 1

    division3 = div_t(a + 1)
    if division3[1] == False:
        return [act, False, division3[2], iter]
    return [2 * (a - 1) * division3[0] * act, True, "Success", iter]


def log_t(x, a):
    """
    Calcula el valor de log_a(x)
    Entradas: x es el número del logaritmo, a es la base del logaritmo
    Salidas: [log_a(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x y a deben ser números reales positivos diferentes de 1
    Uso: log_t(x, a) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    lnx = ln_t(x)
    if lnx[1] == False:
        return [0, False, lnx[2], 0]

    lna = ln_t(a)
    if lna[1] == False:
        return [0, False, lna[2], 0]

    division = div_t(lna[0])
    if division[1] == False:
        return [0, False, division[2], 0]

    return [lnx[0] * division[0], True, "Success", 0]


def power_t(x, y):
    """
    Calcula el valor de x^y
    Entradas: x es la base, y es el exponente
    Salidas: x^y
    Restricciones: tanto x como y deben ser números reales
    Uso: power_t(x, y)
    """
    return x**y


def sinh_t(x):
    """
    Calcula el valor de sinh(x)
    Entradas: x es el ángulo en radianes
    Salidas: [sinh(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: sinh_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    e1 = exp_t(x)
    e2 = exp_t(-x)
    if e1[1] == False:
        return [0, False, e1[2], 0]
    if e2[1] == False:
        return [0, False, e2[2], 0]
    
    return [(e1[0] - e2[0]) * 0.5, True, "Success", 0]


def cosh_t(x):
    """
    Calcula el valor de cosh(x)
    Entradas: x es el ángulo en radianes
    Salidas: [cosh(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: cosh_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    e1 = exp_t(x)
    e2 = exp_t(-x)
    if e1[1] == False:
        return [0, False, e1[2], 0]
    if e2[1] == False:
        return [0, False, e2[2], 0]
    
    return [(e1[0] + e2[0]) * 0.5, True, "Success", 0]


def tanh_t(x):
    """
    Calcula el valor de tanh(x)
    Entradas: x es el ángulo en radianes
    Salidas: [tanh(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: tanh_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    sinh = sinh_t(x)
    if sinh[1] == False:
        return [0, False, sinh[2], 0]
    
    cosh = cosh_t(x)
    if cosh[1] == False:
        return [0, False, cosh[2], 0]
    
    division = div_t(cosh[0])
    if division[1] == False:
        return [0, False, division[2], 0]
    
    return [sinh[0] * division[0], True, "Success", 0]


def sqrt_t(x):
    """
    Calcula el valor de sqrt(x)
    Entradas: x es el radicando
    Salidas: [sqrt(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real positivo
    Uso: sqrt_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    if x < tol:
        return [-1, False, "Invalid input: Square root of zero", 0]
    return root_t(x, 2)


def root_t(x, y):
    """
    Calcula el valor de x^(1/y)
    Entradas: x es la base, y es el exponente
    Salidas: [x^(1/y), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real positivo, y debe ser un número real positivo diferente de 0
    Uso: root_t(x, y) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    if x < tol:
        return [-1, False, "Invalid input: Root of zero", 0]
    elif y < 0:
        return [-1, False, "Invalid input: 0th root", 0]
    elif y == 1:
        return [x, True, "Success", 0]

    act = 0
    prev = x * 0.5

    for n in range(iterMax):
        division = div_t(y * power_t(prev, y - 1))
        if division[1] == False:
            return [act, False, division[2], n]

        act = prev - (power_t(prev, y) - x) * division[0]

        if abs(act - prev) < tol * act:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, False, "Iteration limit reached", iterMax]


def asin_t(a):
    """
    Calcula el valor de asin(a)
    Entradas: a es el número del seno inverso
    Salidas: [asin(a), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: a debe ser un número real entre -1 y 1
    Uso: asin_t(a) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    act = 0
    prev = 0

    if a < -1 or a > 1:
        return [-1, False, "Input must be between -1 and 1", 0]

    if a == 1:
        return [pi_t * 0.5, True, "Success", 0]
    elif a == -1:
        return [-pi_t * 0.5, True, "Success", 0]

    for n in range(iterMax):
        division = div_t(power_t(4, n) * power_t(factorial_t(n), 2) * (2 * n + 1))
        if division[1] == False:
            return [act, False, division[2], n]
        
        act += factorial_t(2 * n) * division[0] * power_t(a, 2 * n + 1)

        if abs(act - prev) < tol:
            return [act, True, "Success", n]
        prev = act
    else:
        return [act, False, "Iteration limit reached", iterMax]


def atan_t(a):
    """
    Calcula el valor de atan(a)
    Entradas: a es el número del tangente inverso
    Salidas: [atan(a), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: a debe ser un número real
    Uso: atan_t(a) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    act = 0
    prev = 0

    if a == 1:
        return [pi_t * 0.25, True, "Success", 0]
    elif a == -1:
        return [-pi_t * 0.25, True, "Success", 0]

    if a >= -1 and a <= 1:
        for n in range(iterMax):
            division = div_t(2 * n + 1)
            if division[1] == False:
                return [act, False, division[2], n]
            act += power_t(-1, n) * power_t(a, 2 * n + 1) * division[0]

            if abs(act - prev) < tol:
                return [act, True, "Success", n]
            prev = act
        else:
            return [act, False, "Iteration limit reached", iterMax]

    else:
        isNegative = False
        if a < 0:
            a = -a
            isNegative = True

        for n in range(iterMax):
            division = div_t((2 * n + 1) * power_t(a, 2 * n + 1))

            if division[1] == False:
                if a > 1:
                    return [pi_t * 0.5 - act, False, division[2], n]

                else:
                    return [-pi_t * 0.5 - act, False, division[2], n]

            act += power_t(-1, n) * division[0]

            if abs(act - prev) < tol:

                if isNegative:
                    return [-pi_t * 0.5 - act, True, "Success", n]

                else:
                    return [pi_t * 0.5 - act, True, "Success", n]
            prev = act

        else:

            if isNegative:
                return [-pi_t * 0.5 - act, False, "Iteration limit reached", iterMax]

            else:
                return [pi_t * 0.5 - act, False, "Iteration limit reached", iterMax]


def acos_t(x):
    """
    Calcula el valor de acos(x)
    Entradas: x es el número del coseno inverso
    Salidas: [acos(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real entre -1 y 1
    Uso: acos_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    return pi_t * 0.5 - asin_t(x)[0]


def sec_t(x):
    """
    Calcula el valor de sec(x)
    Entradas: x es el ángulo en radianes
    Salidas: [sec(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: sec_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    cos = cos_t(x)
    if cos[1] == False:
        return [0, False, cos[2], 0]
    
    division = div_t(cos_t(x)[0])
    if division[1] == False:
        return [0, False, division[2], 0]
    
    return [division[0], True, "Success", 0]

def cot_t(x):
    """
    Calcula el valor de cot(x)
    Entradas: x es el ángulo en radianes
    Salidas: [cot(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: cot_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    tan = tan_t(x)
    if tan[1] == False:
        return [0, False, tan[2], 0]
    
    division = div_t(tan_t(x)[0])
    if division[1] == False:
        return [0, False, division[2], 0]
    
    return [division[0], True, "Success", 0]

def csc_t(x):
    """
    Calcula el valor de csc(x)
    Entradas: x es el ángulo en radianes
    Salidas: [csc(x), Booleano de éxito, mensaje de error, iteraciones]
    Restricciones: x debe ser un número real
    Uso: csc_t(x) y utilice índices '[#]' para acceder a los valores, [0] para el resultado, [1] para el booleano, [2] para el mensaje de error y [3] para la cantidad de iteraciones.
    """
    sin = sin_t(x)
    if sin[1] == False:
        return [0, False, sin[2], 0]
    
    division = div_t(sin_t(x)[0])
    if division[1] == False:
        return [0, False, division[2], 0]
    
    return [division[0], True, "Success", 0]


# pruebas

print("")
print("factorial_t")
print("0!: ", factorial_t(0))
print("1!: ", factorial_t(1))
print("2!: ", factorial_t(2))
print("33!: ", factorial_t(33))
print("42!: ", factorial_t(42))

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
print("sen pi/4: ", sin_t(pi_t / 4))
print("sen 180: ", sin_t(180))
print("sen 270: ", sin_t(270))
print("sen 360: ", sin_t(360))
print("sen 18: ", sin_t(18))

print("")
print("cos_t")
print("cos 0: ", cos_t(0))
print("cos pi: ", cos_t(pi_t))
print("cos pi/2: ", cos_t(pi_t / 2))
print("cos pi/4: ", cos_t(pi_t / 4))

print("")
print("tan_t")
print("tan 0: ", tan_t(0))
print("tan pi: ", tan_t(pi_t))
print("tan pi/4: ", tan_t(pi_t / 4))
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
print("sinh 0: ", sinh_t(0))
print("sinh 1: ", sinh_t(1))
print("sinh 2: ", sinh_t(2))
print("sinh 3: ", sinh_t(3))
print("sinh 4: ", sinh_t(4))

print("")
print("cosh_t")
print("cosh 0: ", cosh_t(0))
print("cosh 1: ", cosh_t(1))
print("cosh 2: ", cosh_t(2))
print("cosh 3: ", cosh_t(3))
print("cosh 4: ", cosh_t(4))

print("")
print("tanh_t")
print("tanh 0: ", tanh_t(0))
print("tanh 1: ", tanh_t(1))
print("tanh 2: ", tanh_t(2))
print("tanh 3: ", tanh_t(3))
print("tanh 4: ", tanh_t(4))

print("")
print("sqrt_t")
print("sqrt 0: ", sqrt_t(0))
print("sqrt 1: ", sqrt_t(1))
print("sqrt 2: ", sqrt_t(2))
print("sqrt 10: ", sqrt_t(10))
print("sqrt 25: ", sqrt_t(25))

print("")
print("root_t")
print("root 2, 2: ", root_t(2, 2))
print("root 3, 2: ", root_t(3, 3))
print("root 4, 2: ", root_t(4, 2))

print("")
print("asin_t")
print("asin 0: ", asin_t(0))
print("asin 1: ", asin_t(1))
print("asin -0.707193123: ", asin_t(-0.707193123))
print("asin 0.707193123: ", asin_t(0.707193123))
print("asin 0.5: ", asin_t(0.5))
print("asin -0.25: ", asin_t(0.25))
print("asin 0.75: ", asin_t(0.75))
print("asin -0.125: ", asin_t(0.125))
print("asin 0.875: ", asin_t(0.875))
print("asin -0.0625: ", asin_t(0.0625))
print("asin 0.03125: ", asin_t(0.03125))
print("asin -0.015625: ", asin_t(0.015625))

print("")
print("atan_t")
print("entre -1 y 1")
print("atan 0: ", atan_t(0))
print("atan 1: ", atan_t(1))
print("atan -1: ", atan_t(-1))
print("atan 0.5: ", atan_t(0.5))
print("atan -0.5: ", atan_t(-0.5))
print("atan 0.25: ", atan_t(0.25))
print("atan -0.25: ", atan_t(-0.25))
print("atan 0.75: ", atan_t(0.75))
print("atan -0.75: ", atan_t(-0.75))
print("atan 0.125: ", atan_t(0.125))
print("atan -0.125: ", atan_t(-0.125))
print("atan 0.875: ", atan_t(0.875))
print("atan -0.875: ", atan_t(-0.875))
print("atan 0.0625: ", atan_t(0.0625))
print("atan -0.0625: ", atan_t(-0.0625))
print("atan 0.03125: ", atan_t(0.03125))
print("atan -0.03125: ", atan_t(-0.03125))
print("atan 0.015625: ", atan_t(0.015625))
print("atan -0.015625: ", atan_t(-0.015625))
print("mayor a 1")
print("atan 1.5: ", atan_t(1.5))
print("atan 1.25: ", atan_t(1.25))
print("atan 1.75: ", atan_t(1.75))
print("atan 1.125: ", atan_t(1.125))
print("atan 1.875: ", atan_t(1.875))
print("atan 1.0625: ", atan_t(1.0625))
print("atan 1.03125: ", atan_t(1.03125))
print("atan 1.015625: ", atan_t(1.015625))
print("atan 2: ", atan_t(2))
print("atan 3: ", atan_t(3))
print("atan 4: ", atan_t(4))
print("atan 5: ", atan_t(5))
print("atan 6: ", atan_t(6))
print("atan 7: ", atan_t(7))
print("menor a -1")
print("atan -1.5: ", atan_t(-1.5))
print("atan -1.25: ", atan_t(-1.25))
print("atan -1.75: ", atan_t(-1.75))
print("atan -1.125: ", atan_t(-1.125))
print("atan -1.875: ", atan_t(-1.875))
print("atan -1.0625: ", atan_t(-1.0625))
print("atan -1.03125: ", atan_t(-1.03125))
print("atan -1.015625: ", atan_t(-1.015625))
print("atan -2: ", atan_t(-2))
print("atan -3: ", atan_t(-3))
print("atan -4: ", atan_t(-4))
print("atan -5: ", atan_t(-5))
print("atan -6: ", atan_t(-6))
print("atan -7: ", atan_t(-7))


print("")
print("acos_t")
print("acos 0: ", acos_t(0))
print("acos 1: ", acos_t(1))
print("acos -0.707193123: ", acos_t(-0.707193123))
print("acos 0.707193123: ", acos_t(0.707193123))
print("acos 0.5: ", acos_t(0.5))
print("acos 0.25: ", acos_t(0.25))
print("acos 0.75: ", acos_t(0.75))
print("acos 0.125: ", acos_t(0.125))
print("acos 0.875: ", acos_t(0.875))
print("acos 0.0625: ", acos_t(0.0625))
print("acos 0.03125: ", acos_t(0.03125))
print("acos 0.015625: ", acos_t(0.015625))


print("")
print("sec_t")
print("sec 0: ", sec_t(0))
print("sec pi: ", sec_t(pi_t))
print("sec pi/2: ", sec_t(pi_t / 2))
print("sec pi/4: ", sec_t(pi_t / 4))

print("")
print("cot_t")
print("cot 0: ", cot_t(0))
print("cot pi: ", cot_t(pi_t))
print("cot pi/2: ", cot_t(pi_t / 2))

print("")
print("csc_t")
print("csc 0: ", csc_t(0))
print("csc pi: ", csc_t(pi_t))
print("csc pi/2: ", csc_t(pi_t / 2))
print("csc pi/4: ", csc_t(pi_t / 4))