class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        fir, sec, curr = 1, 1, 0
        
        for i in range(1, len(s)):
            num = int(s[i])
            if num > 0 and num < 10:
                curr += sec
            two = int(s[i-1:i+1])
            if two >= 10 and two <= 26:
                curr += fir
            fir = sec
            sec = curr
            curr = 0
            
        return sec

