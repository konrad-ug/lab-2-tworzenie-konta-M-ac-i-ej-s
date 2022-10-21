class Konto:
    def __init__(self,imie,nazwisko,pesel,kod_promocyjny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.kod_promocyjny = kod_promocyjny
        if(self.kod_promocyjny != None):
            if(self.kod_promocyjny[0:5] == "PROM_" and len(self.kod_promocyjny) == 8 and int(self.pesel[0:2])>60):
                self.saldo = 50
            else:
                self.saldo = 0     
        else:
            self.saldo = 0

