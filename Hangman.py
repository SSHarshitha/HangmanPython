import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

         

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess=''
    for letter in secret_word:
        if letter not in letters_guessed:
            guess+=("_ ")
        else:
            guess+=letter       
    return guess     


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    char=string.ascii_lowercase
    for i in letters_guessed:
        char=char.replace(i,"")
    return char

def unique_letters(secret_word):
    unique=[]
    for char in secret_word:
        if char not in unique:
            unique.append(char)
    return(len(unique))        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    '''

    print("\nWelcome to the game Hangman!!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    qn="_ "*len(secret_word)
    print("The secret word you need to guess is::: ",qn,"\n")
    inti_guess=6
    letters_guessed=[]
    warn=3
    print("You have",warn,"warning left.")
    vowels='aeiou'
    cword=[] #correct letters
    
    while inti_guess>0:
        letter=get_available_letters(letters_guessed)
        print("You have",inti_guess,"guesses left.") 
        print("\nAvailable letters",letter)
        guess_letter=input("Please select a letter:")
        count=secret_word.count(guess_letter)
        
        
                
        if str.isalpha(guess_letter):
            guess_letter=str.lower(guess_letter)
            if guess_letter in cword:
                if warn>0:
                    warn-=1
                    print("Oops!! Letter already guessed. You've",warn,"warnings left.")
                    continue
                else:
                    inti_guess-=1
                    print("Oops!! Letter already guessed.")
                    continue
                
        
            letters_guessed.append(guess_letter)
            letter=get_available_letters(letters_guessed)
            count=secret_word.count(guess_letter)
            new_guess=get_guessed_word(secret_word, letters_guessed)
            if count!=0:
                print("Good guess","\U0001F601",new_guess)
                cword.append(guess_letter)
                    
            else:
                print("Oops! that letter is not in my guess","\U0001F612",new_guess)
                if guess_letter not in vowels:
                    inti_guess-=1
                else:
                    inti_guess-=2
            '''if inti_guess<4:
                choice=input("Do you need any hint?Yes or No: ")
                if choice=="Yes":
                    my_word=new_guess'''
                    
            if is_word_guessed(secret_word, cword):
                score=unique_letters(secret_word)
                print("Hurray \U0001F973 You guesssed it right")
                print("Your score is",inti_guess*score)
                break
        else:
           if warn>0:
               warn-=1
               print("Oops! That's not a valid letter!!! You have",warn,"warnings left.")
           else:
               inti_guess-=1
               print("Oops! That's not a valid letter!!!")
        print("#"*20+"\n")
        
    if inti_guess==0:
        print("You're out of guesses. Better luck next time.")
        print("The secret word is",secret_word)
        



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
    corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;False otherwise:
            '''
    word=""        
    for i in my_word:
        y=i.strip()
        word+=y   
    my_word=word
    if len(my_word)==len(other_word):
        for i in range(len(my_word)):
            if my_word[i]!="_":
                if my_word[i]!=other_word[i]: 
                    return False              
    else:
        return False            
    return True       
    



def show_possible_matches(my_word):    
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    hints=""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            hints+=other_word+" "
    if hints=="":
        print("Sorry, No matches found.")
    print("Showing similar words: ",hints)    
            



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("\nWelcome to the game Hangman!!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    qn="_ "*len(secret_word)
    print("The secret word you need to guess is::: ",qn,"\n")
    inti_guess=6
    letters_guessed=[]
    warn=3
    print("You have",warn,"warning left.")
    vowels='aeiou'
    cword=[] #correct letters
    
    while inti_guess>0:
        letter=get_available_letters(letters_guessed)
        print("You have",inti_guess,"guesses left.") 
        print("\nAvailable letters",letter)
        guess_letter=input("Please select a letter:")
        count=secret_word.count(guess_letter)
                
        if str.isalpha(guess_letter):
            guess_letter=str.lower(guess_letter)
            
            if guess_letter in cword:
                if warn>0:
                    warn-=1
                    print("Oops!! Letter already guessed. You've",warn,"warnings left.")
                    continue
                else:
                    inti_guess-=1
                    print("Oops!! Letter already guessed.")
                    continue
                
        
            letters_guessed.append(guess_letter)
            letter=get_available_letters(letters_guessed)
            count=secret_word.count(guess_letter)
            new_guess=get_guessed_word(secret_word, letters_guessed)
            if count!=0:
                print("Good guess","\U0001F601",new_guess)
                cword.append(guess_letter)
                    
            else:
                print("Oops! that letter is not in my guess","\U0001F612",new_guess)
                if guess_letter not in vowels:
                    inti_guess-=1
                else:
                    inti_guess-=2
            '''if inti_guess<4:
                choice=input("Do you need any hint?Yes or No: ")
                if choice=="Yes":
                    my_word=new_guess'''
                    
            if is_word_guessed(secret_word, cword):
                score=unique_letters(secret_word)
                print("Hurray \U0001F973 You guesssed it right")
                print("Your score is",inti_guess*score)
                break
        elif guess_letter=="*":
            my_word=new_guess
            show_possible_matches(my_word)    

        else:
           if warn>0:
               warn-=1
               print("Oops! That's not a valid letter!!! You have",warn,"warnings left.")
           else:
               inti_guess-=1
               print("Oops! That's not a valid letter!!!")
        print("#"*20+"\n")
        
    if inti_guess==0:
        print("You're out of guesses. Better luck next time.")
        print("The secret word is",secret_word)
        


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
