def plusOne(self, digits: List[int]) -> List[int]:
    number, n = 0, len(digits)-1 #Initialize the number, assign the proper value to n
    for i in digits: #Iterate through digits array
        number += 10**n * i # Do the reverse-mod(10) to find value of the number
        n -= 1 #10**2 * 1 = 100  10**1 * 2 = 20 10**0 * 3 = 3 --> 123
    number += 1 #123 + 1 = 124
    return [int(x) for x in str(number)] # turning number(124) to list(1, 2, 4) process
  
