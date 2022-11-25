import unittest

from app.Rejerstr_kont import RejestrKont
from app.Konto import Konto


class TestCreatingAcc(unittest.TestCase):
    imie = "Bogdan"
    nazwisko = "Kalaszenko"
    pesel = "02252807313"

    @classmethod
    def setUpClass(cls):
        konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.addUser(konto)

    def test_1_dodawanie_pierwszego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto1 = Konto(self.imie + "ddd", self.nazwisko, self.pesel)
        RejestrKont.addUser(konto)
        RejestrKont.addUser(konto1)
        self.assertEqual(RejestrKont.howManyUsers(), 3)

    def test_2_dodawanie_drugie_konto(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.addUser(konto)
        self.assertEqual(RejestrKont.howManyUsers(), 4)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.users = []        