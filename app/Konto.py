from datetime import date


class Konto:
    def __init__(self, imie, nazwisko, pesel,saldo=0, kod_promocyjny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.kod_promocyjny = kod_promocyjny
        self.saldo = saldo

        def peselToYear(pesel):
            if(pesel[0] == str(0)):
                year = int("20" + pesel[0:2])
            else:
                year = int("19" + pesel[0:2])
            return year

        if(len(self.pesel) != 11):
            self.pesel = "Niepoprawny pesel!"

        if(self.kod_promocyjny != None and self.saldo == 0):
            if(self.kod_promocyjny[0:5] == "PROM_" and len(self.kod_promocyjny) == 8 and peselToYear(self.pesel) >= 1960):
                self.saldo = 50
            else:
                self.saldo = 0
        else:
            self.saldo = 0

    def transferTo(self,amount,express):
        if(amount < self.saldo):
            if(express == True):
                self.saldo-=amount-1
            else:
                self.saldo-=amount        

    def transferFrom(self,amount):
        self.saldo+=amount   

