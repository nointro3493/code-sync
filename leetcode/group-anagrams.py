class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        list_anagrams = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in list_anagrams:
                list_anagrams[key] = []
            list_anagrams[key].append(strs[i])
        return list(list_anagrams.values())