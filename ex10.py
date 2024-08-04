word = input("Enter a word: ")
n = int(input("Enter a number: "))
if word == "good" and 7 <= n <= 15:
    print("It's good")
elif word == "bad" and (n < 7 or n > 15):
    print("It's bad")
else:
    print("Conditions not met")