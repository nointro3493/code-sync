class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        final  = [1] * n

        prefix_val = 1
        suffix_val = 1

        # build prefix
        for i in range(n):
            prefix[i] = prefix_val
            prefix_val *= nums[i]

        # build suffix
        for i in range(n-1, -1, -1):
            suffix[i] = suffix_val
            suffix_val *= nums[i]

        # combine
        for i in range(n):
            final[i] = prefix[i] * suffix[i]

        return final