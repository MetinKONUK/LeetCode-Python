def generate(self, numRows: int) -> List[List[int]]:
    def pascal(n): #Calculating each particular line's numbers
        line = [1]
        for k in range(n):
            line.append(line[k]*(n-k)//(k+1)) #Integer division to prevent .0's
        return line
    result = []
    for i in range(numRows):
        result.append(pascal(i)) #Assigning particular results to main result 
    return result #return the main result
