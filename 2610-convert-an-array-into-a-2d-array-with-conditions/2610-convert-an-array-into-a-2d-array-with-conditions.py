class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            n = nums.pop()
            flag = True
            for i in range(len(res)):
                if n not in res[i]:
                    res[i].append(n)
                    flag = False
                    break
            if flag:
                res.append([n])
        return res
            