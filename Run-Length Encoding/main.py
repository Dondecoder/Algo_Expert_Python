#O(n) time | O(n) space - where n is the length of the input sting
def runlineEncoding(string):
    encodedStringCharacters = []
    currentRunLength = 1

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i -1]

        if currentCharacter != previousCharacter or currentCharacter == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(str(previousCharacter))
            currentRunLength = 0

        currentRunLength += 1

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(str(len(string) - 1))

    return "".join(encodedStringCharacters)