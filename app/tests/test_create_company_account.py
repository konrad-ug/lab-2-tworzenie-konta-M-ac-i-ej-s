import unittest

from app.Konto_firmowe import KontoFirmowe
from unittest.mock import patch


class TestCreateBankAccount(unittest.TestCase):

    @patch('app.Konto_firmowe.KontoFirmowe.is_nip_real')
    def test_tworzenie_konta(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        pierwsze_konto = KontoFirmowe("Ada", "0225280735")
        pierwsze_konto.saldo = 0
        self.assertEqual(pierwsze_konto.company_name, "Ada",
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.NIP, "0225280735", "nie poprawny nip")

    @patch('app.Konto_firmowe.KontoFirmowe.is_nip_real')
    def test_NIP_length(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        pierwsze_konto = KontoFirmowe("Ada", "022528073")
        self.assertEqual(pierwsze_konto.NIP,
                         "Niepoprawny NIP!", "NIP jest poprawny")
