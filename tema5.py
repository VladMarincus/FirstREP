#1.Funcție care să calculeze și să returneze suma a două numere

def suma(nr1 , nr2):
    return nr1 + nr2

print(suma(1 , 2))

#2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def par_impar(numar):

    if numar % 2 == 0:
         print(True)
    else:
         print(False)

par_impar(4)

#3. Funcție care returnează numărul total de caractere din numele tău complet.
#(nume, prenume, nume_mijlociu)

def nr_caractere(nume):
    return len(nume) - nume.count(' ')

print(nr_caractere('Vlad Marincus'))

#4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(lungime, latime):
    return lungime * latime

print(aria_dreptunghiului(2, 5))

#5. Funcție care returnează aria cercului      aria cercului este  3.14 * (raza * raza)

def aria_cercului(pi, raza):
    return pi * (raza * raza)

print(aria_cercului(3.14, 3))

#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

caracter = 'v'
def true_false(string):
    if caracter in string:
        print(True)
    else:
        print(False)

true_false("vlad")

#7. Funcție fără return, primește un string și printează pe ecran:
#● Nr de caractere lower case este x
#● Nr de caractere upper case exte y'''

def upper_lower(string):
    caracter_lower = 0
    caracter_upper = 0

    for caracter in string:
        if caracter.isupper():
           caracter_upper +=1
        elif caracter.islower():
            caracter_lower +=1
    print(f'Avem {caracter_upper} caractere upper si {caracter_lower} caractere lower')

upper_lower('VVlad')

#8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive


def lista_numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive

print(lista_numere_pozitive([1,2,3,4, -3, -4]))

#9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
#● Primul număr x este mai mare decat al doilea nr y
#● Al doilea nr y este mai mare decat primul nr x
#● Numerele sunt egale.


def numere(numar1, numar2):
    if numar1 > numar2:
        print('numar1 este mai mare decat numar2')
    elif numar1 < numar2:
        print('numar2 este mai mare decat numar1')
    else:
        print('numerele sunt egale')

numere(2,2)

#10. Funcție care primește un număr și un set de numere.
#● Printeaza ‘am adaugat numărul nou în set’ + returnează True
#● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
#returnează False


def numere(numar, set_numar):
    if numar in set_numar:
        print('nu am adaugat numărul în set. Acesta există deja')
        return print(False)
    else :
        set_numar.add(numar)
        print('am adaugat numărul nou în set')
        return print(True)

numere(2, {1, 3, 4})
