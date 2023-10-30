from translate import Translator
translator= Translator(from_lang="German", to_lang="English")

userInput = ''
stopwords = ['quit', 'exit', 'stop', 'abort', 'cancel']

print('Welcome to the German to English translator.\n')

userName = input('Please enter your name: ')
print(f"\nHello {userName}.")

while True:
    print('Please enter a word you would like to translate from German to English, or type "quit" to stop the program.')
    userInput = input('German word: ')
    
    if userInput.lower() in stopwords:
        break
    
    print(f"\nThank you, {userName}.")
    translation = translator.translate(userInput)
    print(f"The German word you entered was \"{userInput}\", which translates to \"{translation}\" in English.\n")