

list_letters = ['a', 'a', 'a', 'g', 'e', 's', 'c', 'j']


file = open("mots.sansaccent.txt",'r')
data = file.read()
file.close()
possible_words = data.split('\n')



max_number = 0
solution = ''

for word in possible_words:

    word_letters = list(word)
    for letter in list_letters:
        if letter in word_letters:
            word_letters.remove(letter)

    if word_letters == []:        
        number_letter = len(word)
        if max_number < number_letter:
            max_number = len(word)
            solution = word

print(solution,max_number)
