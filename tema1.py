# Ce este o variabila? _______________

#Declara si initializeaza cate o variabila din fiecare urmatoarele :

masina = "Audi"        #string
anFabricatie = 2002    #int
motor = 2.5            #float
defecta = False        #bool


#3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(masina))
print(type(anFabricatie))
print(type(motor))
print(type(defecta))

#4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia.

motor = round(motor)
print(motor)

#5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
#Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f"Detin o masina marca {masina} este din anul {anFabricatie} are un motor de {motor} litrii")
print(f"Acesta masina este defecta? = {defecta}")


#6. Citește de la tastatură:
#- numele;
#- prenumele.
#Afișează: 'Numele complet are x caractere'.

numele = (input("intoduceti numele"))
prenumele = (input("intoduceti prenumele"))

print(f"Numele complet are {len(numele + prenumele)} caractere")

#7. Citește de la tastatură:
#- lungimea;
#- lățimea.
#Afișează: 'Aria dreptunghiului este x'.
#aria dreptungiului = lungimea * latimea

lungimea = int(input("introduceti lungimea"))
latimea = int(input("intoduceti latimea"))

aria = lungimea * latimea
print(f"Aria dreptungiului este de {aria} metrii")


#8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#- afișează de câte ori apare cuvântul 'the';

stringul = "Coral is either the stupidest animal or the smartest rock"
print(stringul.count(" the"))   #aici ii cu smecherie pt. ca trebuie pus spatiu inainte de "the"
                                #daca nu pui spatiu iti da si the-ul din either

#9. Același string.
#Același string, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”)
stringul = "Coral is either the stupidest animal or the smartest rock"

print(stringul.replace('the', 'THE'))

#10. Același string.
#● Folosiți un assert ca să verificați dacă acest string conține doar numere.

stringul = "123"  # aici daca punem "123" o sa treaca

assert stringul.isnumeric()
print(f'Stringul {stringul} contine doar numere ')


#TEME Optionale

#1. Exercițiu:
#- citește de la tastatură un string de dimensiune impară;
#- afișează caracterul din mijloc.


impara = input("introdu un string")
print(impara[0, 1])



