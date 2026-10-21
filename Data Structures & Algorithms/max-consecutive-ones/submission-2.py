class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        loop_count = 0

        for numbers in nums:
            if numbers == 1:
                loop_count += 1
                count = max(count, loop_count)
            if numbers == 0:
                loop_count =  0
            
        return count