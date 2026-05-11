class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_r = 0
        num2_r = 0
        n1 = len(num1)
        n2 = len(num2)
        num_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        for i in range(n1):
            num1_r = 10 * num1_r + num_map[num1[i]]
        
        for i in range(n2):
            # print(10**(n2-i-1))
            num2_r = 10 * num2_r + num_map[num2[i]]
            print(num2_r)

        print(num1_r, num2_r)
        return str(num1_r * num2_r)
        