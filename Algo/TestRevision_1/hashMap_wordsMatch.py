from collections import Counter
def wmatch(w1,w2):
    if len(w1) != len(w2):
        return False
    if set(w1) != set(w2):
        return False
    return True

print(wmatch("listen","silent"))