print("\n\nWELCOME TO GROUP 2'S GAMING PROGRAM\n")


choice = None # variable choice has assigned no value

while choice != "": # refer to previous line
# Program main menu/ directory
    print(
    """
+++++++++++++++++++++++++++++++++++++++++++
|   This program consist of three games.  |
|                                         |
|          Challenge your arithmetic      |
|   Explore your skill                    |
|            Test your memory             |
|                                         |
|             Choose wisely...            |
|                                         |
|    0 - Exit Shop                        |
|    1 - The Calculenator                 |
|    2 - Rock Paper Scissors              |
|    3 - Guess the Lyric                  |
+++++++++++++++++++++++++++++++++++++++++++
    """
    )
    choice = input("Choice: ") # choice is assigned a value (selected game)
    print() # new line
       
    # initalize choice selection
    # exit the game
    if choice == "0": 
        print("exit")
        break # escape loop to main menu

    # user selects game one
    elif choice == "1": 
        which_operation = None  # variable which_choice has no value
        while which_operation != "": # refer to line 1
            # menu options as well as introduction to how the game works
            print(
        """
            ---------------------------------------------------------
                        ¡¡WELCOME TO THE CALCULENATOR!! 
            
                In this game, we will be practicing our math!
                You have only five options to choose from:
            
                                OPTIONS
                        
                            * : multiplication
                            / : division
                            + : addition
                            - : subtraction
                            X : exit the game
            ---------------------------------------------------------
        """
            )
            which_operation = input("Which type of operation would you like to practice on? ")

            # option exits user from the game
            if which_operation == 'X' : 
                print("Sad to see you go :,( See ya later!")  
                break # breaks loop and returns user to main menu 
            # Allos user to add whatever two number they choose
            elif which_operation == '+' : 
                first_number = input("\nChoose a number: ") # user inputs first number
                sec_number = input("Choose a second number: ") # user inputs second number
                total = int(first_number) + int(sec_number) # computer completes arithmetic
                print(f"The sum of {first_number} and {sec_number} is {total}") # program prints total of the two numbers chosen by user
            # option allows user to subtract whatever two numbers they choose
            elif which_operation == '-' : 
                first_number = input("\nChoose a number: ") 
                sec_number = input("Choose a second number: ") 
                total = int(first_number) - int(sec_number)
                print(f"The difference between {first_number} and {sec_number} is {total}")  # program prints the difference of the two numbers chosen by user
            # option allows user to divide whatever two numbers they choose
            elif which_operation == '/' :
                first_number = input("\nChoose a number: ") 
                sec_number = input("Choose a second number: ") 
                total = int(first_number) / int(sec_number)
                print(f"{first_number} divided by {sec_number} is equal to {total}") # program prints the total of the two divided numbers chosen by user
            # option allows user to multiply whatever two numbers they choose
            elif which_operation == '*' :
                first_number = input("\nChoose a number: ") 
                sec_number = input("Choose a second number: ") 
                total = int(first_number) * int(sec_number)
                print(f"{first_number} multiplied by {sec_number} is equal to {total}") # program prints the total of the two multiplied numbers chosen by user
            # user enters anything not apart of the menu, they recieve a notice
            else:
                ("Out of bounds, you only have five options!")

    elif choice == "2":
        print("Welcome to Rock, Paper, Scissors!\nChoose from the options below, depending on your skill level\n")

        #Function to go back and change if necessary
        #Create menu so that the rock, paper game has 2 "modes"

        def mode():
            print("Quick Game: (1)")
            print("Keep Playing Until You Lose: (2)")

        ##Call function, and put option at top since it remains consistent throughout code
        mode()
        option = int(input(" "))

        #A while loop to start the ifs and elses, choose 0

        while option != 0:
            if option == 1:
                print("\nBest of 1?\nReally? Good luck!\n")#Prompt to set up the rest of the game
                import random
                objects = ["Rock", "Paper", "Scissors"]
                opponent = random.choice(objects)# Avoids assigning numbers to objects
                choose = str(input("Rock.\nPaper.\nScissors.\nShoot! "))#Simulates choosing rock paper or scissors on shoot.
                if opponent == choose:
                    print("Your opponent chose:",opponent)
                    print("Its a Draw.")
                    break # break ends the loop efficiently throughout this if statement
                elif (opponent == "Rock" and choose == "Paper") or (opponent == "Paper" and choose == "Scissors") or (opponent == "Scissors" and choose == "Rock"):
                    print("Your opponent chose:",opponent)## All scenarios in one singular elif statement to avoid clutter
                    print("Good job. You actually won")
                    break
                ## Display a prompt to engage players, and include "opponent" so that player knows why they lost
                else:
                    print("Your opponent chose: ",opponent,'.'" You lost.", sep ="")
                    break
            # Prompt to exhibit the difference in both options
            elif option == 2:
                print("\nThe Game ends if you lose!")
                import random
                objects = ["Rock", "Paper", "Scissors"]
                opponent = random.choice(objects)
                choose = str(input("Rock.\nPaper.\nScissors.\nShoot! "))
                if opponent == choose:
                    print("Your opponent chose: ",opponent,'.'" Its a Tie.", sep = "") # Change the prompts from option 1
                elif (opponent == "Rock" and choose == "Paper") or (opponent == "Paper" and choose == "Scissors") or (opponent == "Scissors" and choose == "Rock"):
                    print("Your opponent chose: ", opponent)
                    print("You won. Try to keep your streak going!")## Seperates this prompt from the previous print statement
                else:
                    print("Your opponent chose: ",opponent)
                    print("You lost. Close the application or build a streak if you can!")
                    break# Break to close out the loop, allows user to restart the entire game by going to menu

    elif choice == "3":
        SONGS = {"bright": "So shine ______, tonight, you and I.",
          "sunshine": "I broke his heart 'cause he was nice. He was ________, I was midnight rain. ",
          "cherry": "Last night really was the ______ on the cake. Been some dark days lately and I'm finding it crippling."}
        # variable song stores a dictionary keys are missing lyric, values are the verses.
        chance = 3 # 3 chances to guess the missing lyric
        guessCount = 0 # user starts with 0 guesses

        choice = None  # variable choice has no value
        while choice != "0": #refer to previous line
            #instructions for how the game operates
            print(
        """
    ------------------------------------------------------------
                ! Welcome to the Guess the Lyric ! 
    
    The game consist of three levels: Easy, Medium, and Hard.

                The RULES are simple:
     ~Guess the lyric without looking it up.
     ~You have 3 chances per level.
     ~Have fun!
    
                    OPTION MENU
                0 - Exit the Game.
                1 - Easy
                2 - Medium
                3 - Hard
    ------------------------------------------------------------
        """
    ) 
            choice = input("Choice: ") # menu choice of the strings 0-3 to follow through
            print() #new line

            # exits the game
            if choice == "0": 
                print("Thank's for visting!") 
                break # escapes loop back to inital menu

            # user selects the easy level
            elif choice == "1":
                # reset guessCount for each interation (after the 3 chances you can try another level w/ 3 chances)
                guessCount = 0  
                print("Level: EASY""\n")
                print(SONGS["bright"]) # prints the value aka the song verses
                print() 

                # demonstates loop that occurs for guessCount
                while guessCount != 3: # recognizes max of 3 guesses
                    guessCount += 1 # add 1 to guessCount
                    guess = input("Guess the missing lyric: ")
                    # check if guess exists in the dictionary
                    if guess in SONGS: 
                        guesss = SONGS["bright"] 
                        print("\nCorrect: So shine", guess,"tonight, you and I.")
                        print("Diamonds by Rihanna") 
                        break # escape loop if guess in SONGS
                    # check if guess not in SONGS
                    if guess != SONGS: 
                        left = chance - guessCount  # take away a guessCount from chance, store in variable left
                        # demonstrates when left is zero
                        if left == 0:
                            print("\nOut of chances. The missing lyric was: bright")

            # user selects the the medium level
            elif choice == "2":
            # reset guessCount for each interation (after the 3 chances you can try another level w/ 3 chances)
                guessCount = 0 
                print("Level: MEDIUM""\n")
                print(SONGS["sunshine"])
                print() 
                # demonstates loop that occurs as long as guessCount is not 3
                while guessCount != 3:
                    guessCount += 1
                    guess = input("Guess the missing lyric: ")
                    # check if guess exists in the dictionary
                    if guess in SONGS:
                        guesss = SONGS["sunshine"]
                        print("\nCorrect: I broke his heart 'cause he was nice. He was", guess, ",I was midnight rain.")
                        print("Midnight Rain by Taylor Swift")
                        break
                    # check if guess not in SONGS
                    if guess != SONGS:
                        left = chance - guessCount
                        if left == 0: 
                            print("\nOut of chances. The missing lyric was: sunshine")
            elif choice == "3":
                # reset guessCount for each interation (after the 3 chances you can try another level w/ 3 chances)
                guessCount = 0
                print("Level: HARD""\n")
                print(SONGS["cherry"])
                print() 
                # demonstates loop that occurs as long as guessCount is not 3
                while guessCount != 3:
                    guessCount += 1
                    guess = input("Guess the missing lyric: ")
                    # check if guess exists in the dictionary
                    if guess in SONGS:
                        guesss = SONGS["cherry"]
                        print("\nCorrect!\n""Last night really was the", guess,"on the cake. Been some dark days lately and I'm finding it crippling.")
                        print("Escapism. by 070 Shake and Raye")
                        break
                    # check if guess not in SONGS
                    if guess != SONGS:
                        left = chance - guessCount
                        if left == 0:
                            print("\nOut of chances.""\nThe missing lyric was: cherry")
        # user enters anything not apart of the menu, they recieve a notice
        else: 
            print("Invalid entry.")
          


          


