#verifica de cate ori un numar se poate divide cu 3 pana ajunge la 1

numar = 21
contor = 0
while numar >= 1:
    numar = numar / 3
    contor += 1
print(f'numarul total de iteratii este {contor}')


#cere utilizatorului sa introduca un numar de la tastatura intre un anumit interval, pana cand acesta introduce un numar corect, printeaza un mesaj

numar = int(input("introdu un numar intre intervalul 5 si 25"))
contor = 0
while numar < 5 or numar > 25:
    numar = int(input("nu ai introdus un numar intre intervalul 5 si 25, mai incearca"))
else:
    print('ai introdus un numar corect')

#adauga elemente (introduse de la tastatura) intr-o lista; daca se introduce valoare "mar", intrerupe iteratia; printeaza lista la final
#list va avea maxim 5 elemente
fructe = []
while len(fructe) < 5:
    fruct = input('introdu un fruct')
    if fruct == 'mar':
        break
    fructe.append(fruct)
print(fructe)


#avand doua numere, a si b, a fiind mai mic decat b, incrementeaza a cu 1 si decrementeaza b cu 1 pana cand cele doua numere sunt egale
#daca a devine mai mare decat b, opreste executia si printeaza un mesaj

a = 7
b = 12
while a != b:
    a += 1
    b -= 1
    if a > b:
        print('a este mai mare decat b')
        break
else:
    print('a este egal cu b')


#avand doua numere, a si b, a fiind mai mic decat b, incrementeaza a cu 1 si decrementeaza b cu 1 pana cand cele doua numere sunt egale
#daca b este mai mare decat a cu 1, incrementeaza pe a si sari peste iteratie ( skip )

a = 7
b = 12

while a != b:
    a += 1
    b -= 1
    if b == a + 1:
        a += 1
        continue
else:
    print(f' {a} este egal cu {b}')


#printeaza suma numerelor impare de la 1 la 19
sum = 0
for i in range(1, 19, 2):
    sum += i
print(sum)


#creaza o lista (folosing for) cu numere intre 4 si 50 care sunt divizibile cu 4

lista = []
for i in range (4, 50):
    if i % 4 == 0:
        lista.append(i)
print(lista)


#calculeaza si printeaza patratul fiecarui numar dintr-o lista

lista = [3, 7, 9, 12, 15]
for i in lista:
    print(i ** 2)


# printeaza fiecare numar dintr-o lista; daca un numar este mai mare decat 15 fa skip

numere = [3, 7, 9, 12, 16]
for numar in numere:
    if numar > 15:
        continue
    print(numar)


#scrie un program care printeaza fiecare caracter dintr-un string; daca caracterul e o cifra, intrerupe executia

string = 'Vlad1988'
for caracter in string:
    if caracter.isdigit():
        break
    print(caracter)


#scrie un program care printeaza fiecare caracter dintr-un string; daca caracterul nu e o litera, intrerupe executia

string = 'Vlad88'
for caracter in string:
    if not caracter.isalpha():
        break
    print(caracter)


#printeaza de cate ori apare o litera a in string

cuvinte = 'alabala portocAla'
count = 0
for litera in cuvinte.lower():
    if litera == 'a':
        count += 1
print(count)


#printeaza fiecare numar din lista pe rand, in ordine inversa

lista = [5, 7, 13, 17]
lista.reverse()
for numar in lista:
    print(numar)


#printeaza fiecare numar din lista cu urmatoarele conditii:
#numarul trebuie sa fie divizibil cu 5
#daca nr. e mai mare decat 100, treci la nr urmator
#daca nr e mai mare decat 200, opreste executia

lista = [5, 100, 20, 110, 150, 200]
for numar in lista:
    if numar > 200:
        break
    if numar > 100:
        continue
    if numar % 5 == 0:
        print(numar)
    else:
        print('conditiile nu sunt indeplinite')


#declara un numar pe care utilizatorul trebuie sa il ghiceasca introducand numere de la tastatura:
#printeaza un mesaj corespunzator:

numar = 7
numar_de_ghicit = int(input("introdu un numar"))
while numar != numar_de_ghicit:
    numar_de_ghicit = int(input("Mai incearca, introdu un numar"))
else:
    print(f"ai introdus numarul {numar}")


#printeaza indexul si valoarea dintr-o lista data

animale = ['caine', 'pisica', 'cal', 'gaina']
for i in range(0, len(animale)):
    print(f'indexul este {i} iar valoarea este {animale[i]}')


#Având lista: mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
#Folosește un for că să iterezi prin toată lista și să afișezi;
#● ‘Mașina mea preferată este x’.
#● Fă același lucru cu un for each.
#● Fă același lucru cu un while.


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

# for
for i in range (0, len(masini)):
    print (f'Masina mea preferata este {masini[i]}')

# for each
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# while
i=0
masina = len(masini)
while i < masina:
    print(f'Masina mea preferata este {masini[i]}')
    i = i+1


# Aceeași listă: masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
#Folosește un for else
#În for
#- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
#exceptând primul și ultimul.
#În else:
#- Printează lista.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(1,len(masini)-1):
       masini[i]=masini[i].upper()
else:
     print(f'Masina mea preferata este {masini} !')


# Aceeași listă:
#Vine un cumpărător care dorește să cumpere un Mercedes.
#Itereaza prin ea prin modalitatea aleasă de tine.
#Dacă mașina e mercedes:
#Printează ‘am găsit mașina dorită de dvs’
#Ieși din ciclu folosind un cuvânt cheie care face acest lucru
#Altfel:
#Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dvs')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam')


# Aceași listă;
#Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
#excepția Trabant și Lăstun.
#- Dacă mașina e Trabant sau Lăstun:
#Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
#- Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    else:
        print(f'S-ar putea să vă placă mașina {masina}')


# Modernizează parcul de mașini:
#● Crează o listă goală, masini_vechi.
#● Itereaza prin mașini.
#● Când găsesti Lăstun sau Trabant:
#- Salvează aceste mașini în masini_vechi.
#- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

#● Printează Modele vechi: x.
#● Modele noi: x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini.remove(masina)
        masini.append('Tesla')

print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')


#Având dict:
#pret_masini = {
#'Dacia': 6800,
#'Lăstun': 500,
#'Opel': 1100,
#'Audi': 19000,
#'BMW': 23000
#}
#Vine un client cu un buget de 15000 euro.
#● Prezintă doar mașinile care se încadrează în acest buget.
#● Itereaza prin dict.items() și accesează mașina și prețul.
#● Printează Pentru un buget de sub 15000 euro puteți alege mașină
#xLastun
#● Iterează prin listă.


pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(masina)

for masina, pret in pret_masini.items():
    if pret <= buget:
        print(masina,':', pret, 'euro')

for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina}.')


#7. Având lista:
#numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#● Iterează prin ea.
#● Afișează de câte ori apare 3 (nu ai voie să folosești count).


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    print(numar)

numar = 3
x = [i for i in numere if i ==numar]

print(f'Numarul 3 apare de {len(x)} ori')


# Aceeași listă:
#● Iterează prin ea
#● Calculează și afișează suma numerelor (nu ai voie să folosești sum).


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma = suma + numar
    print(f'Numarul este {suma}')
print (f'Suma numerelor este {suma}')

