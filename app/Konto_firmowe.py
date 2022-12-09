from .Konto import Konto
from datetime import date
import requests
import os

class KontoFirmowe(Konto):
    def __init__(self, company_name, NIP):
        self.company_name = company_name
        self.saldo = 0
        self.historia = []

        if(len(NIP) != 10 and self.is_nip_real(NIP) == False):
            return False
        else:
            self.NIP = NIP

    def is_nip_real(self,NIP):
            today_date = date.today()
            today = today_date.strftime("%Y-%m-%d")

            response = requests.get(f"${os.environ.get('BANK_APP_MF_URL.')}/${NIP}?date=${today}"
            )

            if (response.status_code == 200):
                return True
            else:
                return False

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
