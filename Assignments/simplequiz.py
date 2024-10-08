print("This is a quiz, please answer the questions as best as you can")

answer = int(input("What is a whole number that is less than 5.\n"))
print(answer < 5)

answer2 = int(input("What is a whole number that is more than 9.\n"))
print(answer2 > 9)

answer3 = int(input("What is a whole number that is equal to 6.\n"))
print(answer3 == 6 )

answer4 = int(input("What is a whole number that is less than or equal to 5.\n"))
print(answer4 <= 5)

answer5 = int(input("What is a whole number that is less than 1?\n"))
print(answer5 < 1)


def tally_score():
    score = 0
    if answer < 5:
        score = score + 1
    if answer2 > 9:
        score = score + 1
    if answer3 == 6:
        score = score + 1
    if answer4 <= 5: 
        score = score + 1
    if answer5 < 1: 
        score = score + 1
    print("your score is " + str(score) + " out of 5")

tally_score()