def isPalindrome(string):
    # Write your code here.
    return isPalindromeHelper(string, 0, len(string) - 1)


def isPalindromeHelper(string, start, end):
    if len(string) <= 1:
        return False
    while start < end:
        if string[start] != string[end]:
            return False
        elif string[start] == string[end]:
            start += 1
            end -=1
    return True