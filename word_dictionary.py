from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter the word (press 1 to exit): ")
    if word == "1":
        break

    print(dictionary.meaning(word))#provide meaning of the word form dictionary
