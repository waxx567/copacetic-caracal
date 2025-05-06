def reverse_word(word):
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

def is_palindrome(word):
        return word == reverse_word(word)

def check_all_palindromes(arr):
        for word in arr:
                if is_palindrome(word) == False:
                        return False
        return True