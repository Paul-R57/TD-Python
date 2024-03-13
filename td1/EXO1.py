list_letters = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
possible_words = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge',
                   'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars',
                    'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase',
                    'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas',
                    'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']


max_number = 0
solution = ''

for word in possible_words:
    word_letters = [letter for letter in word]
    for letter in 

    if word_letters in list_letters:        
        number_letter = len(word)
        if max_number < number_letter:
            max_number = len(word)
            solution = word

print(solution,max_number)
