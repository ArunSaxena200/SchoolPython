'''
k,n
k=3,n=9
1,2,3,4,5,6,7,8,9
'''

def combSum(k,n):
    res = []
    def backtrack(build,num,sum):
        #base
        if sum==n and len(build)==k:
            res.append(build)
            return
        # iteration
        for i in range(num,9+1):
            if sum + i>n:
                break
            backtrack(build + [i],i+1,sum+i)
    backtrack([],1,0)
    return res

print(combSum(3,9))