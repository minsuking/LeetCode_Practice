class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []
        stack = [("(", 1, 0)]

        while stack:
            s, open_count, close_count = stack.pop()
            if open_count == close_count == n:
                result.append(s)
            else:
                if open_count < n:
                    stack.append((s + "(", open_count + 1, close_count))
                if close_count < open_count:
                    stack.append((s + ")", open_count, close_count + 1))

        return result
        