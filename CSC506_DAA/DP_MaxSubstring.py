def longestSubSeq(str1,str2):
    # create matrix
    matrix = []
    #create storage matrix
    for i in range(len(str1)):
        matrix.append([0]* len(str2))
    print(matrix)

longestSubSeq('looking','look')