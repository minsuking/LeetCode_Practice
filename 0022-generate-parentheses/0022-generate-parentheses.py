class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = [("(", 1, 0)]

        while stack:
            s, open, close = stack.pop()
            if open == close == n:
                res.append(s)
            else:
                if open < n:
                    stack.append((s + "(", open + 1, close))
                if close < open:
                    stack.append((s + ")", open, close + 1))

        return res