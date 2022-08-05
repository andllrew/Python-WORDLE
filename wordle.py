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
                    if wordGuess == wordToGuess:
                        for line in board:
                            print(line)
                        for a in keys:
                            print(a)
                        print(f'Congrats! You guessed the word: {wordToGuess} \n \n')
                        return row, True
                    row += 2
            else:
                print(f'"{wordGuess}" is not five characters. \n')
        else:
            print(f'"{wordGuess}" is not a valid word. Try again. \n')
    for line in board:
        print(line)
    for a in keys:
        print(a)
    print(f'The correct word was: {wordToGuess} \n')
    return 0, False

def stat(wins, board):
    if wins == 1:
        board["ONE"] += 1
    if wins == 3:
        board["TWO"] += 1
    if wins == 5:
        board["THREE"] += 1
    if wins == 7:
        board["FOUR"] += 1
    if wins == 9:
        board["FIVE"] += 1
    if wins == 11:
        board["SIX"] += 1

if __name__ == "__main__":
    scores = {"ONE": 0,
              "TWO": 0,
              "THREE": 0,
              "FOUR": 0,
              "FIVE": 0,
              "SIX": 0}
    wordList = open("./Python-WORDLE/words.txt").read().splitlines()
    guessList = open("./Python-WORDLE/guess.txt").read().splitlines()
    while True:
        print(f'Welcome to the Python Wordle Game! \n \n' +
        f'{"1. Play the game":>22} \n' +
        f'{"2. Display stats":>22} \n' +
        f'{"3. Exit":>13}')
        userInput = valid()
        if userInput == 1:
            result, check = play()
            if check == True:
                stat(result, scores)
        if userInput == 2:
            index = 0
            statIndex = 1
            str = [f'{"+":>9}-------+---+',
                   f'{"| ":>10}{list(scores.keys())[0]}   |',
                   f'{"+":>9}-------+---+',
                   f'{"| ":>10}{list(scores.keys())[1]}   |',
                   f'{"+":>9}-------+---+',
                   f'{"| ":>10}{list(scores.keys())[2]} |',
                   f'{"+":>9}-------+---+',
                   f'{"| ":>10}{list(scores.keys())[3]}  |',
                   f'{"+":>9}-------+---+',
                   f'{"| ":>10}{list(scores.keys())[4]}  |',
                   f'{"+":>9}-------+---+',
                   f'{"| ":>10}{list(scores.keys())[5]}   |',
                   f'{"+":>9}-------+---+ \n',]
            for point in scores:
                if scores[point] < 10:
                    str[statIndex] += f' {scores[list(scores.keys())[index]]} |'
                if 9 < scores[point] < 100:
                    str[statIndex] += f'{scores[list(scores.keys())[index]]} |'
                if 99 < scores[point] < 1000:
                    str[statIndex] += f'{scores[list(scores.keys())[index]]}|'
                index += 1
                statIndex += 2
            for lines in str:
                print(lines)
        if userInput == 3:
            print("Thank you for playing! Goodbye!")
            exit()