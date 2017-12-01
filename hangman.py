#Hangman
#Made by Shane F.

def sphash_screen():
    print("=======================")
    print("~~Welcome to FootRace~~")
    print("=======================")
    print("           .==,_")
    print("         .===,_`\        ,,,,, ")
    print("       .====,_ ` \      .====,\__")
    print(" ---     .==-,`~. \           \ OO__,")
    print("  ---      `~~=-.  \           /__-/")
    print("    ---       `~~=. \         /")
    print("                 `~. \       /")
    print("                   ~. \____./")
    print("                     `.=====)")
    print("                  ___.--~~~--.__")
    print("        ___\.--~~~              ~~~---.._|/")
    print("        ~~~*  ""                           " "/")
sphash_screen()
def get_puzzle():
    return "answer"

def get_solved(puzzle, correct_guesses):
    solved = ""
    
    for letter in puzzle:
        if letter in correct_guesses:
            solved += letter
        else:
            solved += "-"
            
            
    
    return solved

def get_guess(puzzle, correct_guesses, missed_letters, missed_words):
    guess = input("Guess a letter:")
    if guess in correct_guesses or guess in missed_letters:
        print("*********************************")
        print("**You already used this letter.**")
        print("*********************************")
        guess = ""
    while len(guess)>1:
        guessing_word = input("Is "+(guess)+" your answer:")
        if guessing_word == 'y':
            if guess == puzzle:
                return guess
            else:
                print("Nope, that is not the word.")
            return guess      
        if guessing_word == 'n':
            
            print("Only give one letter.")
            guess = ""
    
    return guess

def display_board(solved, missed_letters, missed_word):
    print("========================================")
    print("Solved: " + solved)
    print("Missed Letters: {" + missed_letters + "}")
    print("Missed Words: {" + missed_word + "}")
    
    

def show_result(solved, puzzle):
    if solved==puzzle:
        print("You got the puzzle...")
        print("You Win!")
    else:
        print("You ran out of tries...")
        print("You Lose!")
    
def play():
    puzzle = get_puzzle()
    correct_guesses = ""
    missed_words = ""
    missed_letters = ""
    solved = get_solved(puzzle, correct_guesses)

    strikes = 0
    limit = 6
    print(solved)
    
    while solved != puzzle and strikes!=6:
        letter = get_guess(puzzle, correct_guesses, missed_letters, missed_words)
        if len(letter)>1:
            word = letter

        
        
            
        if letter not in puzzle and len(letter)==1:
            missed_letters += letter + " "
        elif letter != puzzle and len(letter)>1:
            missed_words += letter + " "
        else:
            correct_guesses +=letter
        
        solved = get_solved(puzzle, correct_guesses)
        display_board(solved, missed_letters, missed_words)
        if letter == "" or (len(letter)==1 and letter in puzzle) or (len(letter)>1 and letter == puzzle):
            pass
        else:
            strikes += 1
        print("Strikes: " + str(strikes))
        print("========================================")

    show_result(solved, puzzle)



def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def show_credits():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Thank you for playing.")
    print("This game was made by Shane F.!")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
playing=True
            
while playing:
    play()
    playing=play_again()

show_credits()
