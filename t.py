# oName = "Jacques"
# oName2 = "Marie"


# print(oName + ":")
# print("Salut!")

# print(oName2 +": ")
# print("Salut")

# print(oName + ": ")
# print("Tu vas bien?")

# print(oName2 + ": ")
# print("Oui merci")

# VARIABLES

# oName = "10"
# oInt2 = 10

# str()
# int()

# print (int(oName) + oInt2)


# CONDITIONS 

# oName = "Marie"

# if oName == "Pierre":
#     print("Victoire!!!")
# elif oName == "Marie":
#     print("Victoire encore")
# else:
#     print("echec")

# EXERCICE

# oAge = int(input("Quele âge avez-vous? "))

# if oAge >= 18:
#     print("Bravo vous êtes majeur")
# elif oAge <18:
#     print("Dommage vous êtes mineur !!!")

# BOUCLES

# oName = "Pierre"

# for i in range(0,len(oName)):
#     print(oName[i])


# oInput = ""

# while oInput !="o":
#     oInput = input("Voulez-vous quitter le programme ? o/n ")

#     print("Bravo, vous avez quitter le programme")

    # LISTES

# oNameList = ["Pierre", "Paul", "Jacques"]
# oInt = [0,2,5,9]

# for item in oNameList:
#     print(item)

# oNameList = ["Pierre", "Paul", "Jacques"]
# print(oNameList[0][2])

# oNameList = ["Pierre", "Paul", "Jacques"]

# oNameList.append ("Marie")

# print(oNameList)

# oNameList = ["Pierre", "Paul", "Jacques"]

# oNameList.insert (1, "Marie")

# print(oNameList)


# oNameList = ["Pierre", "Paul", "Jacques"]

# oNameList.remove ("Pierre")

# print(oNameList)

# oNameList = ["Pierre", "Paul", "Jacques"]

# oNameList.pop(1)

# print(oNameList)
 
# oNameList = ["Pierre", "Paul", "Jacques"]

# oNameList.reverse()

# print(oNameList)


# oNameList = [0,50,12,89,13]

# oNameList.sort()

# print(oNameList)

# PROGRAMME 

"""
- récupérer ce que saisit l'utilisateur
- vérifier si l'utilisateur a bien saisit un nombre
- si oui, continuer, afficher la table de multiplication, et demander à l'utilisateur s'il souhaite quitter le programme
- si non, arrêter la boucle et demander à l'utilisateur de saisir un nombre

"""
    oQuitter = ""

    while oQuitter != "o":

        oInput = input("Svp, entrez un nombre : ")
        

        oBool = oInput.isdigit()

        if oBool:
            oInput = int(oInput)
                for i in range(0,11):
                    print(str(i) +"*" + str(oInput) + "=" + str(i*oInput))

                oQuitter = input("Voulez-vous quitter ? o/n ")


        elif oBool == False:
            print("Erreur, vous n'avez pas entré de nombre !")