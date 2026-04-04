class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # one line answer
        return Counter(s) == Counter(t)