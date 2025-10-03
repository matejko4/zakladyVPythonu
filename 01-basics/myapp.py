
def kviz():
    print("Vítejte ve fotbalovém kvízu!")
    print("Odpovězte na následující otázky:\n")
    
    score = 0
    pocet_otazek = 6


    answer1 = input("Který tým vyhrál Mistrovství světa ve fotbale v roce 2018? ")
    if answer1.strip().lower() == "francie":
        score += 1
        print("Správně!\n")
    else:
        print("Špatně! Správná odpověď je Francie.\n")

    answer2 = input("Kdo je nejlepším střelcem v historii Ligy mistrů UEFA?(jen příjmení) ")
    if answer2.strip().lower() == "ronaldo":
        score += 1
        print("Správně!\n")
    else:
        print("Špatně! Správná odpověď je Ronaldo.\n")

    answer3 = input("Který hráč získal Zlatý míč (Ballon d'Or) nejvícekrát?(jen příjmení) ")
    if answer3.strip().lower() == "messi":
        score += 1
        print("Správně!\n")
    else:
        print("Špatně! Správná odpověď je Messi.\n")

    answer4 = input("Jaký je maximální počet hráčů jednoho týmu na hřišti během fotbalového utkání? ")
    if answer4 == "11":
        score += 1
        print("Správně!\n")
    else:
        print("Špatně! Správná odpověď je 11.\n")


    answer5 = input("""Který tým je známý jako 'The Red Devils'? 
    možnosti:
        manchester united, 
        liverpool, 
        chelsea, 
        arsenal:
    """)
    if answer5.strip().lower() == "manchester united":
        score += 1
        print("Správně!\n")
    else:
        print("Špatně! Správná odpověď je Manchester United.\n")


    answer6 = input("Co znamená nehýbající se zvednutý praporek pomezního ve fotbale? ")
    if answer6.strip().lower() == "ofside" or answer6.strip().lower() == "ofsajd":
        score += 1
        print("Správně!\n")
    else:
        print("Špatně! Správná odpověď je ofsajd.\n")


    print(f"Kvíz skončil! Váš celkový počet bodů je: {score}/{pocet_otazek}")

kviz()
