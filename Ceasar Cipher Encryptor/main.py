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