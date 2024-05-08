def recurse(nums, arr):
    if len(nums) == 2:
        return [ arr + [nums[0]] + [nums[1]], arr + [nums[1]] + [nums[0]] ]
    else:
        r = []
        for i in range(0,len(nums)):
            t = nums[:]
            n = arr[:]
            n.insert(0,t[i])
            del(t[i])
            r += recurse(t, n)
        return r

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        return recurse(nums, [])
