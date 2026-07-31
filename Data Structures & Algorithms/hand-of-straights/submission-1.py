class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        hm = {}

        for i in hand:
            if i not in hm:
                hm[i] = 0
            hm[i] += 1

        for i in hand:
            if hm[i] == 0:
                continue
            for i in range(i, i + groupSize):
                if i not in hm or hm[i] == 0:
                    return False
                hm[i] -= 1
        
        return True

        
        

            