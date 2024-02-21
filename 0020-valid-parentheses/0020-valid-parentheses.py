class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {')':'('
               ,']':'['
               ,'}':'{'
               }
        stack = []
        for c in s:
            if c in map_ and stack:
                v = stack.pop()
                if v!= map_[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        