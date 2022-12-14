import random

movies = [
          'trance', 'forensic', 'shylock', 'the kung fu master', 'big brother', 'lucifer', 'brothers day',
          'cold case', 'cbi', 'one', 'home', 'the priest', 'malik', 'the great indian kitchen', 'salute',
          'joseph', 'night drive', 'traffic', 'classmates', 'bangalore days', 'sunny', 'joji', 'take off',
          'godfather', 'ramji rao speaking', 'his highness abdullah', 'uncle bun', 'johny walker', 'hitler',
          'superman', 'the car', 'summer in bethlehem', 'punjabi house', 'crime file', 'friends'
         ]

# unlocked = []

def create_question(movie): # for making packed form of taken movie, eg: for cbi -> *** (packing as stars)
    temp = []
    for i in list(movie):
        # temp.append(' ') if i == ' ' else temp.append('*') -> shorthand
        if i == ' ':
            temp.append(' ') # for space b\w words of taken movie name
        else:
            temp.append('*') # for letters in movie name
    qn = ''.join(str(x) for x in temp)
    return qn
            
def unlock(qn, movie, letter): # qn = mod_qn, movie = picked_movie, letter = user input letter
    ref = list(movie) # picked movie as list
    qn_list = list(qn) # previously modified qn as list
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ':
            temp.append(" ")
        elif ref[i] == letter:
            temp.append(ref[i])
        elif ref[i] == [j for j in ref]:
            if ref[i] == letter:
                continue
            else:
                temp.append(ref[i])
        else:
            if qn_list[i] == '*' or qn_list[i] == '_':
                temp.append(' _ ')
            
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def movie_guess(picked_movie, modi_qn):
    if input("Your answer: ") == picked_movie:
        print("Correct...")
        again()
    else:
        print("Wrong Answer, but go on...")
        res = letter_guess(picked_movie, modi_qn)
    return res    


def letter_guess(picked_movie, mod_qn):
    letter = input("Your letter guess: ")
    if letter in picked_movie:
        print(f"Yes, {letter} is found")
        mod_qn = unlock(mod_qn, picked_movie, letter)
        print(mod_qn)
    else:
        print(f"No, {letter} not found")
    return mod_qn      


def again():
    play() if input("Do you want to play again? y/n: ") == 'y' else exit()

def play():
    print("\nMalayalam Movie Guessing Game\n\nOnly Malayalam movies with English title are included\n")
    while True:
        picked_movie = random.choice(movies)
        print(picked_movie) # remove finally -------------- /////////  ---------------  ///////////   ---------------
        qn = create_question(picked_movie)
        print(qn)
        modified_qn = qn
        while True:
            res = letter_guess(picked_movie, modified_qn)
            modified_qn = res
            d = int(input("Press 1) guess movie's full name or 2) guess another letter or 3) Exit : "))
            if d == 1:
                gus = movie_guess(picked_movie, modified_qn)
                modified_qn = gus
            elif d == 2:
                rest = letter_guess(picked_movie, modified_qn)
                modified_qn = rest
            elif d == 3:
                exit()    
            else:
                print(d, "is out of range")
                resl = letter_guess(picked_movie, modified_qn)
                modified_qn = resl
            
play()

# use try catch for entering alphabets when int input is required.
# show previous correctly guessed letter
# add comment - chnage unlock func with other elifs