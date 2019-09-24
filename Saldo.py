#inloggning
pin = 1234

userpin = int(input("Skriv in din pinkod: "))

if pin != userpin:
    exit()

menu = 0
# menu 1 insättning
# menu 2 uttag
# menu 3 avsluta
while menu != 3:
    print("Ditt saldo är: ", saldo)
    menu = int(input("Skriv ditt val(1, 2, 3): "))
    if menu == 1:
        saldo = saldo + float(input("Gör en insättning: "))
    elif menu == 2:
        print("uttag")
    else:
        print("Fel eller avslut")
