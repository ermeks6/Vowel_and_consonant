while True:
    word = input("введите слово: ")
    num_word = len(word)
    vowels = 0
    consonants = 0
    if word == "exit":
        break
    else:
        for i in word.lower():
            if i in ('уеыаоэяиюeeyuoai'):
                vowels += 1
            elif i in "йцкнгшщзхъждлрпвфчсмтьбwrtpsdfghjklzxcvbnm":
                consonants += 1
            else:
                break
        vowels_percent = round((vowels / num_word) * 100, 2)
        consonants_percent = round((consonants / num_word) * 100, 2)

        print(
            f'Слово: {word} \nКоличество букв: {num_word} \nСогласных букв: {consonants} \nГласных букв: {vowels} \n'
            f'Процент гласных/согласных: { vowels_percent}%, {consonants_percent}%')

