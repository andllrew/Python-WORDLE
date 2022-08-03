from contextlib import nullcontext
import random

def valid():
    while True:
        vInput = input()
        if vInput.isdigit():
            if 0 < int(vInput) < 4:
                return int(vInput)
        print(f'"{vInput}" is not a valid option. Try again.')

def play():
    randomNum = random.randint(0, len(wordList))
    wordToGuess = wordList[randomNum]
    wordDisplay = []
    guess = 1
    print(f'+---+---+---+---+---+ \n' +
        f'|   |   |   |   |   | \n' +
        f'+---+---+---+---+---+ \n' +
        f'|   |   |   |   |   | \n' +
        f'+---+---+---+---+---+ \n' +
        f'|   |   |   |   |   | \n' +
        f'+---+---+---+---+---+ \n' +
        f'|   |   |   |   |   | \n' +
        f'+---+---+---+---+---+ \n' +
        f'|   |   |   |   |   | \n' +
        f'+---+---+---+---+---+ \n' +
        f'|   |   |   |   |   | \n' +
        f'+---+---+---+---+---+ \n')
    while guess < 6:
        green = []
        yellow = []
        wordGuess = input("Your word guess: ")
        if wordGuess.isalpha():
            if wordGuess == "quit":
                break
            elif len(wordGuess) == 5: 
                if wordGuess not in guessList:
                    print(f'"{wordGuess}" is not in the word list. \n')
                    continue
                else:
                    for num in range(5):
                        if wordGuess[num] == wordToGuess[num]:
                            green.append(wordGuess[num])
                    for letter in wordGuess:
                        if letter in wordToGuess:
                            if letter not in green:
                                yellow.append(letter)
                    for letter in wordGuess:
                        if letter in green:
                            wordDisplay.append(f'*{letter}*')
                        elif letter in yellow:
                            wordDisplay.append(f' {letter}*')
                        else:
                            wordDisplay.append(f' {letter} ')
                    if guess == 1:
                        newDisplay = (f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n')
                    elif guess == 2:
                        newDisplay = (f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[5]}|{wordDisplay[6]}|{wordDisplay[7]}|{wordDisplay[8]}|{wordDisplay[9]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n')
                    elif guess == 3:
                        newDisplay = (f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[5]}|{wordDisplay[6]}|{wordDisplay[7]}|{wordDisplay[8]}|{wordDisplay[9]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[10]}|{wordDisplay[11]}|{wordDisplay[12]}|{wordDisplay[13]}|{wordDisplay[14]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n')
                    elif guess == 4:
                        newDisplay = (f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[5]}|{wordDisplay[6]}|{wordDisplay[7]}|{wordDisplay[8]}|{wordDisplay[9]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[10]}|{wordDisplay[11]}|{wordDisplay[12]}|{wordDisplay[13]}|{wordDisplay[14]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[15]}|{wordDisplay[16]}|{wordDisplay[17]}|{wordDisplay[18]}|{wordDisplay[19]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n')
                    elif guess == 5:
                        newDisplay = (f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[5]}|{wordDisplay[6]}|{wordDisplay[7]}|{wordDisplay[8]}|{wordDisplay[9]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[10]}|{wordDisplay[11]}|{wordDisplay[12]}|{wordDisplay[13]}|{wordDisplay[14]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[15]}|{wordDisplay[16]}|{wordDisplay[17]}|{wordDisplay[18]}|{wordDisplay[19]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[20]}|{wordDisplay[21]}|{wordDisplay[22]}|{wordDisplay[23]}|{wordDisplay[24]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|   |   |   |   |   | \n' +
                                    f'+---+---+---+---+---+ \n')
                    elif guess == 6:
                        newDisplay = (f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[5]}|{wordDisplay[6]}|{wordDisplay[7]}|{wordDisplay[8]}|{wordDisplay[9]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[10]}|{wordDisplay[11]}|{wordDisplay[12]}|{wordDisplay[13]}|{wordDisplay[14]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[15]}|{wordDisplay[16]}|{wordDisplay[17]}|{wordDisplay[18]}|{wordDisplay[19]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[20]}|{wordDisplay[21]}|{wordDisplay[22]}|{wordDisplay[23]}|{wordDisplay[24]}| \n' +
                                    f'+---+---+---+---+---+ \n' +
                                    f'|{wordDisplay[25]}|{wordDisplay[26]}|{wordDisplay[27]}|{wordDisplay[28]}|{wordDisplay[29]}| \n' +
                                    f'+---+---+---+---+---+ \n')
                    print(newDisplay)
                    if wordGuess == wordToGuess:
                        print(f'Congrats! You guessed the word: {wordToGuess} \n \n')
                        return True
                    guess += 1
            else:
                print(f'"{wordGuess}" is not five characters. \n')
        else:
            print(f'"{wordGuess}" is not a valid word. Try again. \n')
    print(f'The correct word was: {wordToGuess} \n')

def stats(stat):
    print(f'The number of games you won: {stat} \n \n')

if __name__ == "__main__":
    wins = 0
    wordList = open("c:/Users/Andrew Nguyen/Downloads/git/website-repo/words.txt").read().splitlines()
    guessList = open("c:/Users/Andrew Nguyen/Downloads/git/website-repo/guess.txt").read().splitlines()
    while True:
        print(f'Welcome to the Python Wordle Game! \n \n' +
        f'{"1. Play the game":>22} \n' +
        f'{"2. Display stats":>22} \n' +
        f'{"3. Exit":>13}')
        userInput = valid()
        if userInput == 1:
            result = play()
            if result == True:
                wins += 1
        if userInput == 2:
            stats(wins)
        if userInput == 3:
            print("Thank you for playing! Goodbye!")
            exit()