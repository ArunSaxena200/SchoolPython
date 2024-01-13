from collections import Counter
def wordMatch(word1,word2):
    if len(word1)!=len(word2):
        return False
    if set(word1)!=set(word2):
        return False
    # freq check
    freqWord1 = Counter(word1)
    freqWord2 = Counter(word2)

    if freqWord1 == freqWord2:
        return True
    
    occurance_freq1 = Counter(line for line in freqWord1.values())
    occurance_freq2 = Counter(line for line in freqWord2.values())

    if occurance_freq1 != occurance_freq2:
        return False

    return True

print(wordMatch('abbzzca','babzzcz'))
