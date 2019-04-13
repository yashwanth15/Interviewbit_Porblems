import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        minimum = sys.maxsize
        result =0
        A.sort()
        for i in range(len(A)):
            l=i+1
            h=len(A)-1
            while(l<h):
                threeSum=A[i]+A[l]+A[h]
                difference = abs(threeSum-B)
                if difference ==0:
                    return threeSum
                if difference<minimum:
                    minimum=difference
                    result=threeSum
                if threeSum<B:
                    l+=1
                else:
                    h-=1
        return result
