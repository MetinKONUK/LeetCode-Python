    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in range(len(nums)):
            if not nums[i] in nums[:i]:
                nums[p] = nums[i]
                p += 1
        return p
"""
Just iterating through every element and appending every first unique element to head of the list
And returning the unique element count so judge can take nums[:unique_element_count] list
"""
