class CompteBancaire:
    def __init__(self,titulaire,solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []
    @property
    def solde(self):
        return self.__solde
    @solde.setter
    def solde(self,montant):
        if montant < 0:
            raise ValueError("Solde négatif interdit")
        self.__solde = montant
    def deposer(self,montant):
        if montant <0:
            print("Invalide")
        else:
            self.__solde +=montant
        self._operations.append(f"Dépôt : +{montant} MAD")
    def retirer(self,montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Insuffisant")
        self._operations.append(f"Retirer : -{montant} MAD")
    def __str__(self):
        return f"titulaire:{self._titulaire}, solde :{self.__solde} MAD"
    def afficher_historique(self):
        for h in self._operations:
            print("-",h)


#Classe Drivé
class CompteEpargne (CompteBancaire):
    def __init__(self,titulaire,solde_initial,taux_annuel):
        super().__init__(titulaire,solde_initial)
        self.taux_annuel=taux_annuel

    def calculer_interet(self):
        interet = self.solde *self.taux_annuel/100
        self.deposer(interet)
        self._operations.append(f"Intérêt annuel ({self.taux_annuel}%) : +{interet} MAD")

if __name__ == "__main__":
    compte = CompteEpargne("Ali", 1000,2)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)
    compte.calculer_interet()
    # Tentative de modification directe
    compte.solde = 500  # Ne fonctionnera pas
    compte.afficher_historique()
    a = "entrer"
    print(a)