def longestPalindrome(string):
    alphas, plusone = {}, False #define dictionary and boolean checker
    for letter in string: #iterate through string
        if letter in alphas: #increment letters count value in dictionary for every occurance
            alphas[letter] += 1
        else:
            alphas[letter] = 1 #start the value as 1 for the first occurance
    for i in alphas.values():
        if i % 2: plusone = True #if there is an odd count it means we can use "1" letter at the middle
    result = sum([x - 1 if x % 2 else x for x in alphas.values()]) #define the result for plusone = False condition
    return result+1 if plusone else result #return the true result checking whether plusone is True or False
