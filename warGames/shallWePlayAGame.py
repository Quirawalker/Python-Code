"""
This is based on the iconic computer from the movie "War Games" and then I added
some modifications and additions of my own. Please note this code is not fully complete.
it will run but not all files are completed, so only the Chat, TicTacToe, Explain, and Shutdown
functions work. The rest will print a file name but will not execute.
"""

import time, sys
from tictactoe import *
from Razzie_Chatter import *
from downloadBar import *
from gtw import *
passwordTrys = 0

print('\n'*50)
print("Hello, I am the Razzie Computer.\n")
time.sleep(1.0)
while True:
    print("\n\t|-------Login-------|")
    print("\tUsername: ")
    print("\tPassword: ")
    username = input("Username: ")
    print('\n'*50)
    print("\n\t|-------Login-------|")
    print("\tUsername: ",username)
    print("\tPassword: ")
    password = input("Password: ")
    print('\n'*50)
    print("\n\t|-------Login-------|")
    print("\tUsername: ",username)
    print("\tPassword: ",password)

    print("\tPLEASE WAIT...")
    downloadBar()
#
    if password == 'pi':
#
        print("\t~Access Granted~")
        time.sleep(2.0)
        print("\nWelcome ",username)
        time.sleep(2.0)
        while True:
            print("What would you like to do?")
            time.sleep(1.0)
            print("\n\t1: Chat")
            time.sleep(0.75)
            print("\t2: Play a game")
            time.sleep(0.75)
            print("\t3: Shutdown")
            time.sleep(0.75)
            mainMenu = input()
            if mainMenu == '1':
                print("Would you like to Chat with Razzie? {yes or no}")
                chatAnswer = input()
                if chatAnswer == 'yes':
                    #print("Run File ==> Chat")
                    downloadBar()
                    chatter()
                elif chatAnswer == 'no':
                    #print("Returning you to line 30")
                    time.sleep(1.0)
                else:
                    print("Invalid Input, try again.")
                    time.sleep(1.0)
                    continue
            elif mainMenu == '2':
                print("Would you like to play a game? {yes or no}")
                gameAnswer = input()
                if gameAnswer == 'yes':
                    print("What would you like to play?\n")
                    time.sleep(0.75)
                    print("\t1: Tic-Tac-Toe")
                    time.sleep(0.75)
                    print("\t2: Connect Four")
                    time.sleep(0.75)
                    print("\t3: Checkers")
                    time.sleep(0.75)
                    print("\t4: Chess")
                    time.sleep(0.75)
                    print("\t5: Global Thermonuclear War")
                    time.sleep(0.75)
                    print("\n\t6: Explain")
                    time.sleep(0.75)
                    print("\t7: Exit")
                    gameChoice = input()
                    if gameChoice == '1':
                        #print("Running File ==> Tic-Tac-Toe")
                        downloadBar()
                        tictactoe()
                    elif gameChoice == '2':
                        print("Running File ==> Connect Four")
                        time.sleep(1.0)
                    elif gameChoice == '3':
                        print("Running File ==> Checkers")
                        time.sleep(1.0)
                    elif gameChoice == '4':
                        print("Running File ==> Chess")
                        time.sleep(1.0)
                    elif gameChoice == '5':
                        #print("Running File ==> Global Thermonuclear War")
                        downloadBar()
                        Global_Thermonuclear_War()
                    elif gameChoice == '6':
                        print("Do you need one of the above choices explained? {yes or no}")
                        time.sleep(1.0)
                        gameChoiceAnswer = input()
                        if gameChoiceAnswer == 'yes':
                            print(
                                """
                                Which game would you like explained?
                                \t1: Tic-Tac-Toe
                                \t2: Connect Four
                                \t3: Checkers
                                \t4: Chess
                                \t5: Global Thermonuclear War
                                """)
                            gameAnswerChoice = input()
                            if gameAnswerChoice == '1':
                                print("Tic-Tac-Toe",
                                    """
                                    This is simple game is actually rather a game of luck.
                                    A two-player game where the goal is for one player to
                                    be the first one to get 3 in a row.
                                    You can win:
                                        ~Horizontally
                                        ~Vertically
                                        ~Diagonally
                                    """
                                    )
                                input("Press ENTER to continue")
                            elif gameAnswerChoice == '2':
                                print("Connect Four",
                                    """
                                    This is a step up from Tic-Tac-Toe, and is more challenging.
                                    A two-player game where the goal is for one player to be the
                                    first one to reach 4 in a row.
                                    You can win:
                                        ~Horizontally
                                        ~Vertically
                                        ~Diagonally
                                    """
                                    )
                                input("Press ENTER to continue")
                            elif gameAnswerChoice == '3':
                                print("Checkers",
                                    """
                                    This is an old-fashioned board game for 2 players. The goal
                                    is simple... Be the first to get all your opponents pieces
                                    by jumping them diagonally. You can only jump on your color
                                    and only jump once unless you can take multiple pieces.
                                    """
                                    )
                                input("Press ENTER to continue")
                            elif gameAnswerChoice == '4':
                                print("Chess",
                                    """
                                    Chess is much like Checkers but takes skill and stratagey.
                                    This two-player game is compossed of a 8x8 checkered board
                                    and 16 pieces per player. Those 16 pieces are made up of:
                                    ~8 Pawns: Move 1 or 2 spaces forward on first move and 1
                                        space each consecutive move. They may only take a piece
                                        one move diagonally.
                                    ~1 King: Moves in any direction one space at a time and can
                                        take a piece one move in any direction.
                                        ~~~The King must be able to escape the opponent. If the
                                            King can't be moved to safety the opponent wins.
                                            If you can trap the opponent's King you win.
                                    ~1 Queen: Moves the same as the King but may go multiple spaces.
                                    ~2 Bishops: Moves like the Rooks but only diagonally, and can
                                        a piece in the movement.
                                    ~2 Knights: Move in an 'L' shape. These are the only pieces
                                        that can jump other pieces. You can only take a piece
                                        if you land on it. You can move 1 space by 2 spaces or
                                        2 spaces by 1 space.
                                    ~2 Rooks: Moves horizontally or vertically as many spaces as
                                        you like and may take a piece in the movement.
                                    """
                                    )
                                input("Press ENTER to continue")
                            elif gameAnswerChoice == '5':
                                print("Global Thermonuclear War",
                                    """
                                    UKNOWN FILE. . .
                                    """
                                    )
                                input("Press ENTER to continue")
                            else:
                                print("Invalid Input, try again")
                                time.sleep(1.0)
                                continue
                        elif gameChoiceAnswer == 'no':
                            #print("Returning you to line 53")
                            time.sleep(1.0)
                        else:
                            print("Invalid Input, try again.")
                            time.sleep(1.0)
                            continue
                    elif gameChoice == '7':
                        #print("Returning you to line 30")
                        time.sleep(1.0)
                    else:
                        print("Invalid Input, try again.")
                        time.sleep(1.0)
                        continue
                elif gameAnswer == 'no':
                    #print("Returning you to line 30")
                    time.sleep(1.0)
                else:
                    print("Invalid Input, try again.")
                    time.sleep(1.0)
                    continue
            elif mainMenu == '3':
                time.sleep(2.0)
                print("Are you sure you would like to Shutdown {yes or no}")
                shutdownAnswer = input()
                if shutdownAnswer == 'yes':
                    print("Have a good day!",username)
                    time.sleep(1.0)
                    print("Shutting Down...")
                    time.sleep(1.0)
                    sys.exit()
                elif shutdownAnswer == 'no':
                    print("Shutdown Aborted")
                    time.sleep(1.0)
                    #print("Returning you to line 30")
                    time.sleep(1.0)
                else:
                    print("Invalid Input, try again.")
                    time.sleep(1.0)
                    continue
            else:
                print("Invalid Input, try again.")
                time.sleep(1.0)
                continue
    else:
        print("\t~Access Denied~")
        passwordTrys += 1
        time.sleep(0.5)
        print("\tIncorrect Password")
        time.sleep(0.5)
        print('\n'*50)
        if passwordTrys == 3:
            print("\n\t~~~SYSTEM LOCKOUT~~~")
            time.sleep(3.0)
            sys.exit()