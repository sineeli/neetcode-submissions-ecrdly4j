class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);

        int l = 0;
        int res = 0;
        int max_freq = INT_MIN;
        for (int r = 0; r < s.size(); r++){
            count[s[r] - 'A'] += 1;
            max_freq = max(count[s[r] - 'A'], max_freq);
            while ((r - l + 1) - max_freq > k) {
                count[s[l] - 'A'] -= 1;
                l += 1;
            }
            res = max(r - l + 1, res);
        }
        return res;

    }
};
