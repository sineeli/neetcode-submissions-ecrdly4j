class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size();
        int n = s2.size();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return dfs(0, 0, s1, s2, s3, dp);
        
    }
    bool dfs(int i, int j, string& s1, string& s2, string& s3, vector<vector<int>>& dp){
        if (i + j == s3.size()) {
            if (i == s1.size() and j == s2.size()) {
                return true;
            }
        }
        if (dp[i][j] != -1) return dp[i][j];

        int k = i + j;
        if (i < s1.size() && s3[k] == s1[i]) {
            if (dfs(i + 1, j, s1, s2, s3, dp)) return true;
        }
        if (j < s2.size() && s3[k] == s2[j]) {
            if (dfs(i, j + 1, s1, s2, s3, dp)) return true;
        }
        dp[i][j] = false;
        return false;
    }
};
