from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c  = defaultdict(set),defaultdict(set)
        b = defaultdict(set)
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                num = board[i][j]
                x, y = 3 * (i//3), 3 * (j//3)
                if num != "." and (num in r[i] or num in c[j] or num in b[(x,y)]):
                    return False
                r[i].add(num)
                c[j].add(num)
                b[(x,y)].add(num)
        return True
        
        