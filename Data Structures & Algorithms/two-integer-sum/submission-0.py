class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #this is the hashmap that will be holding the value : index

        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[j] = i
        
        