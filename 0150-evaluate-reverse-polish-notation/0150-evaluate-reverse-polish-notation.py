class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            elif token.lstrip("-").isnumeric():
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*" :
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a/b))
                    
        return stack[0]