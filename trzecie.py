question1 = "Jakie jest twoje ulubione zwierzę?"
answers1 = ["Kot", "Pies", "Koń", "Ryba"]
question2 = "Jaką muzykę najczęściej słuchasz?"
answers2 = ["Rock", "Pop", "Hip hop", "Klasyczna"]
question3 = "Jakie jest twoje ulubione danie?"
answers3 = ["Pizza", "Sushi", "Spaghetti", "Burger"]

name = input("Podaj swoje imię i nazwisko: ")
print(f"Witaj {name}! Odpowiedz na poniższe pytania jednym z dostępnych wyborów:")

print(question1)
print("1. " + answers1[0])
print("2. " + answers1[1])
print("3. " + answers1[2])
print("4. " + answers1[3])
choice1 = int(input("wybierz odpowiedź (podaj numer): "))

print(question2)
print("1. " + answers2[0])
print("2. " + answers2[1])
print("3. " + answers2[2])
print("4. " + answers2[3])
choice2 = int(input("Wybierz odpowiedź (podaj numer): "))

print(question3)
print("1. " + answers3[0])
print("2. " + answers3[1])
print("3. " + answers3[2])
print("4. " + answers3[3])
choice3 = int(input("Wybierz odpowiedź (podaj numer): "))

print("\nDziękujemy za wypełnienie ankiety!")
print("Twoje odpowiedzi to:")
print("1. " + question1 + " - " + answers1[choice1-1])
print("2. " + question2 + " - " + answers2[choice2-1])
print("3. " + question3 + " - " + answers3[choice3-1])
