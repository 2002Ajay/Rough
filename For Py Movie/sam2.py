import random

movies = [
          'trance', 'forensic', 'shylock', 'the kung fu master', 'big brother', 'lucifer', 'brothers day',
          'cold case', 'cbi', 'one', 'home', 'the priest', 'malik', 'the great indian kitchen', 'salute',
          'joseph', 'night drive', 'traffic', 'classmates', 'bangalore days', 'sunny', 'joji', 'take off',
          'godfather', 'ramji rao speaking', 'his highness abdullah', 'uncle bun', 'johny walker', 'hitler',
          'superman', 'the car', 'summer in bethlehem', 'punjabi house', 'crime file', 'friends'
         ] # list of movies for guessing


def inst(): # instructions before starting the game 
    print("\nMalayalam Movie Guessing Game.\n\nOnly Malayalam movies with English like title are included.\n")
    if input("Let's start? (y/n): ") != 'y':
        print("Exited!\n") 
        exit()


def create_qn(movie): # for making packed form of picked movie, eg: cbi -> *** (packing as stars)
    temp = []
    for i in list(movie):
        temp.append(' ') if i == ' ' else temp.append('*') # if else shorthand
    return ''.join(str(x) for x in temp) # returing string after joining contents of list temp


def letter_guess(movie, mod_qn): # getting and checking user's guessed letter
    letter = input("Your letter guess: ").lower() # getting letter
    if letter in movie:
        print(f"Yes, {letter} found")
        ref = list(movie) # picked movie as list
        qn_list = list(mod_qn)    
        temp = []
        for i in range(len(movie)):
            if ref[i] == letter or ref[i] in mod_qn:
                temp.append(ref[i])
            elif qn_list[i] in ['*', '_']:
                temp.append('_')
        mod_qn = ''.join(str(x) for x in temp)
        if mod_qn == movie: # if user fills the question by gussing each letters
            print("Correct...You guessed it...\n", mod_qn)
            again()
        else:
            print(mod_qn)    
        return mod_qn
    else:
        print(f"No, {letter} not found")


def getNum(): # getting number for user's next move
    try:
        numb = int(input("Press 1) Guess movie's full name or 2) Guess another letter or 3) Exit : "))
    except:
        print("Wrong Input. Try Again")
        numb = getNum()
    return numb


def movie_guess(movie, modi_qn): # guesssing full movie name
    if input("Your answer: ").lower() == movie:
        print("Correct...You guessed it...\n", movie)
        again()
    else:
        print("Wrong Answer, but go on...")
        gus = letter_guess(movie, modi_qn)
        return gus


def again(): # if user likes to play again
    main() if input("Do you want to play again? y/n: ") == 'y' else exit()


def main(): # picking & removing the current movie & getting the guesses from user
    inst()
    picked_movie = random.choice(movies)
    movies.remove(picked_movie) # removing currently selected movie to avoid repetition, works in multiple plays at one go
    qn = create_qn(picked_movie)
    print(qn)
    modified_qn = qn
    while True:
        gus = letter_guess(picked_movie, modified_qn)
        modified_qn = gus
        num = getNum()
        if num == 1:
            guss = movie_guess(picked_movie, modified_qn)
            modified_qn = guss
        elif num == 2:
            res = letter_guess(picked_movie, modified_qn)
            modified_qn = res
        elif num == 3:
            exit()    
        else:
            print(num, "is out of range. Please guess another letter.")
            resl = letter_guess(picked_movie, modified_qn)
            modified_qn = resl            

if __name__ == "__main__": # main function call
    main()