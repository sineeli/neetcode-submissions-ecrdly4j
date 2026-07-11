class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        main_s1_count = Counter(s1)
        for i in range(0, n):
            temp_dict = Counter(s2[i:i+m])
            if temp_dict == main_s1_count:
                return True

        return False

        