print ("Hello You!, ik ben Pawel!")
print ("Wie ben jij?")

username = input("")
print("Mijn naam is " + username)

print("Hello " + username)

import datetime
x = datetime.datetime.now()

print(x)

answer = input(username + " wil jij dit programma nog een keer doen? Type Ja/Nee:")
if answer == "Ja":
      print("Restart de programma")
elif answer == "Nee":
      print("Oke, Doei!")
else:
   print(username + " dankjewel voor het gebruiken van mijn programma!")
