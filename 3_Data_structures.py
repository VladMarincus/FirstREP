#1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#a. Afiseaz-o
#b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
#varianta actuala (inversata)
#c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
#inverseze ordinea si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
#varianta inițială

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

note_muzicale_invers = note_muzicale[::-1]
print(note_muzicale_invers)

note_muzicale_invers.reverse()
print(note_muzicale)


#2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.


note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale.count("do"))


#3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2 #varianta1
print(lista3)
lista1.extend(lista2)
print(lista1)


#4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
#folosind o functie si apoi afiseaza din nou lista


lista3.sort()
print(lista3)
lista3.pop(0)
print(lista3)


#5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
#- Lista este goala (IF)
#- Lista nu este goala (ELSE)


if len(lista3) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')


#6. Foloseste o functie care sa goleasca lista de la exercitiul 3


lista3.clear()
print(lista3)


#7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
#afiseze ca lista e goala


if len(lista3) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')


#8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
#afisezi Elevii (cheile)


dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5,
        }

elevi = dict1.keys()
print(elevi)


#9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
#Ex: ‘Ana a luat nota {x}’.
#Doar nota o vei lua folosindu-te de cheie


print(f'Ana a luat nota {dict1["Ana"]}.')
print(f'Gigel a luat nota {dict1["Gigel"]}.')
print(f'Dorel a luat nota {dict1["Dorel"]}.')


#10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
#- Modifica nota lui Dorel in 6
#- Printeaza nota lui dupa modificare


dict1['Dorel'] = 6
print(dict1)


#11. Imagineaza-ti ca Gigel se transfera din clasa.
#- Cauta o functie care sa il stearga
#Vine un coleg nou.
#- Adaugati-l in lista pe Ionica, cu nota 9
#- Printati dictionarul cu noii elevi


dict1.pop('Gigel')
print(dict1)

dict1['Ionica'] = 9
print(dict1)


#12. Ai urmatoarele seturi:
#zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
#- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

#zile_sapt.add('luni')
print(zile_sapt)   # structurile de date de tip set nu pot contine 2 item-uri cu aceeasi valoare; valorile duplicate sunt ignorate


#13. Foloseste un if si verifica daca:
#- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
#regasesc intre elementele din setul zile_sapt)
#- Weekend nu este un subset al zilelor din sapt
#Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
#punct de mai sus va fi un boolean


if weekend.issubset(zile_sapt):
    print(f'zielele : {weekend} se regasesc in zielele : {zile_sapt}')
else:
    print(f'zielele : {weekend} nu se regasesc in zielele : {zile_sapt}')


#14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
#sunt in weekend si invers)

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

print(zile_sapt.difference(weekend))

#15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
#ambele seturi). Hint: Va puteti folosi de o functie

print(zile_sapt.intersection(weekend))