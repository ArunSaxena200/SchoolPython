def exists(grid,word):
    '''
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]], word = "ABCCED"
    Output: true
    '''
    def dfs(i,j,k):
        #base case
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or  grid[i][j] != word[k]:
            return False
        if k == len(word)-1:
           return True
        #traversal
        res = dfs(i-1,j,k+1) or  dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
        return res
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i,j,0):
                return True
    return False

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

word = "BCCED"

result = exists(board, word)
print(result)

