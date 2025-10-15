# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python []
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_bracks = {")":"(", "}":"{", "]":"["}
        stack = []
        
        for i in range(len(s)):
            if s[i] in valid_bracks:
                if stack and stack[-1] == valid_bracks[s[i]]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(s[i])

        if stack:
            return False
        else:
            return True

                    
```