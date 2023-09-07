#1.Variabila= o cutiuta din memorie in care stocam valori, aceasta este creata in momentul in care ii atribuim o valoare

#2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
#variabilă :

#- string 3333
#- int
#- float
#- bool


masina = "Audi"        #string
anFabricatie = 2002    #int
motor = 2.5            #float
defecta = False        #bool


#3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.


print(type(masina))
print(type(anFabricatie))
print(type(motor))
print(type(defecta))

#4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în #aceeași variabilă (suprascriere):
#- Verifică tipul acesteia.


motor = round(motor)
print(type(motor))
print(motor)

#5. Folosește print() și printează în consola o propoziție folosind cele 4 variabile.


print(f'Am in gara o masina {masina} din {anFabricatie} cu motor de {motor} litrii. Daca m-ai intreba daca masina este defecta, ti-as raspunde, {defecta}')

#6. Citește de la tastatură:
#- numele;
#- prenumele.
#Afișează: 'Numele complet are x caractere'.


nume =input("introdu numele")
prenume = input("introdu prenumele")
nr_caractere = len(nume + prenume)
print(f'numele introdus este {nume} {prenume} si are {len(nume + prenume)} caractere')

#7. Citește de la tastatură:
#- lungimea;
#- lățimea.
#Afișează: 'Aria dreptunghiului este x'.

lungime = float(input("introdu lungime"))
latime = float(input("introdu latimea"))
aria = lungime * latime
print(f'Aria dreptunghiului este {aria}')

#8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#- afișează de câte ori apare cuvântul 'the';

string = 'Coral is either the stupidest animal or the smartest rock'
print(string.count(' the'))

#9. Același string.
#● Afișează de câte ori apare cuvântul 'the';
#● Printează rezultatul.

string = 'Coral is either the stupidest animal or the smartest rock'
cuvant = " the"
print(string.count(' the'))
print(f'Cuvantul "the" apare in propozitia de mai sus de {string.count(cuvant)} ori')

#10. Același string.
#● Folosiți un assert ca să verificați dacă acest string conține doar numere.

string = 'Coral is either the stupidest animal or the smartest rock'
assert string.isnumeric(), "stringul nu are doar numere"
print("Sirul are doar numere")

#11 Exercițiu:
#- citește de la tastatură un string de dimensiune impară;
#- afișează caracterul din mijloc.

string = input("introdu un string de dimensiune impara")

last_index=len(string)-1
numarimpar= last_index/2
numarimpar=int(numarimpar)
print(string[numarimpar])

#12 Folosind assert, verifică dacă un string este palindrom.

cuvant=input('Introdu un cuvant')
assert cuvant == cuvant[::-1], "nu este palindrom"
print('Este palindrom')

#13 Folosind o singură linie de cod :
#- citește un string de la tastatură (ex: 'alabala portocala');
#- salvează fiecare cuvânt într-o variabilă;
#- printează ambele variabile pentru verificare.

string = input("introdu un string").split()
print(string)

#14.Exercițiu:
#- citește un user de la tastatură;
#- citește o parolă;
#- afișează: 'Parola pt user x este ***** și are x caractere';
#- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
#afișeze corect.

user = input("introdu un user")
password = input('introdu o parola')

lungimea_parolei = '*' * len(password)

print(f"Parola pentru utilizatorul {user} este {lungimea_parolei} și are {len(password)} caractere.")


