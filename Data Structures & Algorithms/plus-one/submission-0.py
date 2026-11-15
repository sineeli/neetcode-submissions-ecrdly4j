class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            temp = digits[i] + carry
            carry = temp // 10
            digits[i] = temp % 10
        
        if carry:
            return [carry] + digits

        return digits 