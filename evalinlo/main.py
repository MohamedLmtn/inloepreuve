class vente_enchere:
        
    def ecnchere(self,nomprod : str,prixprod: int,prixenchere : int,diffprct : int = 100) -> bool:
        if (prixenchere % 10) == 0 and prixenchere > prixprod and (prixenchere*100) / prixprod > 120:
            if (((prixenchere *100)/prixprod) - 100) >= diffprct:
                return True
            else :
                return False
        else :
            return False
    