from contextlib import nullcontext
import random
from tkinter import N

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
    toGuessList = []
    for i in wordToGuess:
        toGuessList.append(i)
    print(toGuessList)
    row = 1
    board = [f'+---+---+---+---+---+',
             f'|   |   |   |   |   |',
             f'+---+---+---+---+---+',
             f'|   |   |   |   |   |',
             f'+---+---+---+---+---+',
             f'|   |   |   |   |   |',
             f'+---+---+---+---+---+',
             f'|   |   |   |   |   |',
             f'+---+---+---+---+---+',
             f'|   |   |   |   |   |',
             f'+---+---+---+---+---+',
             f'|   |   |   |   |   |',
             f'+---+---+---+---+---+ \n']
    while row < 11:
        for line in board:
            print(line)
        wordDisplay = [' ', ' ', ' ', ' ', ' ']
        check = []
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
                        check.append(wordGuess[num])
                        if wordGuess[num] == wordToGuess[num]:
                            wordDisplay[num] = f'*{wordGuess[num]}*'
                        elif wordGuess[num] in wordToGuess:
                            if toGuessList.count(wordGuess[num]) > 1:
                                if check.count(wordGuess[num]) > toGuessList.count(wordGuess[num]):
                                    wordDisplay[num] = f' {wordGuess[num]} '
                                else:
                                    wordDisplay[num] = f' {wordGuess[num]}*'
                            elif check.count(wordGuess[num]) < 2:
                                wordDisplay[num] = f' {wordGuess[num]}*'
                            else:
                                wordDisplay[num] = f' {wordGuess[num]} ' 
                        else:
                            wordDisplay[num] = f' {wordGuess[num]} '
                    board[row] = f'|{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}|'
                    row += 2
                    if wordGuess == wordToGuess:
                        print(f'Congrats! You guessed the word: {wordToGuess} \n \n')
                        return True
            else:
                print(f'"{wordGuess}" is not five characters. \n')
        else:
            print(f'"{wordGuess}" is not a valid word. Try again. \n')
    print(f'The correct word was: {wordToGuess} \n')

def stats(stat):
    print(f'The number of games you won: {stat} \n \n')

if __name__ == "__main__":
    wins = 0
    wordList = open("c:/Users/Andrew Nguyen/Downloads/git/Python-WORDLE/words.txt").read().splitlines()
    guessList = open("c:/Users/Andrew Nguyen/Downloads/git/Python-WORDLE/guess.txt").read().splitlines()
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