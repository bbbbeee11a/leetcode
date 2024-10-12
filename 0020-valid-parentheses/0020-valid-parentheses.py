class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        for x in s:
            if x in "([{":
                li.append(x)
            elif x in ")]}":
                if li:
                    y = li.pop()
                    if y == "(" and x == ")":
                        continue
                    elif y == "[" and x == "]":
                        continue
                    elif y == "{" and x == "}":
                        continue
                    else:
                        return False
                else:
                    return False
        if li:
            return False
        else:
            return True
    # print("true") if isValid(self, s) else print("false")