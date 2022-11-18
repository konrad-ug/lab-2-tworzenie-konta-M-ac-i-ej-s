import unittest
from ..Konto import Konto

class TestLoan(unittest.TestCase):

    def setUp(self):
        self.konto = Konto("Darek", "Maciborek", "02252807358")
        
    @parameterized([
    ([200,20,100,400,40], 200, True, 200),
    ([200,-20,100,400,40], 200, False, 0),
    ([100,400,40], 200, False, 0),
    ([10,10,10,10,10], 200, False, 0),
    ])
    def test_pow(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        self.assertEqual(self.konto.takeLoan(kwota), oczekiwany_wynik, "Kredyt nie został udzielony!")
        self.assertEqual(self.konto.saldo, oczekiwane_saldo, "nie poprawna suma pieniedzy")

