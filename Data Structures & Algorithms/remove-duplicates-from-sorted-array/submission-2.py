class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 #here I am placing the left pointer at 1 because at index 0 no matter what the number is it will be unique
        for r in range(1, len(nums)): #this means the right pointer will iterate (go through) each value of the list one by one starting at the index of one for the length of nums list 
            if nums[r] != nums[r - 1]: #this means that if the right pointer IS NOT equal to the number index before it [n - 1] then 
                nums[l] = nums[r] #then ... we need to make the left pointer equal to the right to store the correct number on the index
                l += 1 #we also must increment the left pointer since it is not part of the loop like the right we also need to move it forward so it can hold the next place of the number
        return l