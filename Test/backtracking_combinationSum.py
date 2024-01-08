def combination_sum(k,n):
    
    '''
    1,2,3,4,5,6,7,8,9

    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]   

    '''
    result = []
    def backtrack(build,num,sum_so_far):
        #base
        if len(build)==k and sum_so_far == n:
            result.append(build)
            return
        
        #recursion
        for i in range(num,9+1):
            #print("sum",sum_so_far+i)
            if sum_so_far + i > n:
                break
            
            backtrack(build+[i],i+1,sum_so_far+i)


    backtrack([],1,0)
    return result



    
# Example usage:
k1, n1 = 3, 9
output1 = combination_sum(k1, n1)
print(output1)  # Output: [[1, 2, 4]]
