def costArray(costArrayInp):
    '''
    
        You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, 
        you can either climb one or two steps.

        You can either start from the step with index 0, or the step with index 1.

        Return the minimum cost to reach the top of the floor.

        

        Example 1:

        Input: cost = [10,15,20],0
        Output: 15
        Explanation: You will start at index 1.
        - Pay 15 and climb two steps to reach the top.
        The total cost is 15.

    '''
    costArrayInp.append(0)
    for i in range(len(costArrayInp)-3,-1,-1):
        costArrayInp[i] = min(costArrayInp[i]+costArrayInp[i+1],costArrayInp[i]+costArrayInp[i+2])
    return min(costArrayInp[i],costArrayInp[i+1])


print(costArray([10,15,20]))
