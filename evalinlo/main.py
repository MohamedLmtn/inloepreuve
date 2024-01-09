class vente_enchere:
        
    def enchere(self,nomprod : str,prixprod: int,prixenchere : int,diffprct : int = 100) -> bool:
        if (prixenchere % 10) == 0 and prixenchere > prixprod and (prixenchere*100) / prixprod > 120:
            if (((prixenchere *100)/prixprod) - 100) >= diffprct:
                return True
            else :
                return False
        else :
            return False
        

    def offres(self,name : str = None,prix : int = None):
        lstoffre = {"bague or":100,"bracelet":120}

        if name in lstoffre.keys() or prix in lstoffre.values():
            return True
        else :
            return False
        
    

