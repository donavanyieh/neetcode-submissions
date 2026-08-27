class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for c in s:
            if c not in parenthesis_map: # c is a parenthesis opening
                stack.append(c)
                continue
            else: # c is a parenthesis closer
                if len(stack) == 0:
                    return False
                elif parenthesis_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0