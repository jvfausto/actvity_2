#Function to identify vowel position


def is_vowel(word):
    
    word_lenght = len(word)
    position = 0
    
    while position < word_lenght:
        if(word[position] == 'A') or (word[position] == 'E') or(word[position] == 'I') or (word[position] == 'O') or (word[position] == 'U') or (word[position] == 'a') or (word[position] == 'e') or (word[position] == 'i') or (word[position] == 'o') or (word[position] == 'u'):
            return position
        
        position = position + 1

    return -1

