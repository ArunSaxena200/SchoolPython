def ucombo(input):
    freq = {}
    for nums in input:
        freq[nums] = freq.get(nums,0)+1
    freqset = set(freq.values())
    print(freq,freqset)

ucombo([1,2])