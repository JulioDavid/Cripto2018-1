'''Implementar todas las funciones que faltan. La descripcion
   se encuentra en el pdf de la practica. Perdon por la falta de acentos.'''

def mcd(a, b):
    ''' Calcula el maximo comun divisor de a y b '''
    assert(a >= b)
    if a % b == 0:
        return b
    else:
        return mcd(b, a % b)

def xmcd(a, b):
    ''' Calcula el maximo comun divisor de a y b, ademas devuelve
        X y Y tales que mcd(a,b) = Xa + Yb '''
    assert a >= b
    if a % b == 0:
        return (b, 0, 1)
    else:
        q = a / b
        r = a % b
        d, X, Y = xmcd(b, r)
        return (d, Y, X-Y*q)

def inverso_mod(a, N):
    ''' Calcula el inverso multiplicativo de a en los enteros modulo N '''
    (d, X, Y) = xmcd(N, a)
    if d != 1:
        print str(a) + ' no tiene inverso modulo ' + str(N)
    else:
        return Y % N

def potencia_mod(a, b, N):
    ''' Calcula a^b mod N '''
    pass


def test_fermat(p):
    ''' Si p es compuesto devuelve False. Si p es primo, puede devolver True o False
        Repetir esto varias veces da mayor certeza cuando p es primo '''
    from random import randint
    a = randint(2,p-1)
    if (a**(p-1)) % p != 1: # Exponenciacion lenta a^(p-1) mod p. Cambiar por potencia_mod
        return False
    else:
        return True

def separa_dos(N):
    ''' Separa N en una potencia de 2 y un numero impar,
        es decir, devuelve (r,u) tales que N = (2^r)*u
        donde u es impar y por tanto r es lo mayor posible '''
    if N % 2 != 0:
        return (0, N)
    else:
        r,u = separa_dos(N/2)
        return r+1, u

def es_potencia(N):
    ''' Devuelve True si N es potencia de otro entero, False en otro caso '''
    pass

def test_miller_rabin(p, t=5):
    ''' Test de primalidad de Miller-Rabin '''
    pass

def genera_primo(n=20):
    pass

def genera_modulo(n=20):
    ''' Genera N = pq, un producto de primos distintos, 2^(n-1) <= p,q <= 2^n
        e = 2**16 + 1 y
        d = e^(-1) mod phi(N) '''
    pass

print separa_dos(88)
print genera_modulo(20)