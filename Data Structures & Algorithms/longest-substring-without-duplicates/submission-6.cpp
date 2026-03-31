class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int l = 0;
        int res = 0;
        vector<bool> seen(256, false);
        for(int r=0; r < n; r++){
            int idx = s[r];
            while (seen[idx]) {
                seen[s[l]] = false;
                l += 1;
            }
            seen[idx] = true;
            res = max(res, r - l + 1);
        }
        return res;
    }
};
