class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter = 0
        result = 0

        index = 0
        while index < len(nums):

            if nums[index] == 0:
                counter = 0

            else:
                counter += 1

            result = max(result, counter)

            index +=1
        
        return result