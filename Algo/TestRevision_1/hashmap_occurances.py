def uq(input):
    freq={}
    for num in input:
        freq[num] = freq.get(num,0)+1
    freqSet = set(freq.values())
    print(freqSet)
    return len(freq)==len(freqSet)

print(uq([1,2,2,1,1,3]))