def combination_sum(k,n):
    res = []
    def backtrack(build,num,sum_so_far):
        if len(build)==k and sum_so_far ==n:
            res.append(build)
            return
    
        for i in range(num,9+1):
            if sum_so_far > n:
                break
        
            backtrack(build+[i],i+1,sum_so_far+i)
    backtrack([],1,0)
    return res


# Example usage:
k1, n1 = 4, 10
output1 = combination_sum(k1, n1)
print(output1)  # Output: [[1, 2, 4]]