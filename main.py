import random

def generatePassword(length):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$' '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '<', '>', '?', '/']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    validCharacters = letters + symbols + numbers
    random.shuffle(validCharacters)
    randomNumbers = []
    password = ''

    for i in range(length):
        randomNumbers.append(random.randrange(0, len(validCharacters)))
    
    for j in range(length):
        ifLowercase = random.randrange(1, 3)
        if validCharacters[randomNumbers[j]] in letters:
            if ifLowercase % 2 == 0:
                validCharacters[randomNumbers[j]] = validCharacters[randomNumbers[j]].lower()

        password = password + validCharacters[randomNumbers[j]]
    
    return password