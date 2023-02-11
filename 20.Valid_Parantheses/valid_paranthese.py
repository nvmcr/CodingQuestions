class Solution:
    def isValid(self, s: str) -> bool:
        #Map the closing brackets to opening as we check for closures
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in hashmap:
                if stack and hashmap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
