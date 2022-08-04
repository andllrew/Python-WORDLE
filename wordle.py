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
    toGuessList = []
    for i in wordToGuess:
        toGuessList.append(i)
    row = 1
    board = [f'{"+---+---+---+---+---+":>30}',
             f'{"|   |   |   |   |   |":>30}',
             f'{"+---+---+---+---+---+":>30}',
             f'{"|   |   |   |   |   |":>30}',
             f'{"+---+---+---+---+---+":>30}',
             f'{"|   |   |   |   |   |":>30}',
             f'{"+---+---+---+---+---+":>30}',
             f'{"|   |   |   |   |   |":>30}',
             f'{"+---+---+---+---+---+":>30}',
             f'{"|   |   |   |   |   |":>30}',
             f'{"+---+---+---+---+---+":>30}',
             f'{"|   |   |   |   |   |":>30}',
             f'{"+---+---+---+---+---+":>30} \n']
    keys = [f'+---+---+---+---+---+---+---+---+---+---+',
            f'| Q | W | E | R | T | Y | U | I | O | P |',
            f'+---+---+---+---+---+---+---+---+---+---+',
            f'  +---+---+---+---+---+---+---+---+---+',
            f'  | A | S | D | F | G | H | J | K | L |',
            f'  +---+---+---+---+---+---+---+---+---+',
            f'     +---+---+---+---+---+---+---+',
            f'     | Z | X | C | V | B | N | M |',
            f'     +---+---+---+---+---+---+---+ \n']
    keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
    while row < 13:
        green = []
        yellow = []
        check = []
        wordDisplay = [' ', ' ', ' ', ' ', ' ']
        for line in board:
            print(line)
        for a in keys:
            print(a)
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
                        format = 0
                        count = 1
                        check.append(wordGuess[num])
                        if wordGuess[num] == wordToGuess[num]:
                            green.append(wordGuess[num])
                            wordDisplay[num] = f'*{wordGuess[num]}*'
                            if wordGuess[num] in yellow:
                                if check.count(wordGuess[num]) > toGuessList.count(wordGuess[num]):
                                    wordDisplay[wordDisplay.index(f' {wordGuess[num]}*')] = f' {wordGuess[num]} '
                                    yellow.remove(wordGuess[num])
                        elif wordGuess[num] in wordToGuess:
                            if toGuessList.count(wordGuess[num]) > 1:
                                if check.count(wordGuess[num]) > toGuessList.count(wordGuess[num]):
                                    wordDisplay[num] = f' {wordGuess[num]} '
                                else:
                                    yellow.append(wordGuess[num])
                                    wordDisplay[num] = f' {wordGuess[num]}*'
                            elif check.count(wordGuess[num]) < 2:
                                yellow.append(wordGuess[num])
                                wordDisplay[num] = f' {wordGuess[num]}*'
                            else:
                                wordDisplay[num] = f' {wordGuess[num]} ' 
                        else:
                            wordDisplay[num] = f' {wordGuess[num]} '
                        for b in range(3):
                            str = f'{"|":>{format}}'
                            for c in keyboard[b]:
                                if wordGuess[num].upper() == c.replace(' ', '').replace('*', ''):
                                    if wordGuess[num] in green:
                                        keyboard[b][keyboard[b].index(c)] = f'*{wordGuess[num].upper()}*'
                                        c = f'*{wordGuess[num].upper()}*'
                                    elif wordGuess[num] in yellow:
                                        keyboard[b][keyboard[b].index(c)] = f' {wordGuess[num].upper()}*'
                                        c = f' {wordGuess[num].upper()}*'
                                    else:
                                        keyboard[b][keyboard[b].index(c)] = ' '
                                        c = ' '
                                if "*" not in c:
                                    str += f' {c} |' 
                                else:
                                    str += f'{c}|'
                            keys[count] = str
                            format += 3
                            count += 3
                    board[row] = f'{"|":>10}{wordDisplay[0]}|{wordDisplay[1]}|{wordDisplay[2]}|{wordDisplay[3]}|{wordDisplay[4]}|'
                    row += 2
                    if wordGuess == wordToGuess:
                        for line in board:
                            print(line)
                        for a in keys:
                            print(a)
                        print(f'Congrats! You guessed the word: {wordToGuess} \n \n')
                        return True
            else:
                print(f'"{wordGuess}" is not five characters. \n')
        else:
            print(f'"{wordGuess}" is not a valid word. Try again. \n')
    for line in board:
        print(line)
    for a in keys:
        print(a)
    print(f'The correct word was: {wordToGuess} \n')

if __name__ == "__main__":
    wins = 0
    wordList = open("./Python-WORDLE/words.txt").read().splitlines()
    guessList = open("./Python-WORDLE/guess.txt").read().splitlines()
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
            print(f'The number of games you won: {wins} \n \n')
        if userInput == 3:
            print("Thank you for playing! Goodbye!")
            exit()