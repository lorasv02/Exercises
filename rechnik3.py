#smile = '\U0001F642'
#grin = '\U0001F641'

variables = {":)": "\U0001F642", ":(": "\U0001F641"}

sentence = input()

while sentence != "Done":

    words = sentence.split(" ")

    for i in words:
        if i in variables:
            sentence = sentence.replace(i, variables[i])

    break        

print (sentence)
