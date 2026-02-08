def topk(nums,k):
    count ={}
    for chars in nums:
        count[chars] = count.get(chars,0)+1
    print(count)

    bucket = [[] for i in range(len(nums)+1)]

    for num in count:
        freq = count[num]
        bucket[freq].append(num)
    print(bucket)

    res = []
    for freq_index in range(len(bucket)-1,0,-1):
        for nums in bucket[freq_index]:
            res.append(nums)
            if len(res)==k:
                return res


nums=[1,1,1,2,2,3]
k1=2

print(topk(nums,k1))