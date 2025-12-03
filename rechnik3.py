#smile = '\U0001F642'
#grin = '\U0001F641'

variables = {":)": "\U0001F642", ":(": "\U0001F641"}
sentence = ""

while sentence != "Done":

    sentence = input()

    words = sentence.split(" ")

    for i in range(0, len(words)):
           token = words[i]
           words[i] = variables.get(token, token)

    sentence = " ".join(words)
    print(sentence)
    