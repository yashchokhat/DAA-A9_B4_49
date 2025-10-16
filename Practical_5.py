def lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0]*(n+1) for _ in range(m+1)]
    D = [['']*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
                D[i][j] = 'd'
            elif L[i-1][j] >= L[i][j-1]:
                L[i][j] = L[i-1][j]
                D[i][j] = 'u'
            else:
                L[i][j] = L[i][j-1]
                D[i][j] = 'l'
    s, i, j = "", m, n
    while i > 0 and j > 0:
        if D[i][j] == 'd':
            s = X[i-1] + s
            i -= 1; j -= 1
        elif D[i][j] == 'u': i -= 1
        else: j -= 1
    return L[m][n], s, L, D

def lrs_len(S):
    n = len(S)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]

def lrs_str(S):
    n = len(S)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    s, i, j = "", n, n
    while i > 0 and j > 0:
        if dp[i][j] == 1 + dp[i-1][j-1] and S[i-1] == S[j-1] and i != j:
            s = S[i-1] + s
            i -= 1; j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else: j -= 1
    return s

X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"
l, s, cm, dm = lcs(X, Y)
print("--- TASK-1: LCS ---")
print("X:", X)
print("Y:", Y)
print("\nCost Matrix:")
for r in cm: print(r)
print("\nDirection Matrix:")
for r in dm: print(r)
print("\nLength:", l)
print("LCS:", s)

S = "AABCBDC"
print("\n--- TASK-2: LRS ---")
print("S:", S)
print("Length:", lrs_len(S))
print("LRS:", lrs_str(S))
