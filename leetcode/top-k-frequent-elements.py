class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        nums_list = {}

        for i in range(len(nums)):
            if nums[i] not in nums_list:
                nums_list[nums[i]] = 0
            nums_list[nums[i]] += 1
        
        nums_list_2 = nums_list.items()

        sorted_nums_list = sorted(nums_list_2, key=lambda x: x[1], reverse=True)

        top_k = []
        for i in range(k):
            top_k.append(sorted_nums_list[i][0])

        return top_k