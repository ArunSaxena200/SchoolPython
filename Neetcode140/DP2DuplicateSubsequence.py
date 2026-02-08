def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    if n > m:
        return 0

    # dp[j] = ways to form t[0:j] using processed part of s
    dp = [0] * (n + 1)
    print("dp1 = ",dp)
    dp[0] = 1  # empty t
    print("dp2 = ",dp)


    for i in range(1, m + 1):
        # reverse loop IMPORTANT (warna overwrite ho jayega)
        for j in range(n, 0, -1):
            #print("i=",i,"j=",j)
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]

    return dp[n]


s="rabbbit" 
t="rabbit"

print(numDistinct(s,t))
