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

        unmatched, count, encountered = 0, 0, set()
        for i in range(len(s)):
            ch = s[i]
            if ch not in encountered:
                unmatched += 1
                encountered.add(ch)
            count += 1
            if i == hm[ch]:
                unmatched -= 1

            if unmatched == 0:
                res.append(count)
                count = 0
                encountered = set()
        return res
        

        
