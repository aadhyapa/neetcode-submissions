class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        first = digits[-1] + 1
        carryforward = 1 if first > 9 else 0
        res.append(first % 10)

        for i in range(len(digits) - 2, -1, -1):
            dig = digits[i] + carryforward
            carryforward = 1 if dig > 9 else 0
            res.append(dig % 10)

        if carryforward:
            res.append(carryforward)

        return res[::-1]
