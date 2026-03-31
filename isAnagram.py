class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(26n)time complexity because the count() method 
        #loops through n chars in the strings 26 times.
        countListForS = []
        countListForT = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"   
        if len(s) != len(t): 
            return False
        else:
            for char in alphabet:
                countListForS.append(s.count(char))
                countListForT.append(t.count(char))
            if countListForS == countListForT:
                return True
            else:
                return False
                
        # O(n) time bcs we loop through n chars
        # in both strings only one time.
        if len(s) != len(t):
            return False
        counts = [0] * 26
        aOrd = ord('a')
        for ch in s:
            counts[ord(ch) - aOrd] += 1
        for ch in t:
            counts[ord(ch) - aOrd] -= 1
            if counts[ord(ch) - aOrd] < 0:
                return False
        return True
