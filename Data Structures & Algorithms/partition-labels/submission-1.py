class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        memo = [0] * 26
        res = []
        for i in range(len(s)):
            ch = s[i]
            if ch not in hm:
                hm[ch] = i
            hm[ch] = i

        end, count = 0, 0
        for i in range(len(s)):
            end = max(end, hm[s[i]])
            count += 1

            if i == end:
                res.append(count)
                count = 0
        return res
        

        
