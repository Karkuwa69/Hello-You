print("Welkom bij mijn Casino game :)")
print("Wil je beginnen met spelen? \n A: Ja \n B: Nee")

answer = input()

if answer == "A":
   print("Kies de moeilijkheid \n A: Easy $2000 \n B: Medium $1000 \n C: Hard $200")
   difficulty = input()
elif answer == "B":
   print("Oké, doei!")

if difficulty == "A":
   print("Je hebt Easy gekozen! Hier is je $2000!")
if difficulty == "B":
   print("Je hebt Medium gekozen! Hier is je $1000!")
if difficulty == "C":
   print("Je hebt Hard gekozen! Hier is je $200!")