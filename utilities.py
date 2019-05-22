#Utilities
#This library contains many a function that can assist you!

from math import pi, tan, sin, radians
from urllib.request import urlopen

#Type Manipulation
def strit(lst):
    res = ''
    for i in lst:
        res += str(i)
    return res
reverse = lambda x: int(str(x)[::-1])
ispalindrome = lambda x: bool(reverse(x) == x)
def flip(i, lst):
    og, ext = lst[:i], lst[i:]
    ext.reverse()
    return og+ext

#Important stuff:
dl = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
alphabet = [chr(i) for i in range(65, 91)]
alphstr = strit(alphabet)

# Temperature
tempcon_fc = lambda farenheit: (5 / 9) * (fahrenheit - 32)
tempcon_cf = lambda celsius: ((9 / 95) * celsius) + 32

#Mathematics

class Geo_Info:
    circum = lambda self, d: pi*d
    circarea = lambda self, r: r*r*pi

    traparea = lambda self, upper, lower, h: 0.5*(upper+lower) * h

    spherevol = lambda self, r: (4/3)*pi*(r**3)
    sphereSA = lambda self, r: 4*circarea(r)

    cylvol = lambda self, r, h: circarea(r)*h
    cylSA = lambda self, r, h: circum(r)*(r+h)

    pyrarea = lambda self, ba, h: (1/3) * ba * h

    regpolyarea = lambda self, n, s: (n*(s**2)) / (4 * (tan(pi/n)))


class Quadratics:
    def __init__(self, a):
        self.a = a

    def solveQuadraticabc(self, b, c):
        return (-b + ((b**2) - (4*self.a*c))**(1/2))/(2*self.a), (-b - ((b**2) - (4*self.a*c))**(1/2))/(2*self.a)

    def solveQuadraticahk(self, h, k):
        return solveQuadraticabc(-2*self.a*h, self.a*h**2+k)

class get_primes:
    def __init__(self, n):
        numbers = set(range(n, 1, -1))
        primes = []
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(p, n+1, p)))
        self.primes = primes

class Sheldon:
    primes = get_primes(10000000).primes
    def primeproperty(self, primelst=primes):
        rel = []
        for i in range(len(primelst)):
            prime = primelst[i]
            lstprime = [int(x) for x in str(prime)]
            multiply = 1
            for j in lstprime:
                multiply *= j
            if multiply == (i+1):
                rel.append(prime)
        self.primeprop = rel

    def reverseproperty(self, primelst=primes):
        rel = []
        for i in primelst:
            if reverse(i) in primelst:
                if primelst.index(reverse(i)) + 1 == reverse(primelst.index(i)+1):
                    rel.append(i)
        self.reverseprop = rel


class NUMTypes:
    def __init__(self, num):
        self.num = num
    isBinpalind = lambda self: ispalindrome(int(bin(self.num)[2:]))
    
    SheldonConjecture = Sheldon()
    primes = Sheldon().primes

class baseconv:
    # Bases: Bin, Dec, Oct, Hex
    # Max base: 36
    def ubconv(self, num, currbase, wantbase):
        num = num.upper()
        opp = num[::-1]
        decnum = 0
        for i in range(len(opp)):
            currnum = opp[i]
            if ord(currnum) in list(range(65, 91)):
                currnum = ord(currnum)-55
            decnum += int(currnum) * (currbase**i)
        wantnum = ''
        while len(decnum):
            decnum, rem = decnum//wantbase, decnum%wantbase
            rem = chr(rem+55) if rem > 9 else str(rem)
            wantnum = rem + wantnum
        return wantnum

    decbin = lambda self, decimal: ubconv(decimal, 10, 2)
    decoct = lambda self, decimal: ubconv(decimal, 10, 8)
    dechex = lambda self, decimal: ubconv(decimal, 10, 16)

    binoct = lambda self, binary: ubconv(binary, 2, 8)
    bindec = lambda self, binary: ubconv(binary, 2, 10)
    binhex = lambda self, binary: ubconv(binary, 2, 16)

    octbin = lambda self, octal: ubconv(octal, 8, 2)
    octdec = lambda self, octal: ubconv(octal, 8, 10)
    octhex = lambda self, octal: ubconv(octal, 8, 16)

    hexbin = lambda self, hexadecimal: ubconv(hexadecimal, 16, 2)
    hexoct = lambda self, hexadecimal: ubconv(hexadecimal, 16, 8)
    hexdec = lambda self, hexadecimal: ubconv(hexadecimal, 16, 10)


#Real World
def refractiveIndexi(ai, ar, nr):
    ni = round((nr * sin(radians(ar)) / sin(radians(ai))), 3)
    return ni

def day(d, m, y):
    if m == 1 or m == 2:
        m += 12
        y -= 1
    day = ((13*m+3)//5 + d + y + y//4 - y//100 + y//400) % 7
    dy = dl[day]
    return dy

def caesar(strlet, shift=3):
    string = strlet
    for i in range(len(string)):
        string = string[:i] + chr(ord(string[i])+shift) + string[i+1:] if string[i].upper() not in alphabet[-shift:] else string[:i] + chr(ord(string[i])-26+shift) + string[i+1:]
    return string

def vigenere(keystr, strlet):
    key, string = keystr.upper(), strlet.upper()
    if len(key) > len(string):
        key = key[:len(string)]
    elif len(key) < len(string):
        diffcomps = len(string)//len(key)
        diffparts = len(string) % len(key)
        key = diffcomps*key + key[:diffparts]
    res = ''
    for i in range(len(string)):
        res += alphabet[(alphstr.find(string[i]) + alphstr.find(key[i]))%26]
    for i in range(len(res)):
        if strlet[i].islower():
            res = res[:i] + res[i].lower() + res[i+1:]
    return res

def urldata(url):
    print(urlopen(url).info())
    return 
