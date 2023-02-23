'''Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.'''




masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for masina in masini:
  print (f'masina mea preferata este {masina}')

while masini:
    print(f'masina mea preferata este {masini.pop(0)}')



'''2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrisa cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
     print(masini)

"""3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘"""


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']


for masina in masini:
    if masina == "Mercedes":
       print('Am gasit masina dorita de dvs. Este Mercedes')
       break

    else:
        print(f'Am gasit masina {masina} mai cautam')



"""4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x."""


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
       continue

    print(f'S-ar putea sa va placa masina {masina}')

'''5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == "Lastun" or masina == "Trabant":
        masini_vechi.append(masina)
        masini.remove(masina)
        masini.append('Tesla')
print(f'modelele vechi sunt {masini}')
print(f'modelele noi sunt {masini_vechi}')

'''6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.'''

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}



for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(f'pentru un buget de sub 15000 euro puteti alege marca {masina} care are pretul de {pret} euro')

'''7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for numar in numere:
    print(numar)

numar = 3
numar3 = [i for i in numere if i ==numar]

print(f'numarul 3 apare de {len(numar3)} ori ')

'''8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
        suma = suma + numar
        print(f' numarul este {numar}')
print(f'suma numerelor este {suma}')

'''9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
cel_mai_mare_numar = 0

for i in numere:
    if i> cel_mai_mare_numar:
        cel_mai_mare_numar = i
    print(f'numarul este {i}')
print(f'cel mai mare numar de mai sus este {cel_mai_mare_numar}')


'''10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for numar in numere:
    if numar > 0:
        print(f'numarul pozitiv este numarul {numar} ')
        numar = numar * (-1)
        print(f'valoarea pozitiva a acestui numar este {numar}')






