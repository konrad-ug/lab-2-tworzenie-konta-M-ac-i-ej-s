import unittest

from app.Konto_firmowe import KontoFirmowe
from app.Konto import Konto
from unittest.mock import patch


class TestHistory(unittest.TestCase):
    def test_combined_transfer(self):
        konto = Konto("Darek", "Maciborek", "02252807358")
        konto.saldo = 400
        konto.transferFrom(100)
        konto.transferTo(400)
        konto.transferTo(20, True)
        self.assertEqual(
            konto.historia, [-21, -400, 100], "Niepoprawna historia przelewów!")

    @patch('app.Konto_firmowe.KontoFirmowe.is_nip_real')
    def test_combined_transfer_company(self, mock_is_nip_real):
        mock_is_nip_real.return_value = True
        konto = KontoFirmowe("Kostrzyn", "1234567890")
        konto.saldo = 400
        konto.transferFrom(100)
        konto.transferTo(400)
        konto.transferTo(20, True)
        self.assertEqual(
            konto.historia, [-25, -400, 100], "Niepoprawna historia przelewów!")
