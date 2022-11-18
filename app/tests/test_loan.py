import unittest
from ..Konto import Konto

class TestLoan(unittest.TestCase):
    def test_loan_positive(self):
        konto = Konto("Darek", "Maciborek", "02252807358")
        konto.saldo = 400
        konto.historia = [200,20,100,400,40]
        self.assertEqual(konto.takeLoan(200), True, "Kredyt nie został udzielony!")
        self.assertEqual(konto.saldo, 600, "nie poprawna suma pieniedzy")

    def test_loan_negative1(self):
        konto = Konto("Darek", "Maciborek", "02252807358")
        konto.saldo = 400
        konto.historia = [200,-20,100,400,40]
        self.assertEqual(konto.takeLoan(200), False, "Kredyt został udzielony!")    
        self.assertEqual(konto.saldo, 400, "nie poprawna suma pieniedzy")

    def test_loan_negative2(self):
        konto = Konto("Darek", "Maciborek", "02252807358")
        konto.saldo = 400
        konto.historia = [100,400,40]
        self.assertEqual(konto.takeLoan(200), False, "Kredyt został udzielony!")
        self.assertEqual(konto.saldo, 400, "Kredyt został udzielony!")       

    def test_loan_negative3(self):
        konto = Konto("Darek", "Maciborek", "02252807358")
        konto.saldo = 140
        konto.historia = [10,10,10,10,10]
        self.assertEqual(konto.takeLoan(200), False, "Kredyt został udzielony!")    
        self.assertEqual(konto.saldo, 140, "nie poprawna suma pieniedzy")        
 
