class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new_string = s.strip()
        new_string = "".join(new_string.split())
        new_string = new_string.lower()
        new_string_list = list(new_string)
        filter_string = []

        for i in range(len(new_string_list)):
           if new_string[i].isalnum():
                filter_string.append(new_string_list[i])

        if filter_string == []:
            return True
        
        for i in range(0, len(filter_string)//2):
            if filter_string[i] != filter_string[-(i+1)]:
                return False
        return True