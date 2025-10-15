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
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        operations = ["+", "-", "/", "*"]
        cur_sum = 0

        for op in tokens:
            if op == "+":
                cur_sum = stack.pop() + stack.pop()
                stack.append(cur_sum)

            elif op == "-":
                a,b = stack.pop(), stack.pop()
                cur_sum = b - a
                stack.append(cur_sum)

            elif op == "/":
                a, b = stack.pop(), stack.pop()
                cur_sum = int(float(b)/a)
                stack.append(cur_sum)
            
            elif op == "*":
                cur_sum = stack.pop() * stack.pop()
                stack.append(cur_sum)
            
            else:
                stack.append(int(op))

        return stack[-1]

                

            

        
```