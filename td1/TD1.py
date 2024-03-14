#############################################################################
####################### Exercice 1 et 2 #####################################


list_letters = ['c','w','z','?']


file = open("mots.sansaccent.txt",'r')
data = file.read()
file.close()
words_list = data.split('\n')[:-1]



def longest_word(list_letters,words_list):
    max_letter_number = 0
    solution = ''


    for word in words_list:
    
    
        word_letters = list(word)
        
        
        for letter in list_letters:
            if letter in word_letters:
                word_letters.remove(letter)
    
    
        if word_letters == []:        
            number_letter = len(word)
            if max_letter_number < number_letter:
                max_letter_number = len(word)
                solution = word
    
    
    return solution


#############################################################################
####################### Exercice 3 ##########################################

letter_point = {
    'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2, 'm': 2,
    'b': 3, 'c': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4,
    'j': 8, 'q': 8,
    'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10 }


def score(word):
    word_score = 0
    
    for letter in list(word):
        word_score += letter_point[letter]
        
    return word_score


def MaxScore(word_list):
    max_score = 0
    best_word = ''
    
    for word in word_list:
        word_score = score(word)
        
        if word_score > max_score:
            best_word = word
            max_score = word_score
            
    return (best_word,max_score)


#############################################################################
####################### Exercice 4 ##########################################


def PossibleWords(list_letters,words_list):
    possible_words = []

    for word in words_list:
    
        word_letters = list(word)
         
        for letter in list_letters:
            if letter in word_letters:
                word_letters.remove(letter)
    
    
        if word_letters == []:        
            possible_words.append(word)
            
        elif (len(word_letters) == 1) and ('?' in list_letters):
            possible_words.append(word)
    
    return possible_words  

print(PossibleWords(list_letters,words_list))
print(MaxScore(PossibleWords(list_letters,words_list)))






#############################################################################
######################## Affichage ##########################################


'''
print('\n\n EXERCICE 2\n',
      'On recherche le mot le plus long contenant les lettres ' + str(list_letters),
      '\n Dans le fichier "mots.sansaccent.txt", le mot est:\n',
      longest_word(list_letters,words_list))
      
'''
