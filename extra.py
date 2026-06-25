# V1 Gestionnaire de contact en python 
# ajouter, modifier, supprimer, afficher les contacts
#Rechercher un contact par nom ou par numéro de téléphone
import re


# Dictionnaire des contacts : en gros c'est la liste des contacts 
liste_contact = {}

# Normalisation simple pour éviter les erreurs de saisies
def normaliser_numero(numero):
    return re.sub(r"\D", "", numero)

# Pour ajouter un contact en entrant deux paramètres : le nom et le numéro
def ajouter_contact(nom, numero):
    numero = normaliser_numero(numero)
    liste_contact[nom] = numero
    print(f"Contact '{nom}' ajouté avec succès !")

# Modifier le contact en entrant de nouvelles informations sur un contact déjà existant 
def modifier_contact(nom, nouveau_numero):
    if nom in liste_contact:
        liste_contact[nom] = normaliser_numero(nouveau_numero)
        print(f"Contact '{nom}' modifié avec succès !")
    else:
        print(f"Le contact '{nom}' n'existe pas.")

# Supprimer un contact en entrant le nom et le num du contatc 
def supprimer_contact(nom):
    if nom in liste_contact:
        del liste_contact[nom]
        print(f"Contact '{nom}' supprimé avec succès !")
    else:
        print(f"Le contact '{nom}' n'existe pas.")

# Afficher la liste des contacts sous la forme d'un dict 
def afficher_contact():
    if not liste_contact:
        print("Aucun contact enregistré.")
        return
    print("\n📒 Liste des contacts :")
    for nom, numero in liste_contact.items():
        print(f"- {nom} : {numero}")
    print()

# Recherche de contact en fonction de critères entrés par l'utilisateur
def rechercher_contact(critere):
    critere = critere.lower()
    resultat = {}
    # Recherche dans la liste de conatct en fonction des crutères (nom,num)
    for nom, numero in liste_contact.items():
        if critere in nom.lower() or critere in numero:
            resultat[nom] = numero

    if resultat:
        print("\n🔍 Résultats de la recherche :")
        for nom, numero in resultat.items():
            print(f"- {nom} : {numero}")
    else:
        print("Aucun contact trouvé.")


# Fonction principale du programme : c'est ici que l'interface s'afficher etc...
# Et que l'on appelle les fonctions 
def main():
   # Faire tourner la boucle en boucle 
    while True:
        print("="*45)
        print("Bienvenue dans le gestionnaire de contact ! ")
        print("1. Ajouter un contact à la liste")
        print("2. Supprimer un contact de la liste")
        print("3. Modifier un contact de la liste")
        print("4. Rechercher un contact de la liste")
        print("5. Afficher les contacts ")
        print("6. Exit")
        print("="*45)
        # Pour éviter les erreurs
        try:
                    choice = int(input("Entrez votre choix (1-6) :  "))
        except ValueError:
            print("Veuillez entrer un nombre valide svp (1-6) ! ")
            continue
        # Code en fonction de la réponse de l'utilisateur 
        if choice == 1:
            nom = input("Entrez le nom du contact à ajouter : ")
            numero = input("Entrez le numéro du contact : ")
            ajouter_contact(nom=nom,numero=numero)
        elif choice == 2:
            nom_remove = input("Entrez le nom du contact à supprimer : ")
            supprimer_contact(nom=nom_remove)
        elif choice == 3:
            nom_contact = input("Entrer le nom du contact sur lequel vous voulez modifier le numéro de tel : ")
            new_num = input("Entrez le nouveau numéro de tle du contact : ")
            modifier_contact(nom=nom_contact,nouveau_numero=new_num)
        elif choice == 4:
            critere = input("Entrez le nom ou le numéro à rechercher : ")
            rechercher_contact(critere=critere)
        elif choice == 5:
            afficher_contact()
        elif choice == 6:
            print("Au revoir ! ")
            break
        else:
            print("Numéro invalide ! Veuillez entrez un choix entre 1 et 6")

main()







