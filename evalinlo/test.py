from main import *
import unittest


class unitest(unittest.TestCase):
    
    def test1diffprixenchereproduit(self):
        self.assertEqual(True,vente_enchere.enchere(self,'bague',50,100))
        
    def test2diffprixenchereproduitmoin(self):
        self.assertEqual(False,vente_enchere.enchere(self,'bague',50,40))
        
    def test3multiple10(self):
        self.assertEqual(False,vente_enchere.enchere(self,'bague',40,56))
        
    def test4multiple10true(self):
        self.assertEqual(False,vente_enchere.enchere(self,'bague',40,50))
        
    def test5plupourcentenchere(self):
        self.assertEqual(False,vente_enchere.enchere(self,'bague',50,70))
        
    def test6moinpourcentenchere(self):
        self.assertEqual(False,vente_enchere.enchere(self,'bague',50,60))
        
    def test7plu100poucent(self):
        self.assertEqual(True,vente_enchere.enchere(self,'bague',50,150,200))
        
    def test8moin100pourcent(self):
        self.assertEqual(False,vente_enchere.enchere(self,'bague',50,100,200))
        
    def test9(self):
        self.assertEqual("name only",vente_enchere.offres(self,name="bague or"))

    def test10(self):
        self.assertEqual("prix only",vente_enchere.offres(self,prix=100))
    
    def test12(self):
        self.assertEqual("name prix",vente_enchere.offres(self,name="bague or",prix=100))

    def test13(self):
        self.assertEqual(False,vente_enchere.offres(self,"test",666))
            

                
if __name__ == '__main__':
    unittest.main()
