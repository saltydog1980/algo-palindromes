import re

def palindrome(word):
    #check to see if input is a number
    if str(word).isnumeric():
        #if number, cast to string, reversing, cast to list then joining and cast back to int
        b_word = int(''.join(list(reversed(str(word)))))
        #return boolean for comparison of input vs reveresd b-word
        return word == b_word
    #else if not a number take word to lower, removing everything but alpha then joining back to word
    #doing same for b_word but also reversing it
    else:
        a_word = ''.join(list(re.sub("[^a-z0-9]+", '', word.lower())))
        b_word = ''.join(list(reversed(re.sub("[^a-z0-9]+", '', word.lower()))))
        #returning the boolean for comparing a vs b
        return a_word == b_word


# print(palindrome('racecar')) #=== true);
# palindrome('Noon') #=== true);
# print(palindrome('ciVic')) #=== true);
# print(palindrome('nice')) #=== false);
# print(palindrome(434)) #=== true);
# print(palindrome(123)) #=== false);

# //console.log("The following should be true if you're trying to do the extra portion of this challenge");
# print(palindrome("Sore was I ere I saw Eros.")) #=== true);
# print(palindrome("A man, a plan, a canal -- Panama")) #=== true);