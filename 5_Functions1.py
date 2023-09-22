def demo():
    print('hello')
demo()

def demo1(name):
    print(name)
demo1('Vlad')


def demo2(name):
    return name
print(demo2('Vlad'))


def multi_param(*params):
    for param in params:
        print(param)
multi_param('mar', 'para', 'banana')


# Scrie o functie care sa accepte doi parametrii si sa returneze suma lor

def suma_numerelor(numar1, numar2):
    return numar1 + numar2
print(suma_numerelor(2, 3))


# Scrie o functie care sa accepte doi parametrii si sa returneze suma si produsul lor (foloseste funtia anterioara)

def suma_produs(a, b):
    return suma_numerelor(a, b), a*b
print(suma_produs(3, 4))


# Scrie o functie cu doi parametrii, unul dintre parametrii fiind implicit

def afiseaza_student(nume, angajat=True):
    print(f'{nume} este angajat? {angajat}')
afiseaza_student('Vlad', False)


# Scrie o functie care sa afiseze daca un nr primit ca parametru e par si impar

def par_sau_impar(numar):
    if numar % 2 == 0:
        print('numarul este par')
    else:
        print('numarul este impar')
par_sau_impar(22)


# Defineste o functie care afiseaza cate consoane si vocale are un cuvant

def consoane_vocale(cuvant):
    count_consoane = 0
    count_vocale = 0
    cuvant = cuvant.lower()
    for litera in cuvant:
        if litera in ['a', 'e', 'i', 'o', 'u']:
            count_vocale += 1
        else:
            count_consoane += 1
    print(f'cuvantul {cuvant} are {count_vocale} vocale si {count_consoane} consoane')
consoane_vocale('Alabala')


# Creaza o functie care verifica daca un string primit ca parametru este palindrom

def este_palindrom(cuvant):
    if cuvant == cuvant[::-1]:
        return 'cuvantul este palindrom'
    else:
        return 'cuvantul nu este palindrom'

print(este_palindrom('alabala'))


# Creaza o funtie care ia o lista de numere ca parametru si returneaza o noua lista doar cu numere impare

def lista_nr_impare(numere):
    lista_nr_impare = []
    for numar in numere:
        if numar % 2 != 0:
            lista_nr_impare.append(numar)
    return lista_nr_impare

print(lista_nr_impare([1, 3, 4, 5, 6, 7, 8]))


# Creaza o functie care sa verifice daca un nr dat ca parametru exista in intervalul 3 s 9

def este_nr_in_interval(numar):
    if 3 <= numar <= 9:
        print('Numarul se afla in intervalul 3 - 9')
    else:
        print('Numarul nu se afla in intervalul 3 - 9')

este_nr_in_interval(-5)


# Scrie o functie care sa calculeze numarul de litere mici si mari dintr-un string dat

def count_upper_lower(string):
    count ={
        "upper": 0,
        "lower": 0
    }
    for letter in string:
        if letter.isupper():
            count['upper'] += 1
        elif letter.islower():
            count['lower'] += 1
    return f"Numarul de litere mici este {count['lower']} si numarul de litere mari este {count['upper']}"

print(count_upper_lower('AlAbAlA!!!!'))


# Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(par_impar(3))


# Funcție care returnează numărul total de caractere din numele tău complet.
#(nume, prenume, nume_mijlociu)

def nr_caractere(nume):
    return len(nume) - nume.count(' ')

print(nr_caractere('Vlad Vlad Marincus'))


#Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(lungime, latime):
    return lungime * latime

print(aria_dreptunghiului(2, 2))


#Funcție care returnează aria cercului

def aria_cercului(raza):
    return 3.14 * (raza * raza)

print(aria_cercului(3))


#Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.

caracter = "v"
def true_false(string):
    if caracter in string:
        return True
    else:
        return False
print(true_false("Ana are mere"))




