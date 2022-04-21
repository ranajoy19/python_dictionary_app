import json
from difflib import get_close_matches

path='data.json'
data= json.load(open(path))


def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yn= input("did you mean %s instead? Enter Y if yes or N if you mean NO : " % get_close_matches(w, data.keys())[0])
        yn= yn.upper()
        if yn =="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "word doesn't exist double check"
        else:
            return "we didn't understand you query"
    else:
        return "word doesn't exist in the dictionary"
word=input("enter the word :")


output= translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

