# Link: https://leetcode.com/problems/valid-parentheses
# Time complexity: O(n)
# Week: 2
def isValid(s):
    d = {'(':')', '{':'}','[':']'}
    m = []

    for i in s:

        if i in d:
            m.append(i)
            print(m)

        else: 
            if len(m) and d[m[-1]] == i:
                print("Before delete ")
                print(m)
                del m[-1]
                print("After delete ")
                print(m)

            else:
                return False

    return not m

print(isValid("()"))

"""
    def isValid(self, s: str) -> bool:
        while(("()" in s) or ("{}" in s) or ("[]" in s)):
            if "()" in s:
                s = s.replace("()", "")
            if "{}" in s:
                s = s.replace("{}", "")
            if "[]" in s:
                s = s.replace("[]", "")
        return s == ""

    def isValid(self, s: str) -> bool:
	pairs = {')':'(', 
			 ']':'[', 
			 '}':'{'}

	stack = []
	for char in s:
		if char in pairs and len(stack)>0:
			openingBrace = pairs[char]
			if stack[-1] != openingBrace:
				return False
			stack.pop()
		else:
			stack.append(char)

	return len(stack)==0

    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            else:
                if not st:
                    return False
                if i ==")":
                    if st.pop()!='(':
                        return False
                elif i =="}":
                    if st.pop()!='{':
                        return False
                elif i =="]":
                    if st.pop()!='[':
                        return False
        if st:
            return False
        return True

"""
