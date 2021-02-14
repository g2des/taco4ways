class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums.sort()
        for index, num in enumerate(nums):
            num_set = set(nums[index+1:])
            if target-num in num_set:    
                return [index, index+1+nums[index+1:].index(target-num)]
            # if target-num in nums[index+1:]:
                # return [index,index + nums[index+1:].index(target-num)+1 ]

if __name__ ==  '__main__':
    s = Solution()
    result = s.twoSum([2,7,11,15], target=9)
    for num in result:
        assert num in [0,1]
    print(result)