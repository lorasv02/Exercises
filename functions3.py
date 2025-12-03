#smile = '\U0001F642'
#grin = '\U0001F641'

def emojies(sentence):
    variables = {":)": "\U0001F642", ":(": "\U0001F641"}

    words = sentence.split(" ")

    for i in range(0, len(words)):
        token = words[i]
        words[i] = variables.get(token, token)
        
    return " ".join(words)
      

s = ""

while s != "Done":

    s = input()

    print(emojies(s))
    