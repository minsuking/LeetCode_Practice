import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]",'',s.lower().replace(' ',''))
        return s == s[::-1]