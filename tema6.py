#1.Clasa Cerc
#Atribute: raza, culoare
#Constructor pentru ambele atribute
#Metode:
#● descrie_cerc() - va PRINTA culoarea și raza
#● aria() - va RETURNA aria
#● diametru()
#● circumferinta()


class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
       print(f'Cercul are raza de {self.raza} cm si culoare {self.culoare}')

    def aria(self):
       return f'Cercul are aria de {3.14 * self.raza * self.raza} cm'

    def diametru(self):
        return f'Cercul are diametrul de {self.raza * 2} cm'

    def circumferinta(self):
        return f'Cercul are circumferinta de {(2 * 3.14 * self.raza)} cm'


cerc = Cerc(5 , 'Alb')
cerc.descrie_cerc()
print(Cerc.aria(cerc))
print(Cerc.diametru(cerc))
print(Cerc.circumferinta(cerc))


#2. Clasa Dreptunghi
#Atribute: lungime, latime, culoare
#Constructor pentru toate atributele
#Metode:
#● descrie()
#● aria()
#● perimetrul()
#● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
#Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si culoarea {self.culoare}')

    def aria_dreptunghi(self):
        print(f'Aria dreptunghiului este {self.latime * self.lungime} cm')

    def perimetru_dreptunghi(self):
        print(f'Perimetrul dreptunghiului este {2 * (self.latime + self.lungime)} cm')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare



dreptunghi = Dreptunghi(10, 5, 'alb')
dreptunghi.descrie_dreptunghi()
dreptunghi.aria_dreptunghi()
dreptunghi.perimetru_dreptunghi()
dreptunghi.culoare = 'Rosu'
dreptunghi.descrie_dreptunghi()


#3. Clasa Angajat
#Atribute: nume, prenume, salariu
#Constructor pt toate atributele
#Metode:
#● descrie()
#● nume_complet()
#● salariu_lunar()
#● salariu_anual()
#● marire_salariu(procent)


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_angajat(self):
        print(f'Angajatul are numele {self.nume}, prenumele {self.prenume} si are salariul de {self.salariu} lei')

    def salariu_lunar(self):
        print(f'Angajatul are un salariu de {self.salariu} lei lunar')

    def salariu_anual(self):
        print(f'Angajatul are un salariu de {self.salariu * 12} lei anual')

    def marire_salariu(self, procent):
        self.procent = procent
        self.marire_salariu = self.salariu - self.procent/100
        print(self.marire_salariu)     # aici sunt pierdut la formula matematica




angajat = Angajat('Marincus', 'Vlad', 1000)
angajat.descrie_angajat()
angajat.salariu_lunar()
angajat.salariu_anual()
angajat.marire_salariu(100)




#4.Clasa Cont
#Atribute: iban, titular_cont, sold
#Constructor pentru toate atributele
#Metode:
#● afisare_sold() - Titularul x are în contul y suma de n lei
#● debitare_cont(suma)
#● creditare_cont(suma)


class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        self.suma = suma
        self.debitare_cont = self.sold - self.suma
        print(f'in urma debitarii {self.titular_cont} mai are in cont suma de {self.debitare_cont} lei')

    def creditare_cont(self, suma):
        self.suma = suma
        self.creditare_cont = self.sold + self.suma
        print(f'{self.titular_cont} a adaugat in cont {suma} lei iar acum are {self.creditare_cont} lei in cont')


cont = Cont('RO54XXXX', 'Vlad Marincus', 5000)
cont.afisare_sold()
cont.debitare_cont(2000)
cont.creditare_cont(1000)


