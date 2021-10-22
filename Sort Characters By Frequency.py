def frequencySort(self, s: str) -> str:
    alphas = set(s) #take all unique values to an iterable DS
    statistics = dict() #create a dictionary to keep both count and the letter itself
    for a in alphas:
        statistics[a] = s.count(a) #assign letter's count to it {"A": s.count("A")} 
    values = sorted(statistics.items(), key=lambda x: x[1], reverse=True) #sort dictionary in decreasing order by count values
    result = "" #initialize an empty string to assign letters in order 
    for a in values:
        result += a[0]*a[1] #Assign letters times their count in s
    return result #return wanted result string
