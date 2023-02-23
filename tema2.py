
#1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

# scriem "ceva" in parametrul IF iar daca acel "ceva" este adevarat o sa ne printeze rezultatul de la IF...daca nu...trece de la IF la
#ELSE si o sa ne printeze rezultatul de la ELSE.


#2. Verifica si afiseaza daca y este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)



y = 3
if type(y) == int and y >= 1:
    print("numarul este natural")

else:
    print("numarul nu este natural")



#3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = 3

if x >= 1:
    print(f"numarul {x} este pozitiv")
elif x == 0:
    print(f"numarul {x} este neutru")
else :
    print(f"numarul {x} este negativ")



#4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = 3
if x >= -2 and x <= 13:
    print(f"numarul {x} este cuprins intre -2 si 13")
else:
    print(f"numarul {x} nu este cuprins intre -2 si 13")




#5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
#cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia abs

x = 3
y = 9

if(abs(x - y)) < 5:
    print(f"diferenta dintre {x} si {y} este mai mica decat 5")

elif(abs(x - y)) == 5:
    print(f"diferenta dintre {x} si {y} este egala cu 5")

else: print(f"diferenta dintre {x} si {y} este mai mare decat 5")




# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

x =3
if not(5 <= x <=27):
    print(f"numarul {x} nu este cuprins intre numerele 5 si 27")

else:
    print(f"numarul {x} este este cuprins intre numerele 5 si 27")



#7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
#daca nu, afiseaza care din ele este mai mare

x = 3
y = 9

if x == y:
    print(f"numerele {x} si {y} sunt egale")
elif x > y:
    print(f"numerele {x} si {y} nu sunt egale iar numarul {x} este mai MARE decat numarul {y}")
else :
    print(f"numerele {x} si {y} nu sunt egale iar numarul {x} este mai MIC decat numarul {y}")



#8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

x = 3
y = 9
z = 9

if   x == y == z:
    print("triunghiul este echilateral")
elif x == y:
    print("triungiul este isoscel")
elif x == z:
    print("triungiul este isoscel")
elif y == z:
    print("triungiul este isoscel")
else :
    print("nici o latura nu este egala")


#9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
#Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = str(input("Introdu o litera"))

vocale = "AaEeIiOoUu"

if litera in vocale:
    print (f' litera {litera} este o vocala')
else:
    print(f" litera {litera} nu este o vocala")


#10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
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



