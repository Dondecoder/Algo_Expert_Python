# Name 

Run-Length Encoding

## Type of Question

Strings

## Difficulty

Easy

## Pre-requisites

Join Function

Iteration

## Description

Write a function that takes in a non-empty string and returns its run-length encoding. 

From Wikipedia, "run-length encodings is a form of loseless data compression in which runs of data are stored as a single data value and count, rather than as the original run." For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run - length encoded as "3A". 

To make things more complecate, however, the input sting can contain all sorts of special characters, including numbers. And since encoded data must be decodable this means that we cant naively run length encode long runs. For example, the run AAAAAAAAAA(12 As) cant naively be encoded as "12A"

## How I approached the problem

### Step One

* The first step is create an empty list and store it under a variable name `encodedStringCharacters = []`. Create a variable called `currentRunLength = 1`. 
    Sb - The reason you make `currentRunLength = 1` is because the descriptions states that you input string is non empty so the length will be at a minimum of 1.

### Step Two

* The next step is that you iterate through each index of the string starting at index 1 and save the value of string[i] in a currentCharacter variable and save string[i -1] in a previousCharacter variable. 

    ```python
    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]
    ```

### Step Three 

* You create an if statement that will be used to add values to the encodingStringCharacters list. 

    ```python
      if currentCharacter != previousCharacter or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(str(previousCharacter))
            currentRunLength = 0

        currentRunLength += 1
    ```

* The statement above will check to see if the string character is recurring or if the currentRunLength is equal to 9. If any of those clauses are hit then it will append to the empty encodedStringCharacters array the str(CurrentRunLength) and the value of the character. If it is not triggered it will continue incrementing the currentRunLength by 1. 

### Step Four

* The next step is preparing for the last value in the string which this formula as in stands doesn't add it. To work around this you can append the last value of the string out of the for loop you first append to the encodedstringCharacters array the currentRunLength and then you append the last value of the string to encodedStringCharacters array. 

    ```python
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])
    ```

### Step 5 

* Finally you use the .join function to join the strings in the encodedStringCharacters array into one string and return it. 

    ```python
    return "".join(encodedStringCharacters)
    ```