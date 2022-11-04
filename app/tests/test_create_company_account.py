import unittest

from ..Konto_firmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoFirmowe("Ada", "0225280735")
        self.assertEqual(pierwsze_konto.company_name, "Ada",
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.NIP, "0225280735", "nie poprawny nip")

    def test_NIP_length(self):
        pierwsze_konto = KontoFirmowe("Ada", "022528073")
        self.assertEqual(pierwsze_konto.NIP,
                         "Niepoprawny NIP!", "NIP jest poprawny")   

    