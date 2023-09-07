#1. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural #daca este numar intreg mai mare ca 0)


y = -45
if type(y) == int and y>0:
    print(f'numarul {y} este natural')
else :
    print(f'numarul {y} nu este natural')


#2. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru


x = 2.5
if x > 0:
    print(f"numarul {x} este pozitiv")
elif x == 0:
    print(f"numarul {x} este neutru")
else:
    print(f'numarul {x} este negativ')


#3. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = 22

if -2 <= x <= 13:
    print(f'numarul {x} este cuprins intre -2 si 13')
else:
    print(f'numarul {x} nu este cuprins intre -2 si 13')


#4. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
#cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
#abs


x = 1
y = 6
if(abs(x - y)) < 5:
    print(f"diferenta dintre {x} si {y} este mai mica decat 5")

elif(abs(x - y)) == 5:
    print(f"diferenta dintre {x} si {y} este egala cu 5")

else: print(f"diferenta dintre {x} si {y} este mai mare decat 5")


#5. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

x = 22
if not( 5 <= x <= 27):
    print(f'numarul {x} nueste cuprins intre 5 si 27')
else:
    print(f'numarul {x} este cuprins intre 5 si 27')


#6. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
#daca nu, afiseaza care din ele este mai mare


y = 21
if y == x:
    print(f'numerele {x} si {y} sunt egale')
elif y > x:
    print(f'numerele {x} si {y} nu sunt egale iar numarul {y} este mai mare ca numarul {x}')
else:
    print(f'numerele {x} si {y} nu sunt egale iar numarul {y} este mai mic ca numarul {x}')


#7. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
#triunghiul este isoscel (doua laturi sunt egale),echilateral (toate laturile sunt egale) sau
#oarecare (nicio latura nu e egala).


x = 2
y = 4
z = 3

if x == y == z:
    print('triunghiul este echilateral')
elif x == y or x == z or z == y:
    print('triungiul este isoscel')
else:
    print("nici o latura a triunghiului nu este egala")

#8. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
#Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = input("introdu o litera")
vocale = 'aAeEiIoOuU'

if litera in vocale:
    print(f'litera {litera}  este o vocala')
else:
    print(f"litera {litera} nu este o vocala")


#9. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
#a. Peste 9 => A
#b. Peste 8 => B
#c. Peste 7 => C
#d. Peste 6 => D
#e. Peste 4 => E
#f. 4 sau sub => F


nota = float(input("Introdu o nota in sistem romanesc"))
if 9 < nota <= 10:
    print("ai luat nota A in sistem american")
elif 8 < nota <= 9:
    print("ai luat nota B in sistem american")
elif 7 < nota <= 8:
    print("ai luat nota C in sistem american")
elif 6 < nota <= 7:
    print("ai luat nota D in sistem american")
elif 4 < nota <= 7:
    print("ai luat nota E in sistem american")
elif 1 <= nota <= 4:
    print("ai luat nota F in sistem american")
else :
    print("nu ai introdus un numar intre 1 si 10")


#10. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)


x = int(input('introdu un numar'))

x_str = str(abs(x))

if len(x_str) >= 4:
    print(f'numarul {x} are minim 4 cifre')
else:
    print(f'numarul introdus are {len(x_str)} cifre')


#11. Verifica daca x are exact 6 cifre


x = int(input('introdu un numar'))

x_str = str(abs(x))

if len(x_str) == 6:
    print(f'numarul {x} are exact 6 cifre')
else:
    print(f'numarul {x} nu are exact 6 cifre, ci are {len(x_str)} cifre')


#12. Verifica daca x este numar par sau impar


x = int(input("introdu un numar"))

if x % 2 == 0:
    print(f' numarul {x} este par')
else:
    print(f'numarul {x} este impar')


#13. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele


x = int(input("Introduceți valoarea lui x: "))

y = int(input("Introduceți valoarea lui y: "))

z = int(input("Introduceți valoarea lui z: "))

cel_mai_mare_numar = x

if y > cel_mai_mare_numar:
    cel_mai_mare_numar = y
if z > cel_mai_mare_numar:
    cel_mai_mare_numar = z

print(f"Cel mai mare număr dintre {x}, {y} și {z} este: {cel_mai_mare_numar}")



