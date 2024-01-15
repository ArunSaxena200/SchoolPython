def minimumAbsDifference(arr):
        
        '''
        4,2,1,3

        1,2,3,9

        '''
        arr.sort()
        small = 99999
        res = []
        for i in range(len(arr)-1):
            first = arr[i]
            next = arr[i+1]
            #print([first,next])
            diff = next - first
            #print(diff)
            if  diff < small:
                small = diff
                #print(small)
                res =  [[first,next]]
            elif diff == small:
                 res.append([first,next])
        return res

print(minimumAbsDifference([4,2,1,3]))