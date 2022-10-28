import unittest

from ..Konto_firmowe import KontoFirmowe

from ..Konto import Konto

class TestCheckBankTransfer(unittest.TestCase):       

    def first_transfer_to(self):
          konto = Konto("Dariusz", "Januszewski",
                               "02252807357",2000, "PROM_3742")
          konto.transferTo(500)                     
          self.assertEqual(konto.saldo, 2000-500, "niepoprawna kwota")

    def first_transfer_from(self):
          konto = Konto("Dariusz", "Januszewski",
                               "02252807357",2000, "PROM_3742")
          konto.transferFrom(500)                     
          self.assertEqual(konto.saldo, 2000+500, "niepoprawna kwota")

    def wrong_amont_transfer(self):
          konto = Konto("Dariusz", "Januszewski",
                               "02252807357",0, "PROM_3742")
          konto.transferTo(500)                     
          self.assertEqual(konto.saldo, 100, "Przelew sie wykonal")

    def set_of_transfers(self):
          konto = Konto("Dariusz", "Januszewski",
                               "02252807357",2000, "PROM_3742")                           
          konto.transferTo(500)
          konto.transferFrom(1000)
          konto.transferTo(1000)
          konto.transferFrom(2000)
          self.assertEqual(konto.saldo, 2000+500+1000-1000+2000, "Przelew sie wykonal")    

    def express_tranfer(self):
          konto = Konto("Dariusz", "Januszewski",
                               "02252807357",2000, "PROM_3742")
          konto.transferTo(500,True)                     
          self.assertEqual(konto.saldo, 2000-501, "niepoprawna kwota")
          konto.transferTo(1499,True)
          self.assertEqual(konto.saldo, 1499-1500, "niepoprawna kwota")



    # Testing Company Tranfers      
    def first_transfer_to(self):
          konto = KontoFirmowe("Ada", "0225280735", 2000)
          konto.transferTo(500)                     
          self.assertEqual(konto.saldo, 2000-500, "niepoprawna kwota")

    def first_transfer_from(self):
          konto = KontoFirmowe("Ada", "0225280735", 2000)
          konto.transferFrom(500)                     
          self.assertEqual(konto.saldo, 2000+500, "niepoprawna kwota")

    def wrong_amont_transfer(self):
          konto = KontoFirmowe("Ada", "0225280735", 0)
          konto.transferTo(500)                     
          self.assertEqual(konto.saldo, 0, "Przelew sie wykonal")

    def set_of_transfers(self):
          konto = KontoFirmowe("Ada", "0225280735", 2000)                          
          konto.transferTo(500)
          konto.transferFrom(1000)
          konto.transferTo(1000)
          konto.transferFrom(2000)
          self.assertEqual(konto.saldo, 2000+500+1000-1000+2000, "Przelew sie wykonal")   
            
    def express_tranfer(self):
          konto = KontoFirmowe("Ada", "0225280735", 2000)
          konto.transferTo(500,True)                     
          self.assertEqual(konto.saldo, 2000-505, "niepoprawna kwota")
          konto.transferTo(1495,True)
          self.assertEqual(konto.saldo, 1495-1500, "niepoprawna kwota")       