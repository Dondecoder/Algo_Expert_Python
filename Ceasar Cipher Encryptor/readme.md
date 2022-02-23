# Name 

Caesar Cipher Encryptor

## Type of Question

Strings

## Difficulty

Easy

## Pre-requisites
* `Modulo`
* `.join` function
* `ord` function
* `chr` function

## Description

Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet where k is the key.

Note that letters shoul "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a 

## How I approached the problem

* For this problem the first thing that you need to do is created a function that takes in a string and a key. Within this function I created an alphabet variable that took in a list of alphabets in string value. 

* Second I created a string_size variable that took in the `len(alphabet)` array. 

* Third I created a new_string variable that will take in an empty array

* Fourth I created a new_key variable that will receive the remainder of the key value modulo string_size. The purpose of the is for wrapping around the alphabet array. So if a key value is greater than the alphabet list it will wrap around the array and return the index of the alphabet that will follow. 
Ex: `key = 52` and `string_size = 26` the modulo of that would be 0 because 52 divides evenly into 26 so the new_key value would be 0 

* The fifth thing is to create a for loop to traverse the string array and for each value in the string array we will append a value in the new_string array. In order to do that we should create a helper function that will traverse the alphabet array and return the value in the new_string array. 

* The sixth thing is to create a helper function that takes in a letter, key, alphabet. In order to append the right value into the new_string array we need to input the letter paramater, new_key, and the alphabet paramater. The helper function will calculate a new_key_value = alphabet.index(letter) + key and then it will return alphabet[new_key_value % len(alphabet)]. It will continue traversing the string array and appending a value in the new_string array for each value in the string array. 

* Finally we will return ".join(x for x in new_string). This will return a new string for each value in the new_String array then it will join all the strings as one string.

Your final code should look like this:


```python
# function returns a new string 
# shifts every letter in the string by k positions in the alphabet 

#string: "lmn"
# key: 4
# output: p,q,r

def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"
				,"y","z"]
	string_size = len(alphabet)
	new_string = []
	new_key = key % string_size
	for letter in string:
		new_string.append(ceasarHelper(letter, new_key, alphabet))
	return "".join(x for x in new_string)

def ceasarHelper(letter, key, alphabet):
	new_key_value = alphabet.index(letter) + key
	return alphabet[new_key_value % len(alphabet)]
```

