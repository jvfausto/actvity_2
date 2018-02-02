def is_vowel(word):
    word_lenght = len(word)
    position = 0
    while position < word_lenght:
        if(word[position] == 'A') or (word[position] == 'E') or(word[position] == 'I') or (word[position] == 'O') or (word[position] == 'U') or (word[position] == 'a') or (word[position] == 'e') or (word[position] == 'i') or (word[position] == 'o') or (word[position] == 'u'):
            return position    
        position = position + 1
    return -1    

def ammend_consonant(word):
    index = is_vowel(word)
    newWord = word[index:]
    finalWord = newWord + word[0:index] +'ay'
    return finalWord

inputString = input("Type some words (no punctuation, please!): ")
wordsList = inputString.split()
newWordsList = []
for n in range(len(wordsList)):
    word = wordsList[n]
    k = is_vowel(word)
    if(k == 0):
        word += 'ay'
    else:
        word = ammend_consonant(word)
        
    newWordsList.append(word)

print(newWordsList)
