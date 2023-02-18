
secretWord='libro'

cont=0
print('Welcome to the word guessing game!')
print()
print('Your hint is: _ _ _ _ _ ')
print()
word=0
while word != secretWord:
    word=input('What is your guess: ')
    hint=''
    
    for i, letter in enumerate(secretWord):
    
        if i < len(word) and letter.lower() == (word)[i]:
            hint += letter.upper()
        elif letter.lower() in word:
            hint += letter.lower()
        elif len(word) > len(secretWord):
            print('Sorry, the guess must have the same number of letters as the secret word.')
        else:
            hint += "_"
    
    print(f'Your hint is {hint}')
    cont +=1
print('Congratulations! You guessed it!')
print(f'It took you {cont} guesses.')







