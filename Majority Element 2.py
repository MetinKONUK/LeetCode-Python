def majorityElement(self, nums: List[int]) -> int:
    n = len(nums) / 2 #Wanted criteria -nums.count(number) > len(nums) / 2-
    for i in set(nums): #do not chech same numbers again and again, use set
        if nums.count(i) > n: return i #if you found the solution then no need to scan the rest of the numbers
