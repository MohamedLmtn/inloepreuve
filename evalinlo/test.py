from main import *
import unittest


class unitest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(True,vente_enchere.ecnchere(self,'bague',50,100))
        
    def test2(self):
        self.assertEqual(False,vente_enchere.ecnchere(self,'bague',40,12))
        
    def test3(self):
        self.assertEqual(False,vente_enchere.ecnchere(self,'bague',50,50))
    
    def test4(self):
        self.assertEqual(True,vente_enchere.ecnchere(self,'bague',50,150))
    
    def test5(self):
        self.assertEqual(False,vente_enchere.ecnchere(self,'bague',50,50))
        
    def test6(self):
        self.assertEqual(False,vente_enchere.ecnchere(self,'bague',50,60))
        
    def test7(self):
        self.assertEqual(True,vente_enchere.ecnchere(self,'bague',50,150,200))
        
    def test8(self):
        self.assertEqual(False,vente_enchere.ecnchere(self,'bague',50,100,200))
                
if __name__ == '__main__':
    unittest.main()
