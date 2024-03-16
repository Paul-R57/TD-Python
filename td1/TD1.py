#############################################################################
####################### Exercice 1 et 2 #####################################

# the list of letters we have
list_letters = ['b', 'p', 'd', 'w', 's', 'y', 'w', '?']


# open the file and save all the data in 'data'
file_path = "mots.sansaccent.txt"
file = open(file_path,'r')
data = file.read()
file.close()

# separate all words and remove the last one which is empty
words_list = data.split('\n')[:-1]



def longest_word(list_letters,words_list):
    max_letter_number = 0
    solution = ''

    # for each word in the list
    for word in words_list:
    
        # it create a list of letters that are in the word
        word_letters = list(word)
        
        # for each letter that we possess
        for letter in list_letters:
            # if this letter is in the word
            if letter in word_letters:
                # it remove it from the list of letters that are in the word
                word_letters.remove(letter)
    
    
        # if the the list of letters that are in the word is empty, 
        # the word can be written
        if word_letters == []:  
            
            number_letter = len(word)
            # if the word is longer than the previous better one
            if max_letter_number < number_letter:
                
                # it save the word and itslength
                max_letter_number = len(word)
                solution = word
    
    
    return solution


#############################################################################
####################### Exercice 3 ##########################################

# dictionary associating each letter to their point
letter_point = {
    'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2, 'm': 2,
    'b': 3, 'c': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4,
    'j': 8, 'q': 8,
    'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10 }



def score(word):
    word_score = 0
    
    # for each letter in the word, it sum the points to the score
    for letter in list(word):
        word_score += letter_point[letter]
        
    return word_score



def max_score(word_list):
    score_max = 0
    best_word = ''
    
    # for each word in the list
    for word in word_list:
        word_score = score(word)
        
        # if the score of this word is higher than the previous better one
        if word_score > score_max:
            # it save the word and the score
            best_word = word
            score_max = word_score
            
    return (best_word,score_max)


#############################################################################
####################### Exercice 4 ##########################################

# same idea than the function longest_word, but it save all the writeable words
# in a list and take in count a possible joker
def possible_words_list(list_letters,words_list):
    possible_words_list = []

    for word in words_list:
    
        word_letters = list(word)
         
        for letter in list_letters:
            if letter in word_letters:
                word_letters.remove(letter)
    
    
        if word_letters == []:        
            possible_words_list.append(word)
        
        # if there is one letter remaining in the word that we can't write
        # and we have a joker, the word is writeable
        elif (len(word_letters) == 1) and ('?' in list_letters):
            possible_words_list.append(word)
    
    return possible_words_list  



# print the result
print(max_score(possible_words_list(list_letters,words_list)))





