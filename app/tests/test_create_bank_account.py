import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "02252807357")
        self.assertEqual(pierwsze_konto.imie, "Dariusz",
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski",
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "02252807357",
                         "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Poprawny pesel!")

    def pesel_length_test(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "022528073571")
        self.assertEqual(pierwsze_konto.pesel,
                         "Niepoprawny pesel!", "Pesel jest poprawny")
        drugie_konto = Konto("Dariusz", "Januszewski", "022528073")
        self.assertEqual(drugie_konto.pesel,
                         "Niepoprawny pesel!", "Pesel jest poprawny")

    def promo_code_for_under_60(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski",
                               "02252807357", "PROM_374")
        self.assertEqual(pierwsze_konto.saldo, 50,
                         "Kod promocyjny aktywowany!")

    def promo_code_for_over_60(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski",
                               "59252807357", "PROM_374")
        self.assertEqual(pierwsze_konto.saldo, 0,
                         "Kod promocyjny nieaktywny dla staruchów!")

    def wrong_promo_code(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski",
                               "59252807357", "PROM_3742")
        self.assertEqual(pierwsze_konto.saldo, 0,
                         "nie prawidłowy kod")



