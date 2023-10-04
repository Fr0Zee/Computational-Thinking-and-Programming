while True:
    words = input("Please enter two words: ").strip()
    if " " in words:
        id = words.find(" ")
        word1 = words[0:id].strip()
        word2 = words[id:len(words)].strip()
        if word1 < word2:
            print(word1, "comes first") 
        else :
            print(word2, "comes first")
    else:
        if (words == "done") or (len(words) == 0):
            print("-- bye !!")
            break
        continue