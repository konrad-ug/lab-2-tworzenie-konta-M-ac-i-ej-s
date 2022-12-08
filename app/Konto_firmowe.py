from .Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, company_name, NIP):
        self.company_name = company_name
        self.saldo = 0
        self.historia = []
        if(len(NIP) != 10):
            self.NIP = "Niepoprawny NIP!"
        else:
            self.NIP = NIP

    def transferTo(self, amount, express=False):
        if(amount <= self.saldo):
            if(express == True):
                self.saldo -= amount+5
                self.historia.insert(0, -amount-5)
            else:
                self.saldo -= amount
                self.historia.insert(0, -amount)

    def transferFrom(self, amount):
        return super().transferFrom(amount)
