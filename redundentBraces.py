class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack=[]
        for i in A:
            if i=='(' or i=='+' or i=='-' or i=='*' or i=='/':
                stack.append(i)
            elif i==')':
                top=stack.pop()
                if top=='(':
                    return 1
                else:
                    while top!='(':
                        top=stack.pop()
        return 0
