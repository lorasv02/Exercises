import random

#list = ["apple", "cherry", "strawberry", "pear"]
mask = []
#random_word = list[random.randrange (0, len(list)-1)]

counter = 0

random_word = "apple"

for n in random_word:
        mask.append("_")

while "_" in mask:

    print (mask)
    
    letter = input ("Please, select a letter")
    found = False

    if letter in mask:
        print ("This letter already exists.")
        continue

    for index in range (0, len(random_word)):
        if letter == random_word[index]:
            mask[index] = letter
            found = True                 

    if not found:                                 
        counter += 1 
        print (f"Wrong! You have {3-counter} attempts left!")

    if counter == 3:
        print ("Game over!")
        break

else:
     print (mask)
     print ("You win!")





