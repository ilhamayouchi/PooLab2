class CompteBancaire:
    compteur = 1

    def __init__(self, solde_initial=0.0):
        self.id = CompteBancaire.compteur
        CompteBancaire.compteur += 1
        self.__solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Solde insuffisant.")

    def get_solde(self):
        return self.__solde


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []

    def ajouter_compte(self, solde_initial=0.0):
        compte = CompteBancaire(solde_initial)
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for compte in self.comptes:
            print(f"  Compte {compte.id} | Solde : {compte.get_solde()}€")


if __name__ == "__main__":
    cli = Client("Yassir")
    cli.ajouter_compte(300)
    cli.ajouter_compte(150)
    cli.comptes[0].retirer(50)
    cli.comptes[1].deposer(200)
    cli.afficher()
